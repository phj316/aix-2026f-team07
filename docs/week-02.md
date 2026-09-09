# 2주차 활동지 / Week 2 Worksheet

**AI 협업 방식 비교 / Comparing two ways of working with AI**

- 작성일 / Date: 
- 참여자 / Present: 
- 결과보고서 / Report chapter: 6장 AI 활용과 판단
- 최종 반영 / Feeds into: PROMPTS.md 첫 항목

---

## 구현할 작은 기능 / Small feature

## 메모 검색 기능 추가하기

## 사용한 도구 / Tool used

## Gemini, Claude

## 방식 A — 통째로 요청 / One big request

## 프롬프트: 메모 검색 기능 만들어줘. 제목이랑 본문에서 키워드로 찾을 수 있게.
## 결과
// 메모 데이터 예시
const notes = [
  { id: 1, title: "장보기 목록", content: "우유, 계란, 사과 사기" },
  { id: 2, title: "회의록", content: "프로젝트 일정 논의 및 장보기 앱 개발" },
  { id: 3, title: "운동 루틴", content: "스쿼트 3세트, 런닝머신 30분" }
];

/**
 * 제목이나 본문에 키워드가 포함된 메모를 검색합니다.
 * @param {Array} notesList - 전체 메모 배열
 * @param {string} keyword - 검색할 단어
 * @returns {Array} 검색 결과 메모 배열
 */
function searchNotes(notesList, keyword) {
  // 공백 제거 및 대소문자 구분을 없애기 위해 소문자로 변환
  const cleanKeyword = keyword.trim().toLowerCase();
  
  if (!cleanKeyword) return notesList;

  return notesList.filter(note => {
    const titleMatch = note.title.toLowerCase().includes(cleanKeyword);
    const contentMatch = note.content.toLowerCase().includes(cleanKeyword);
    
    return titleMatch || contentMatch;
  });
}

// 사용 예시
console.log(searchNotes(notes, "장보기")); 
// 결과: id 1, id 2 메모 반환
## 문제점: 로그인 개념이 없어 전체 메모에서 검색되어 남의 메모까지 다 찾아짐

## 방식 B — 4단계 분해 / spec → context → unit → verify



## 두 방식의 차이 / Difference



## 내가 개입해야 했던 지점 / Where you intervened



---

> 수업 종료 시 커밋하세요 / Commit this at the end of class
> `git add docs/week-02.md && git commit -m "docs: 2주차 활동지 작성"`
