# 4주차 활동지 / Week 4 Worksheet

**주제 선택과 요구 명세 / Choosing a problem & writing the spec**

- 작성일 / Date: 26.9.23
- 참여자 / Present: 박현준, 손민석, 이주현, 오지현

---

## ① 주제 선택 / Choosing one problem

| 항목 Item | 내용 |
|---|---|
| 선택한 주제 Chosen | 자취생의 요금 폭탄을 막는 공과금 예측 및 누진세 절약 서비스 |
| 선택 근거 Why | 자취하는 대학생들이 신경쓰지 못하지만 신경쓸 경우 경제 부담을 줄여주기 좋다고 생각함. |

## ② 성공 기준 가져오기 / Success criteria from Week 3

| 3주차 성공 기준 원문 Original (Week 3) | 모호한 표현 Vague words |
|---|---|
| | |
| 계량기,고지서 확인 시 당월 예상 요금과 누진세 진입전 절약 행동 지침 파악힘 | 누진세 진입 전, 절약 행동 지침, 파악 |

## ③ Acceptance Criteria

최소 정상 경로 2개 + 실패 경로 1개. **판정 방법** 칸이 비면 아직 명세가 아닙니다.
At least two normal paths + one failure path. If "How to check" is empty, it is not yet a spec.

| # | 경로 Path | EARS 문장 Sentence | 판정 방법 How to check |
|---|---|---|---|
|  |  |  | |
| AC-1 | 정상 Normal | WHEN 사용자가 계량기 수치를 수동 입력하고 [예측하기] 버튼을 누르면 THE 공과금 예측 시스템은 SHALL 3초 이내에 당월 예상 금액(원)과 현재 누진 구간(1~3단계)을 화면에 표시한다.  | 1. 계량기 수치(예: 210kWh) 입력 후 버튼 클릭. 2. 3초 이내에 예상 요금과 '누진 2단계' 문구가 정확히 화면에 표시되는지 확인. |
| AC-2 | 정상 Normal | WHEN 사용자의 전력 사용량이 다음 누진 구간 기준(예: 200kWh)의 90%에 도달하면 THE 공과금 예측 시스템은 SHALL "누진세 진입 전" 알림과 함께 예상 절감액이 포함된 절약 행동 지침 3가지를 푸시 알림으로 발송한다.  | 1. 테스트 계정의 전력 사용량을 180kWh(90%)로 변경. 2. 모바일 앱 푸시 알림이 즉시 수신되는지 확인. 3. 알림 클릭 시 맞춤 절약 지침 3가지(예: 에어컨 1℃ 높이기 등)가 노출되는지 확인. |
| AC-3 | 실패 Failure | IF 사용자가 전월 계량기 수치보다 작은 값이나 음수를 입력하면 THEN THE 공과금 예측 시스템은 SHALL "전월 수치보다 큰 수치를 입력해 주세요"라는 경고 문구를 입력창 하단에 붉은색으로 표시한다. | 1. 전월 수치가 200kWh인 상태에서 150kWh 입력 후 확인 클릭. 2. 계산이 진행되지 않고 붉은색 에러 메시지가 즉시 노출되는지 확인. |

> 확인할 동작이 더 있으면 AC-4부터 행을 추가해 쓰십시오.
> If there are more behaviors to check, add rows from AC-4.

- [ ] 이번 활동에서 AI를 사용했다면 `PROMPTS.md`에 기록했습니다 / Logged any AI use in `PROMPTS.md`

---

> 수업 종료 시 커밋하세요 / Commit this at the end of class
> `git add docs/week-04.md && git commit -m "docs: 4주차 활동지 작성"`
