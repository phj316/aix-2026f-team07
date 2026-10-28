"""T5: 주택용 전력(저압) 전기요금 계산 로직.

요금 산정 순서 (한전 청구서 기준)
  1. 기본요금      : 사용량이 속한 '최종' 누진 단계의 기본요금 1건
  2. 전력량요금    : 구간별로 나눠 단가를 곱해 합산 (원 미만 절사)
  3. 기후환경요금  : 사용량 × 9원      (원 미만 절사)   ※ include_surcharges=True일 때
  4. 연료비조정요금: 사용량 × 5원      (원 미만 절사)   ※ include_surcharges=True일 때
  5. 전기요금계    = 1 + 2 + 3 + 4
  6. 부가가치세    = 전기요금계 × 10%  (원 미만 반올림)
  7. 전력기금      = 전기요금계 × 2.7% (10원 미만 절사)
  8. 청구금액      = 5 + 6 + 7         (10원 미만 절사)
"""

import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

RATES_PATH = Path(__file__).with_name("rates.json")


def load_rates(path=RATES_PATH):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


_RATES = load_rates()


def _d(value):
    """float 오차를 피하려고 Decimal로 변환 (예: 214.6 * 195)."""
    return Decimal(str(value))


def _floor_won(value):
    return int(value.to_integral_value(rounding="ROUND_FLOOR"))


def _floor_10(value):
    return int(value // 10 * 10)


def _season_for(month, rates):
    for key, season in rates["seasons"].items():
        if month in season["months"]:
            return key, season
    raise ValueError(f"월(month)은 1~12 사이여야 합니다: {month}")


def calculate_electricity_fee(usage_kwh, month, include_surcharges=True, rates=None):
    """사용량(kWh)과 월로 누진 단계와 예상 청구금액을 계산한다.

    Args:
        usage_kwh: 월 사용량 (0 이상의 정수 kWh — 고지서·계량기 값은 정수)
        month: 1~12
        include_surcharges: 기후환경요금·연료비조정요금 포함 여부 (실제 청구서엔 포함)
        rates: 요금표 dict (기본값: rates.json)

    Returns:
        dict — stage, base_fee, usage_fee, total_estimated_fee,
               remaining_kwh_to_next_stage, season, breakdown
    """
    rates = rates or _RATES

    if isinstance(usage_kwh, bool) or not isinstance(usage_kwh, int):
        raise TypeError(f"사용량은 정수(kWh)여야 합니다: {usage_kwh!r}")
    if usage_kwh < 0:
        raise ValueError(f"사용량은 0 이상이어야 합니다: {usage_kwh}")
    if isinstance(month, bool) or not isinstance(month, int):
        raise TypeError(f"월은 정수여야 합니다: {month!r}")

    season_key, season = _season_for(month, rates)
    stages = season["stages"]

    # 1) 현재 누진 단계
    current = next(s for s in stages if s["max_kwh"] is None or usage_kwh <= s["max_kwh"])

    # 2) 전력량요금: 구간별 누적 계산
    usage_fee = Decimal(0)
    prev_max = 0
    for s in stages:
        upper = usage_kwh if s["max_kwh"] is None else min(usage_kwh, s["max_kwh"])
        kwh_in_stage = max(0, upper - prev_max)
        usage_fee += kwh_in_stage * _d(s["rate_per_kwh"])
        if s["max_kwh"] is None or usage_kwh <= s["max_kwh"]:
            break
        prev_max = s["max_kwh"]

    # 슈퍼유저: 하계·동계 1,000kWh 초과분은 3단계 단가 대신 슈퍼유저 단가
    su = rates.get("super_user")
    if su and month in su["months"] and usage_kwh > su["threshold_kwh"]:
        excess = usage_kwh - su["threshold_kwh"]
        stage3_rate = _d(stages[-1]["rate_per_kwh"])
        usage_fee += excess * (_d(su["rate_per_kwh"]) - stage3_rate)

    usage_fee = _floor_won(usage_fee)
    base_fee = current["base_fee"]

    # 3) 기후환경요금 · 연료비조정요금
    climate_fee = fuel_fee = 0
    if include_surcharges:
        sc = rates["surcharges"]
        climate_fee = _floor_won(usage_kwh * _d(sc["climate_environment_fee_per_kwh"]))
        fuel_fee = _floor_won(usage_kwh * _d(sc["fuel_cost_adjustment_per_kwh"]))

    # 4) 세금·기금
    subtotal = base_fee + usage_fee + climate_fee + fuel_fee
    vat = int((subtotal * _d(rates["taxes"]["vat_rate"])).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    power_fund = _floor_10(_floor_won(subtotal * _d(rates["taxes"]["power_fund_rate"])))
    total = _floor_10(subtotal + vat + power_fund)

    # 5) 다음 단계 진입 전까지 현재 단계에서 더 쓸 수 있는 kWh (3단계는 0)
    remaining = 0 if current["max_kwh"] is None else current["max_kwh"] - usage_kwh

    return {
        "stage": current["stage"],
        "base_fee": base_fee,
        "usage_fee": usage_fee,
        "total_estimated_fee": total,
        "remaining_kwh_to_next_stage": remaining,
        "season": season_key,
        "breakdown": {
            "climate_environment_fee": climate_fee,
            "fuel_cost_adjustment": fuel_fee,
            "subtotal": subtotal,
            "vat": vat,
            "power_fund": power_fund,
        },
    }


if __name__ == "__main__":
    for kwh, m in [(150, 5), (210, 5), (450, 5), (310, 7), (0, 5)]:
        print(kwh, m, calculate_electricity_fee(kwh, m))
