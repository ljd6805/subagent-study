# minishop — OpenCode subagent 실습용 샘플 프로젝트

작은 쇼핑몰 계산 모듈입니다. 실습을 위해 **일부러 버그 2개와 미완성 기능 1개**를 넣어 두었습니다.
정답은 실습 슬라이드 마지막 부록에 있으니, 먼저 subagent에게 찾게 해 보세요.

```
minishop/
  cart.py        장바구니 합계와 할인
  inventory.py   재고 확인과 예약
  report.py      주문 기록 요약 (TODO 있음)
data/orders.csv  주문 기록 예시
tests/           unittest 테스트 (지금은 일부 실패)
opencode.json    task 도구 허용 (전역 설정이 막아도 이 폴더에서는 subagent 호출 가능)
```

테스트 실행 (Python 3.10 이상, 설치할 패키지 없음):

```bash
# Linux · macOS
python3 -m unittest -v
```

```powershell
# Windows (PowerShell)
python -m unittest -v
```
