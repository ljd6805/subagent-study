# subagent-study

OpenCode · Codex · Claude Code의 **subagent**를 공통 원리로 이해하고 직접 돌려 보는 개인 스터디 저장소입니다. (세미나용 아님)

- 허브 페이지: https://ljd6805.github.io/subagent-study/
- 이론 슬라이드: https://ljd6805.github.io/subagent-study/slides/theory/
- 이론 슬라이드 2 (Agent Teams 소개): https://ljd6805.github.io/subagent-study/slides/theory-2/
- OpenCode 실습 슬라이드: https://ljd6805.github.io/subagent-study/labs/01-opencode/
- Claude Code 실습 슬라이드: https://ljd6805.github.io/subagent-study/labs/02-claude-code/
- Codex 실습 슬라이드: https://ljd6805.github.io/subagent-study/labs/03-codex/

## 구성

| 경로 | 내용 | 상태 |
|---|---|---|
| [`index.html`](index.html) | 허브 페이지 — 슬라이드와 실습을 한곳에서 연결 | |
| [`slides/theory/index.html`](slides/theory/index.html) | 이론 슬라이드 61장, 부록(용어집, 부록 A 선언 방법 상세) 포함 (단일 HTML, 16:9 고정 캔버스, ←/→ 이동, `O` 목차, `#번호`로 바로 가기) | v2 |
| [`slides/theory-2/index.html`](slides/theory-2/index.html) | 이론 슬라이드 2편 24장: Agent Teams 소개 (왜 필요한가, 구조, worktree 격리, 언제 쓰나) | v2 |
| [`docs/outline-draft.md`](docs/outline-draft.md) | 이론 덱 목차 초안 | |
| [`docs/research/`](docs/research/) | 도구별 조사 노트 (OpenCode · Codex · Claude Code) | |
| [`labs/01-opencode/`](labs/01-opencode/) | OpenCode 실습 슬라이드 40장 (LAB 0–6)과 샘플 프로젝트 `minishop` | v1 |
| [`labs/02-claude-code/`](labs/02-claude-code/) | Claude Code 실습 슬라이드 40장 (LAB 0–6)과 샘플 프로젝트 `minishop` | v1 |
| [`labs/03-codex/`](labs/03-codex/) | Codex 실습 슬라이드 40장 (LAB 0–6)과 샘플 프로젝트 `minishop` | v1 |
| [`labs/`](labs/) | 도구별 실습 목록 | |

## 자료 추가 규칙

- 새 슬라이드 덱은 `slides/<이름>/index.html`에 두고 허브의 "슬라이드" 카드에 추가한다.
- 실습은 `labs/<번호>-<주제>/`에 두고 허브의 "실습" 목록 항목을 링크로 바꾼다.
- 허브와 README 표를 같이 갱신한다.
