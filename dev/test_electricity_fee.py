"""T5 테스트. 실행: python -m unittest -v test_electricity_fee  (pytest로도 실행 가능)

기대값은 코드와 별개로 손으로 계산한 값이다. (기후환경 9원 + 연료비조정 5원 포함)
"""

import unittest

from electricity_fee import calculate_electricity_fee as calc


class RequiredCases(unittest.TestCase):
    """기획서 T5 완료 조건의 테스트 5건."""

    def check(self, kwh, month, stage, base, usage, total, remaining):
        r = calc(kwh, month)
        self.assertEqual(r["stage"], stage)
        self.assertEqual(r["base_fee"], base)
        self.assertEqual(r["usage_fee"], usage)
        self.assertEqual(r["total_estimated_fee"], total)
        self.assertEqual(r["remaining_kwh_to_next_stage"], remaining)

    def test_case1_150kwh_other_season(self):
        # 150×120 = 18,000
        self.check(150, 5, stage=1, base=910, usage=18_000, total=23_670, remaining=50)

    def test_case2_210kwh_other_season(self):
        # 200×120 + 10×214.6 = 26,146
        self.check(210, 5, stage=2, base=1_600, usage=26_146, total=34_570, remaining=190)

    def test_case3_450kwh_other_season(self):
        # 200×120 + 200×214.6 + 50×307.3 = 82,285
        self.check(450, 5, stage=3, base=7_300, usage=82_285, total=108_050, remaining=0)

    def test_case4_310kwh_summer(self):
        # 300×120 + 10×214.6 = 38,146
        self.check(310, 7, stage=2, base=1_600, usage=38_146, total=49_680, remaining=140)

    def test_case5_0kwh_other_season(self):
        # 사용량 0이어도 1단계 기본요금은 청구됨
        self.check(0, 5, stage=1, base=910, usage=0, total=1_020, remaining=200)


class Accuracy(unittest.TestCase):
    def test_matches_published_summer_450kwh_bill(self):
        # 언론 보도(2026-07) 한전 요금표 기준 하계 450kWh 예상 청구액 85,740원
        self.assertEqual(calc(450, 8)["total_estimated_fee"], 85_740)

    def test_without_surcharges(self):
        # 기본+전력량+VAT+기금만: 27,746 + 2,775 + 740 = 31,261 → 31,260
        self.assertEqual(calc(210, 5, include_surcharges=False)["total_estimated_fee"], 31_260)

    def test_super_user_summer(self):
        # 1,100kWh(8월): 300×120 + 150×214.6 + 550×307.3 + 100×736.2
        self.assertEqual(calc(1_100, 8)["usage_fee"], 36_000 + 32_190 + 169_015 + 73_620)

    def test_super_user_not_applied_in_spring(self):
        self.assertEqual(calc(1_100, 5)["usage_fee"], 24_000 + 42_920 + 215_110)  # 700×307.3


class Boundaries(unittest.TestCase):
    def test_other_season_edges(self):
        self.assertEqual(calc(200, 10)["stage"], 1)
        self.assertEqual(calc(201, 10)["stage"], 2)
        self.assertEqual(calc(400, 10)["stage"], 2)
        self.assertEqual(calc(401, 10)["stage"], 3)

    def test_summer_edges(self):
        self.assertEqual(calc(300, 7)["stage"], 1)
        self.assertEqual(calc(301, 7)["stage"], 2)
        self.assertEqual(calc(450, 8)["stage"], 2)
        self.assertEqual(calc(451, 8)["stage"], 3)

    def test_season_switch_june_september(self):
        self.assertEqual(calc(250, 6)["stage"], 2)
        self.assertEqual(calc(250, 7)["stage"], 1)
        self.assertEqual(calc(250, 9)["stage"], 2)

    def test_remaining_is_zero_at_stage_max(self):
        self.assertEqual(calc(200, 5)["remaining_kwh_to_next_stage"], 0)


class InvalidInput(unittest.TestCase):
    def test_negative_usage(self):
        with self.assertRaises(ValueError):
            calc(-1, 5)

    def test_bad_month(self):
        for m in (0, 13):
            with self.assertRaises(ValueError):
                calc(100, m)

    def test_non_integer_usage(self):
        with self.assertRaises(TypeError):
            calc(150.5, 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
