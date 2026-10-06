"""장바구니: 상품을 담고 합계를 계산한다."""


class Cart:
    def __init__(self):
        self.items = {}  # 상품 이름 -> (단가, 수량)

    def add(self, name, price, qty=1):
        if qty <= 0:
            raise ValueError("수량은 1 이상이어야 합니다")
        _, old_qty = self.items.get(name, (price, 0))
        self.items[name] = (price, old_qty + qty)

    def remove(self, name):
        self.items.pop(name, None)

    def subtotal(self):
        return sum(price * qty for price, qty in self.items.values())

    def total(self, discount_percent=0):
        """할인율(%)을 적용한 최종 금액. 예: 10 이면 10% 할인."""
        subtotal = self.subtotal()
        return subtotal - discount_percent
