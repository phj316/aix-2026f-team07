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
| AC-1 | 정상 Normal | WHEN 사용자가 현재 계량기 수치를 입력하면 THE 공과금 예측 시스템은 SHALL 당월 예상 요금과 현재 누진세 단계를 화면에 표시한다  | 계량기 수치(예: 180kWh) 입력 후 확인 버튼을 눌렀을 때, 당월 예상 요금과 누진 1단계 상태가 화면에 출력되는지 확인 |
| AC-2 | 정상 Normal | WHEN 사용자의 전력 사용량이 다음 누진 구간의 80%에 도달하면 THE 공과금 예측 시스템은 SHALL 누진세 진입 예방을 위한 맞춤형 절약 행동 지침 알림을 발송한다  | 전력 사용량을 다음 누진 구간 도달 80% 수치로 설정했을 때, Push 알림 및 절약 행동 가이드 팝업이 노출되는지 확인 |
| AC-3 | 실패 Failure | IF 사용자가 지난달 수치보다 작은 비정상적인 계량기 수치를 입력하면 THEN THE 공과금 예측 시스템은 SHALL "올바른 계량기 수치를 입력해 주세요"라는 에러 메시지를 표시한다 | 계량기 입력란에 지난달 수치(예: 200kWh)보다 작은 수치(예: 150kWh)를 입력하고 확인을 눌렀을 때 오류 메시지 팝업이 뜨는지 확인 |

> 확인할 동작이 더 있으면 AC-4부터 행을 추가해 쓰십시오.
> If there are more behaviors to check, add rows from AC-4.

- [ ] 이번 활동에서 AI를 사용했다면 `PROMPTS.md`에 기록했습니다 / Logged any AI use in `PROMPTS.md`

---

> 수업 종료 시 커밋하세요 / Commit this at the end of class
> `git add docs/week-04.md && git commit -m "docs: 4주차 활동지 작성"`
