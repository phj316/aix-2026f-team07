A조:
메모 검색 기능 만들어줘. 제목이랑 본문에서 키워드로 찾을 수 있게.



B조:
[지시]
메모 검색 기능을 추가해줘. 제목과 본문에서 키워드로 검색된다.

[규약]
프로젝트 규약
이 문서는 코드를 작성할 때 지켜야 할 규칙입니다.

계층 분리
routes.js는 HTTP 요청과 응답만 다룹니다. SQL을 직접 쓰지 않습니다.
데이터베이스 접근은 service.js에만 둡니다.
응답 형식
모든 응답은 다음 두 형태 중 하나입니다.

{ "ok": true,  "data": ... }
{ "ok": false, "error": "ERROR_CODE" }
에러 코드는 대문자와 밑줄로 씁니다. (예: MEMO_NOT_FOUND)

명명 규칙
함수명은 동사로 시작합니다. list, get, create, update, remove
데이터베이스 컬럼은 스네이크 케이스를 씁니다. user_id, created_at
자바스크립트 변수는 카멜 케이스를 씁니다. userId, createdAt
입력 검증
사용자 입력은 반드시 검증합니다.
검증에 실패하면 400과 함께 { ok: false, error } 를 반환합니다.
권한
모든 조회와 수정은 본인 소유 데이터로 한정합니다.
모든 쿼리에 user_id 조건을 포함합니다.

[근거]
-- memo-seed 데이터베이스 스키마

CREATE TABLE users (
  id         INTEGER PRIMARY KEY,
  email      TEXT NOT NULL UNIQUE,
  name       TEXT NOT NULL,
  created_at TEXT NOT NULL
);

CREATE TABLE memos (
  id         INTEGER PRIMARY KEY,
  user_id    INTEGER NOT NULL,
  title      TEXT NOT NULL,
  body       TEXT NOT NULL,
  created_at TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE INDEX idx_memos_user ON memos(user_id);

const db = require('./db');

/**
 * 사용자의 메모 목록을 최신순으로 조회한다.
 */
function listMemos(userId) {
  return db.all(
    `SELECT id, title, created_at
       FROM memos
      WHERE user_id = ?
      ORDER BY created_at DESC`,
    [userId]
  );
}

/**
 * 메모 한 건을 조회한다. 본인 메모가 아니면 null을 반환한다.
 */
function getMemo(userId, memoId) {
  return db.get(
    `SELECT id, title, body, created_at
       FROM memos
      WHERE id = ? AND user_id = ?`,
    [memoId, userId]
  );
}

/**
 * 메모를 생성한다.
 */
function createMemo(userId, title, body) {
  return db.run(
    `INSERT INTO memos (user_id, title, body, created_at)
     VALUES (?, ?, ?, datetime('now'))`,
    [userId, title, body]
  );
}

module.exports = { listMemos, getMemo, createMemo };

const express = require('express');
const service = require('./service');

const router = express.Router();

// 메모 목록 조회
router.get('/memos', async (req, res) => {
  const memos = await service.listMemos(req.user.id);
  res.json({ ok: true, data: memos });
});

// 메모 단건 조회
router.get('/memos/:id', async (req, res) => {
  const memo = await service.getMemo(req.user.id, req.params.id);

  if (!memo) {
    return res.status(404).json({ ok: false, error: 'MEMO_NOT_FOUND' });
  }

  res.json({ ok: true, data: memo });
});

// 메모 생성
router.post('/memos', async (req, res) => {
  const { title, body } = req.body;

  if (!title || !body) {
    return res.status(400).json({ ok: false, error: 'TITLE_AND_BODY_REQUIRED' });
  }

  const result = await service.createMemo(req.user.id, title, body);
  res.status(201).json({ ok: true, data: { id: result.lastID } });
});

module.exports = router;

[종료조건]
- GET /memos/search?q=키워드 로 호출된다
- 제목 또는 본문에 키워드가 포함된 메모만 반환한다
- 본인 메모만 반환한다
- q가 비어 있으면 400과 { ok: false, error } 를 반환한다

# 3주차
---
-3주차 (1)  
무엇을 하려고 썼는가: 활동지 1절 양식([사용자]는 [상황]에서 [페인포인트] 때문에 [손해]를 본다)에 맞춘 문제 후보 A의 한 문장 정의를 도출하기 위해 사용함.

넣은 프롬프트 원문 그대로: "현재 대학생 자취생을 위한 ai기반 전기세,수도세,난방비 절약 가이드 ai 만들려한다 대강 계량기나 고지서 사진을 찍으면 그것을 통한 분석 및 현재 상황 제시와 누진세 비율 및 공지 등을 통해 최종적으로 자취생들의 공과금 절약 수행 및 더 나아가 에너지 절약관점을 통한 사회적 효과를 달성한다"

나온 것 중 쓴 것 / 버린 것: [쓴 것] 자취생이 공과금 구조를 몰라 요금 폭탄을 맞고 금전적 손해를 본다는 문제 정의 / [버린 것] AI 기능 및 에너지 절약의 사회적 가치 달성 문구

버렸다면 왜 버렸는가: 활동지 가이드라인상 기술/해결책(AI, 서비스)을 빼고 오직 사용자의 '문제와 직접적 손해'만 적어야 했기 때문.  

# 4주차
---  

-4주차 (1) 무엇을 하려고 썼는가: 4주차 활동지 3번의 Acceptance Criteria 부분을 채우기 위해 사용. 
넣은 프롬프트 원문 그대로: (피피티와 활동지 내용 첨부) 피피티 참고해서 두 번째 사진의 Acceptance Criteria 밑 부분 알려 줘 구체적으로 명시되는 내용이 포함되게. 
나온 것 중 쓴 것 / 버린 것: [쓴 것] 구체적인 판정 방법이 포함된 모든 내용을 사용 / [버린 것] 판정 방법이 구체적이지 않은 1차 답변을 버린 후 2차 답변을 사용함.  


-4주차 (2) 무엇을 하려고 썼는가: 4주차 활동지 3번의 Acceptance Criteria 부분 중  어쩔 수 없이 못 쓰는 사람들을 대상으로 한 실패 기준과 관련한 내용을 채우기 위해 사용. 
넣은 프롬프트 원문 그대로: 계량기가 건물 전체로 묶여 있어 측정이 아예 불가한 고시원 거주자(개별 사용량 확인 불가) 얘를 실패기준으로 정하고 하나 더 적어 줘. 
나온 것 중 쓴 것 / 버린 것: [쓴 것] 버리는 것 없이 나온 내용을 모두 사용 / [버린 것] 없음. 
버렸다면 왜 버렸는가: 없음
