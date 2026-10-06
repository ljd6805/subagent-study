# minishop — Claude Code subagent 실습용 샘플 프로젝트

작은 쇼핑몰 계산 모듈입니다. 실습을 위해 **일부러 버그 2개와 미완성 기능 1개**를 넣어 두었습니다.
정답은 실습 슬라이드 마지막 부록에 있으니, 먼저 subagent에게 찾게 해 보세요.

```
minishop/
  cart.py        장바구니 합계와 할인
  inventory.py   재고 확인과 예약
  report.py      주문 기록 요약 (TODO 있음)
data/orders.csv  주문 기록 예시
tests/           unittest 테스트 (지금은 일부 실패)
```

실습 중에 `.claude/settings.json`, `.claude/agents/*.md`, `agents.json`을 이 폴더에 직접 만듭니다.
처음에는 없는 것이 정상입니다.

## 실습 진행

1. 실습 슬라이드를 엽니다: https://ljd6805.github.io/subagent-study/labs/02-claude-code/
2. 이 폴더(`labs/02-claude-code/minishop`)로 이동한 뒤 `claude`를 실행합니다.
3. 슬라이드의 LAB 0부터 순서대로 따라 합니다.

```bash
# Linux · macOS
cd labs/02-claude-code/minishop
claude
```

```powershell
# Windows (PowerShell 7)
cd labs\02-claude-code\minishop
claude
```

## 테스트 실행

Python 3.10 이상, 설치할 패키지 없음:

```bash
# Linux · macOS
python3 -m unittest -v
```

```powershell
# Windows (PowerShell)
python -m unittest -v
```
