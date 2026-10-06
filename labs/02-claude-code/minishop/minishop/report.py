"""주문 기록(CSV)을 읽어 요약한다."""

import csv
from collections import defaultdict


def load_orders(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def sales_by_product(orders):
    """상품별 판매 수량 합계."""
    totals = defaultdict(int)
    for row in orders:
        totals[row["product"]] += int(row["qty"])
    return dict(totals)


def top_products(orders, n=3):
    # TODO: 판매 수량이 많은 순서로 상위 n개 (상품, 수량) 목록을 돌려준다.
    raise NotImplementedError
