# Week 07 팀 활동지 / Team Activity

| 팀명 / Team | 작성일 / Date | 참여자 / Members |
|---|---|---|
|xia |2026-10-26 |박현준,손민석,오지현,이주현 |

## 1. 아키텍처 다이어그램 / Architecture Diagram

손그림 사진을 올리고 링크하십시오 / Upload a photo and link it.

![architecture](img/week-07-arch.png)

| 계층 / Layer | 모듈·파일 / Modules | 의존하지 않는 것 / Does not depend on |
|---|---|---|
| 표현 / Presentation | 입력 화면(출발 위치·도착역·도보/여유 시간 설정), 결과 타임라인 화면, 그룹 공유 화면 | ODsay API 직접 호출, 시간표 데이터 형식, 역산 계산 내부 로직 |
| 로직 / Logic | `time_utils`(분↔HH:MM 변환), `reverse_calc`(막차 역산), `train_filter`(종착 열차 제외), `status_judge`(OK/SOON/NOW/MISSED 판정), `group_sort`(일어날 시각 정렬) | UI 프레임워크, ODsay 응답 JSON 구조, 저장소 종류(DB 등) |
| 데이터 / Data | `odsay_client`(경로 검색 API 연동), `timetable_repo`(요일별 시간표 조회), `group_repo`(술자리 그룹·사용자 정보 저장) | UI 화면 구성, 역산 계산 규칙, 상태 판정 기준 |

## 2. 이슈 / Issues

> 이슈 = **앞으로 할 일** / An issue is work to be done.
> 개발할 때 커밋에 이슈 번호를 붙이고(`#3 알레르기 필터 추가`), 완료 조건을 만족하면 이슈를 닫습니다.
> Add the issue number to commits, and close the issue when its criteria are met.

| # | 제목 / Title | 라벨 / Label | 담당 / Assignee | 완료 조건 / Acceptance Criteria |
|---|---|---|---|---|
| 예시 #3 | 알레르기 필터 | backend | 홍길동 | '땅콩'을 선택하면 땅콩이 들어간 메뉴가 추천 결과에서 빠진다 |
| #1 | 시간 변환 유틸 | backend | 손민석 | `23:12`는 1392분, 다음 날 `00:30`은 1470분으로 변환되고, 1470분은 화면에 `00:30`으로 표시된다 |
| #2 | ODsay 지하철 경로 검색 연동 | data | 박현준 | 출발역과 도착역을 넣으면 환승역과 구간(노선·출발역·도착역)이 담긴 경로 목록이 반환된다 |
| #3 | 요일별 시간표 조회 | data | 박현준 | `WEEKDAY`, `SATURDAY`, `HOLIDAY`를 넘기면 각각 다른 시간표가 반환된다 |
| #4 | 막차 역산 계산 | backend | 이주현 | 막차 출발 23:08, 도보 7분, 여유 5분을 넣으면 일어날 시각이 22:56(1376분)으로 계산된다 |
| #5 | 종착 열차 제외 | backend | 이주현 | 목적지(대화역)에 도달하지 못하는 L3 23:45 구파발행이 후보에서 빠지고 `excludedTrains`에 제외 사유가 기록된다 |
| #6 | 상태 판정 | backend | 손민석 | 현재 시각 기준으로 일어날 시각이 지났으면 `MISSED`, 같으면 `NOW`, 임박하면 `SOON`, 그 외는 `OK`로 판정된다 |
| #7 | 입력 화면 | frontend | 오지현 | 출발 위치, 도착역을 입력하고 도보·여유 시간을 바꿀 수 있으며(기본 7분·5분), 입력 후 계산 버튼으로 결과 화면으로 넘어간다 |
| #8 | 결과 타임라인 화면 | frontend | 오지현 | 일어날 시각과 구간별 출발·도착 시각, 환승 정보가 한 화면에 표시된다 |
| #9 | 그룹 공유 | backend | 손민석 | 같은 술자리 사용자 여러 명의 일어날 시각이 오름차순으로 정렬되어 모두에게 보인다 |
| #10 | 실행 패키지 정리 | docs | 박현준 | README만 보고 처음 보는 사람이 앱을 설치하고 실행해 한 번 계산까지 해볼 수 있다 |

## 3. 마일스톤 / Milestones

| 마일스톤 / Milestone | 마감 / Due | 포함 이슈 / Issues |
|---|---|---|
| MVP 완료 | 11주차 | #1, #2, #3, #4, #5, #6, #7, #8 |
| 실행 패키지 | 13주차 | #9, #10 |

> AI를 사용했다면 `PROMPTS.md`에 기록 / Log any AI use in `PROMPTS.md`
