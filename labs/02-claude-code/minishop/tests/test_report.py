import unittest
from pathlib import Path

from minishop.report import load_orders, sales_by_product

DATA = Path(__file__).resolve().parent.parent / "data" / "orders.csv"


class ReportTest(unittest.TestCase):
    def test_sales_by_product(self):
        totals = sales_by_product(load_orders(DATA))
        self.assertEqual(totals["mouse"], 10)
        self.assertEqual(totals["keyboard"], 3)


if __name__ == "__main__":
    unittest.main()
