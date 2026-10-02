# Subagent 이론 슬라이드 — 목차 초안 v0

> 개인 공부용. 기존 덱(SKILL 심화 ⑤ "쪼개서 위임", OpenCode Orchestrator→Worker 가이드, Hook→Harness)과 이어지도록 설계.
> 슬라이드 제목은 기존 덱처럼 "주장형 한 문장"으로 씀.

## 오프닝 (2장)
1. **표지** — "한 에이전트에서, 위임하는 에이전트로"
2. **왜 지금 subagent인가** — 컨텍스트는 예산이다(SKILL 심화 복습) → 줄이는 것만으로 안 되는 일이 있다

## Part 1. 공통 개론 (OpenCode · Codex · Claude Code 공통) — 약 16장
3. Subagent의 정의 — "별도 컨텍스트에서 위임받은 일을 끝내고 결과만 돌려주는 에이전트 인스턴스"
4. Tool · Skill · MCP · Subagent는 질문이 다르다 — 무엇으로 / 어떻게 / 어디에 연결 / **누가**
5. 동작 메커니즘 — 부모가 위임 도구(task/spawn) 호출 → 새 컨텍스트 + 전용 시스템 프롬프트 + 제한된 도구 → 자체 loop → 최종 메시지만 반환
6. 컨텍스트 격리 — 들어가는 것(브리프) · 나오는 것(결과) · **안 넘어가는 것**(부모 대화 기록, 중간 추론)
7. 정의 파일의 공통 골격 — name · description · prompt · tools/permission · model
8. description은 라우터다 — 자동 위임 vs 명시 호출(@mention, 직접 지시)
9. 권한은 좁게 — 읽기 전용 탐색가, 쓰기 가능한 작업자, 실행 금지 리뷰어
10. 모델은 역할에 맞게 — 탐색은 작고 빠른 모델, 판단은 큰 모델
11. 패턴 ① 탐색/조사 분리 (Explore형)
12. 패턴 ② 병렬 fan-out → 회수(gather)
13. 패턴 ③ 전문가 리뷰어 / 독립 검증자 (같은 맥락에 오염되지 않은 눈)
14. 패턴 ④ Orchestrator–Worker (기존 OpenCode 가이드와 연결)
15. 비용 — 토큰 배수, 지연, 그리고 "전달 손실"(요약이 정보를 깎는다)
16. 브리프 쓰는 법 — 목표 · 범위 · 완료 조건 · 반환 형식(계약)
17. 반환 계약과 검증 — 결과는 파일로, 판정은 코드로 (Harness 덱과 연결)
18. 언제 쓰지 말아야 하나 — 안티패턴(과분할, 공유 상태 동시 수정, 재귀 위임)

## Part 2. 도구별 특화 기능 — 약 12장
### OpenCode (4장)
19. primary / subagent / all 모드와 내장 agent(build·plan·general·explore)
20. 정의 위치: `opencode.json` 의 `agent` vs `.opencode/agent/*.md`
21. `permission.task` 로 위임 대상 제한, `@agent` 호출, child session 탐색
22. headless(`run`/`serve`)에서 subagent 다루기 — 기존 Headless Lab과 연결

### Codex (3~4장) ※ 기능 변화가 빨라 제작 시 최신 공식 문서로 재검증
23. Codex의 multi-agent / subagent 지원 현황과 활성화 방식
24. 역할(role) 정의와 `config.toml` 프로필·모델 라우팅 (기존 codex-model-routing 작업과 연결)
25. `codex exec` · MCP 서버 모드로 "Codex를 subagent로 쓰기"

### Claude Code (4~5장)
26. `.claude/agents/*.md` 프론트매터(tools · model · permissionMode · skills · hooks)와 `/agents`
27. 내장 subagent(Explore · Plan · general-purpose)와 자동 위임
28. 백그라운드 실행 · resume · worktree 격리
29. Subagent용 Hook(SubagentStart/Stop)과 Agent Teams(실험) — "subagent 다음 단계"

### 비교 (1~2장)
30. 3-way 비교표 — 정의 위치 · 호출 · 권한 · 모델 지정 · 병렬 · 중첩 · headless

## 마무리 (2장 + 부록)
31. 한 장 요약 — "언제 위임하고, 무엇을 넘기고, 무엇을 받는가"
32. 다음: 실습편 예고
- 부록: 용어집, 공식 문서 링크 모음
