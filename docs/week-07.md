# Week 07 팀 활동지 / Team Activity

| 팀명 / Team | 작성일 / Date | 참여자 / Members |
|---|---|---|
|xia |2026-10-26 |박현준,손민석,오지현,이주현 |

## 1. 아키텍처 다이어그램 / Architecture Diagram

손그림 사진을 올리고 링크하십시오 / Upload a photo and link it.

![architecture](img/week-07-arch.png)

| 계층 / Layer | 모듈·파일 / Modules | 의존하지 않는 것 / Does not depend on |
|---|---|---|
| 표현 / Presentation | 팀 만들기 화면(팀명·출발역·요일 구분), 팀원 등록 화면(이름·도착역·도보/여유 시간 설정), 팀 결과 화면(팀원별 일어날 시각·예상 소요 시간, 구간별 타임라인) | ODsay API 직접 호출, 시간표·역 목록 데이터 형식, 역산 계산 내부 로직 |
| 로직 / Logic | `time_utils`(분↔HH:MM 변환), `reverse_calc`(막차 역산·예상 소요 시간 계산), `train_filter`(종착 열차 제외), `status_judge`(OK/SOON/NOW/MISSED 판정), `team_sort`(팀원 일어날 시각 정렬) | UI 프레임워크, ODsay 응답 JSON 구조, 저장소 종류(DB 등) |
| 데이터 / Data | `station_repo`(지하철 역 목록·역 검색), `odsay_client`(경로 검색 API 연동), `timetable_repo`(요일별 시간표 조회), `team_repo`(팀명·출발역·팀원 정보 저장) | UI 화면 구성, 역산 계산 규칙, 상태 판정 기준 |

## 2. 이슈 / Issues

> 이슈 = **앞으로 할 일** / An issue is work to be done.
> 개발할 때 커밋에 이슈 번호를 붙이고(`#3 알레르기 필터 추가`), 완료 조건을 만족하면 이슈를 닫습니다.
> Add the issue number to commits, and close the issue when its criteria are met.

| # | 제목 / Title | 라벨 / Label | 담당 / Assignee | 완료 조건 / Acceptance Criteria |
|---|---|---|---|---|
| #1 | 시간 변환 유틸 | backend | 손민석 | `23:12`는 1392분, 다음 날 `00:30`은 1470분으로 변환되고, 1470분은 화면에 `00:30`으로 표시된다 |
| #2 | ODsay 지하철 경로 검색 연동 | data | 박현준 | 출발역과 도착역을 넣으면 환승역과 구간(노선·출발역·도착역·소요 시간)이 담긴 경로 목록이 반환되고, 5초 안에 응답이 없거나 호출이 실패하면 실패 결과가 반환된다 |
| #3 | 요일별 시간표 조회 | data | 박현준 | `WEEKDAY`, `SATURDAY`, `HOLIDAY`를 넘기면 각각 다른 시간표가 반환된다 |
| #4 | 막차 역산·예상 소요 시간 계산 | backend | 손민석 | 막차 출발 23:08, 도보 7분, 여유 5분을 넣으면 일어날 시각이 22:56(1376분)으로 계산되고, 승차·환승 시간 합이 50분인 경로면 예상 소요 시간(도보+여유+승차+환승)이 62분으로 계산된다 |
| #5 | 종착 열차 제외 | backend | 손민석 | 목적지(대화역)에 도달하지 못하는 L3 23:45 구파발행이 후보에서 빠지고 `excludedTrains`에 제외 사유("목적지 미도달")가 기록된다 |
| #6 | 상태 판정 | backend | 이주현 | 현재 시각 기준으로 일어날 시각이 지났으면 `MISSED`, 같으면 `NOW`, 10분 이내로 남았으면 `SOON`, 그 외는 `OK`로 판정된다 |
| #7 | 지하철 역 검색 | data | 오지현 | "홍대", "대화"처럼 역 이름 일부를 넣으면 수도권 역 목록에서 후보(역명·노선)가 반환되고, 목록에 없는 역 이름은 선택되지 않는다 |
| #8 | 팀 만들기 화면 | frontend | 오지현 | 메인화면에서 팀명, 술자리와 가장 가까운 지하철역(출발역), 요일 구분(오늘 날짜로 자동 선택·수정 가능)을 입력할 수 있고, 팀명이나 출발역이 비어 있으면 [다음] 버튼이 비활성화된다 |
| #9 | 팀원 등록 화면 | frontend | 오지현 | 팀원마다 이름과 집(또는 가야 할 곳)과 가장 가까운 지하철역(도착역)을 추가·삭제할 수 있고, 도보·여유 시간은 기본 7분·5분으로 채워져 수정할 수 있으며, 팀원이 0명이면 [계산하기] 버튼이 비활성화된다 |
| #10 | 팀 저장·정렬 | backend | 이주현 | 한 팀에 팀원 여러 명의 계산 결과가 저장되고 일어날 시각 오름차순으로 반환된다 (22:56, 22:30, 23:10 → 22:30, 22:56, 23:10). 한 명의 값을 바꾸면 순서가 다시 정렬된다 |
| #11 | 팀 결과 화면 | frontend | 이주현 | [계산하기] 후 3초 이내에 팀원별 일어날 시각, 예상 소요 시간, 탑승 열차가 빠른 순으로 표시되고, 팀원을 누르면 구간별 출발·도착 시각과 환승 정보가 보인다. `MISSED`이면 "오늘 막차를 놓쳤습니다", 경로 조회 실패면 "경로를 불러오지 못했습니다. 다시 시도해 주세요"와 [다시 시도] 버튼이 시각 대신 표시된다 |
| #12 | 실행 패키지 정리 | docs | 박현준 | README만 보고 처음 보는 사람이 앱을 설치하고 실행해 팀을 만들고 한 번 계산까지 해볼 수 있다 |

