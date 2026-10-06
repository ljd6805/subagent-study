"""재고: 남은 수량을 확인하고 주문만큼 예약한다."""


class Inventory:
    def __init__(self, stock):
        self.stock = dict(stock)  # 상품 이름 -> 남은 수량

    def available(self, name):
        return self.stock.get(name, 0)

    def reserve(self, name, qty):
        """재고가 충분하면 qty 만큼 빼고 True, 부족하면 False."""
        if self.available(name) > qty:
            self.stock[name] -= qty
            return True
        return False
