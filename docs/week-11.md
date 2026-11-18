# 11주차 활동지 / Week 11 Worksheet

**개발 착수 / Starting development**

- 작성일 / Date: 2026-11-17
- 참여자 / Present: 박현준, 손민석, 오지현, 이주현

---

## ① 착수 점검표 / Start checklist

수업 시작 후 10분 안에 확인합니다. 체크되지 않은 항목이 있으면 그것부터 해결하고 개발을 시작합니다.
*Check within the first 10 minutes. Fix any unchecked item before you start coding.*

- [v] 초기 파일이 저장소에 올라와 있다 / Initial files are in the repository
  - `frontend/`, `backend/`(logic·data·tests), `docs/`, `README.md`, `PROMPTS.md`, `.env.example`
- [v] 7주차 이슈가 GitHub에 등록되어 있고 담당자가 지정되어 있다 / Week 7 issues are on GitHub with owners
  - #1~#12 등록, 담당자 지정 (week-07.md 2절)
- [v] 팀원 모두 같은 환경에서 실행된다 / Everyone can run it in the same environment
  - Python `.venv` + `backend/requirements.txt`, API 키는 `backend/.env`(`.env.example` 참고)
  - 실행: `.venv\Scripts\python -m uvicorn main:app --app-dir backend --host 0.0.0.0 --port 8000`
  - 폰은 같은 Wi-Fi에서 `http://<PC IP>:8000`으로 접속
- [v] 브랜치 규칙을 정했다 / Branch rule agreed — `main` 직접 커밋 금지. 이슈·기능 단위로 브랜치를 만들고(`issue6-status-judge`, `T7-chain-cases`, `plan-b-taxi` 등) PR로 `main`에 머지한다. 커밋 메시지에는 이슈 번호를 붙인다(`#6 상태 판정 구현`). ODsay 캐시 추가는 기능 PR과 따로 올린다.

---

## ② 개발 일정 / Development schedule

- 선행 이슈가 끝나기 전에 뒤 이슈를 넣지 않습니다. / Never schedule an issue before the ones it depends on.
- 한 사람에게 몰리지 않았는지 확인합니다. / Check that no one is overloaded.

| 주차 Week | 수업 일정 Class | 끝낼 이슈 # Issues to close | 담당 Owner |
|---|---|---|---|
| 9주차 | 개발 착수 | ✅ #1 시간 변환, #4 막차 역산, #5 종착 열차 제외, #2 ODsay 경로 검색, #3 요일별 시간표, #7 역 검색, #8 입력 화면, #6 상태 판정 | 손민석(#1 #4 #5), 박현준(#2 #3), 오지현(#7 #8), 이주현(#6) |
| 10주차 | 막힘 진단 · 데모 시나리오 초안 | ✅ #9 구간 타임라인, #11 결과 화면(막차 놓침 화면, 자정 넘김 버그 수정), 실제 ODsay·시간표 연결, 시연 모드, 수도권 전체 역 추가 | 오지현(#9), 이주현(#11), 손민석(실데이터 연결) |
| 11주차 | **MVP 완료 · 중간 데모** | ✅ MVP 마일스톤(#1~#9, #11) 완료 → ✅ #10 팀 기능(같이 보기 방) + 추가 기능 4개(귀가 목표 시각 역산, 위치로 출발역 찾기, 플랜 B 택시비, 캘린더 알림) | 이주현(#10), 박현준,손민석,오지현,이주현(추가 기능) |
| 12주차 | 핵심 경로 테스트 | 핵심 경로(입력 → 계산 → 결과 / 막차 놓침 → 플랜 B / 방 만들기 → 들어가기) 테스트, 아이폰 사파리 확인, 택시비 정확도 보완 | 전원 (경로별로 나눠 맡음) |
| 13주차 | **배포 · 실행 패키지** | #12 실행 패키지(README만 보고 설치·실행·계산까지), HTTPS 배포 | 박현준(#12), 손민석(배포) |

> 일정이 맞지 않으면 기능을 줄입니다. 뺀 기능은 5주차 Won't 목록에 옮깁니다.
> *If it doesn't fit, cut scope and move the feature to your Week 5 Won't list.*
>
> - Won't로 옮김: 방장 권한(장소 바꾸기·멤버 내보내기), 방 나가기, 토큰을 잃었을 때 다시 연결
> - 배포 이후로 미룸(HTTPS 필요): 웹 푸시 알림, 그룹 단체 알림("다 같이 일어나기"), 카카오톡 공유 버튼
> - 5주차 Won't의 "푸시 알림 발송"은 **캘린더 알림(.ics)** 으로 대신 구현함 (화면이 꺼져 있어도 알림이 옴)

---

## ③ 이번 주 목표 이슈 / This week's issues

| # | 제목 Title | 담당 Owner | 완료 Done |
|---|---|---|---|
| MVP | 1인 막차 계산 MVP 마일스톤 (#1~#9, #11) 최종 점검 · 중간 데모 | 전원 | [v] |
| #10 | [Could] 팀 기능 — 같이 보기(그룹 방): 방 만들기·코드/링크로 들어가기·일어날 시각 순 정렬·나 먼저 갈게 (PR #29) | 이주현 / 손민석 | [v] |
| PR #23 | 집 도착 목표 시각 기준 역산 (비우면 막차 기준) | 이주현 | [v] |
| PR #24 | 위치로 출발역 찾기 · 막차 기준 출발역 추천 | 손민석 | [v] |
| PR #26 | 막차를 놓쳤을 때 중간까지 열차 + 택시비 안내 (플랜 B) | 오지현 | [v] |
| PR #28 | 일어날 시각 캘린더 알림 받기 | 박현준 | [v] |
| #12 | 실행 패키지 정리 (README 설치·실행 방법) | 박현준 | [ ] |

---

## ④ 오늘 진행한 것 / Progress today

- MVP 마일스톤(1인 막차 계산) 완료 확인: 출발역·도착역 입력 → 일어날 시각·예상 소요 시간·탑승 열차·구간 타임라인 표시, 상태 배지(OK/SOON/NOW/MISSED), 실패 시 [다시 시도]
- MVP 이후 추가 기능 5개 머지 완료 (PR #23, #24, #26, #28, #29) — 진행 내용은 `docs/기능추가.md`에 정리
- 백엔드 테스트 192개 (`backend/tests/`, 그룹 방 테스트 25개 포함)
- 남은 과제 정리: 웹 푸시·단체 알림(HTTPS 필요), 카카오톡 공유, 택시비 정확도, 아이폰 확인 → 12~13주차 일정에 반영
- [] 이번 활동에서 AI를 사용했다면 `PROMPTS.md`에 기록했습니다 / Logged any AI use in `PROMPTS.md`

---

> 수업 종료 시 커밋하세요 / Commit this at the end of class
> `git add docs/week-09.md && git commit -m "docs: 11주차 활동지 작성"`