## 3. 마일스톤 / Milestones

| 마일스톤 / Milestone | 마감 / Due | 포함 이슈 / Issues |
|---|---|---|
| MVP 완료 | 11주차 | #1, #2, #3, #4, #5, #6, #7, #8, #9, #10, #11 |
| 실행 패키지 | 13주차 | #12 |

## 4. 레포 구조 / Repository Structure

> 아키텍처의 세 계층이 폴더로 그대로 나뉘도록 구성했습니다. 화면은 `frontend/`, 로직·데이터는 `backend/logic/`, `backend/data/`에 두고, 각 파일 옆 번호는 담당 이슈입니다.

```
xia-makcha/
├── README.md                    # 설치·실행 방법, 시연 모드 사용법 (#12)
├── PROMPTS.md                   # AI 사용 기록
├── .env.example                 # ODSAY_API_KEY= (실제 키는 .env, 커밋 금지)
├── .gitignore                   # .env, node_modules/, __pycache__/
│
├── docs/                        # 주차별 활동지
│   ├── week-03-candidate-B.md
│   ├── week-04.md
│   ├── week-05.md
│   ├── week-07.md
│   └── img/
│       └── week-07-arch.png
│
├── frontend/                    # 표현 계층
│   ├── index.html
│   └── src/
│       ├── api.js               # backend 계산 API 호출 (ODsay를 직접 부르지 않음)
│       ├── pages/
│       │   ├── TeamCreatePage       # 팀 만들기 화면 (#8)
│       │   ├── MemberRegisterPage   # 팀원 등록 화면 (#9)
│       │   └── TeamResultPage       # 팀 결과 화면 (#11)
│       └── components/
│           ├── StationSearch        # 역 검색 입력칸 (#7, #8, #9 공용)
│           ├── MemberRow            # 팀원 한 줄: 일어날 시각·예상 소요·상태
│           └── RouteTimeline        # 구간별 출발·도착·환승 (#11)
│
└── backend/
    ├── main.py                  # 계산 API 라우트, 시연 모드(now 지정) 처리
    ├── requirements.txt
    ├── logic/                   # 로직 계층: UI·ODsay 응답 형식을 모름
    │   ├── time_utils.py        # #1
    │   ├── reverse_calc.py      # #4
    │   ├── train_filter.py      # #5
    │   ├── status_judge.py      # #6
    │   └── team_sort.py         # #10
    ├── data/                    # 데이터 계층: 계산 규칙을 모름
    │   ├── station_repo.py      # #7
    │   ├── odsay_client.py      # #2
    │   ├── timetable_repo.py    # #3
    │   └── team_repo.py         # #10
    ├── resources/
    │   ├── stations.json        # 수도권 역 목록 (역명·노선·ODsay 역 ID)
    │   └── odsay_cache/         # 개발·시연용으로 저장해 둔 API 응답
    └── tests/
        ├── cases.json           # 정답 케이스 (홍대입구→대화 등, 직접 역산한 값)
        ├── test_time_utils.py
        ├── test_reverse_calc.py
        ├── test_train_filter.py
        ├── test_status_judge.py
        └── test_team_sort.py
```

- **의존 규칙:** `frontend` → `backend/main.py` → `logic` → `data` 방향으로만 부른다. `logic`은 `data`가 넘겨준 값(열차 출발 시각, 구간 목록)만 받아서, ODsay 응답 JSON이 바뀌어도 `odsay_client.py`만 고치면 된다.
- **테스트:** `logic/`의 함수는 API 없이 `tests/cases.json` 값만으로 테스트한다. 이슈의 완료 조건(예: 23:08 출발 → 22:56)을 그대로 테스트 케이스로 옮긴다.

> AI를 사용했다면 `PROMPTS.md`에 기록 / Log any AI use in `PROMPTS.md`
