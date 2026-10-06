import unittest

from minishop.inventory import Inventory


class InventoryTest(unittest.TestCase):
    def test_reserve_some(self):
        inv = Inventory({"mouse": 5})
        self.assertTrue(inv.reserve("mouse", 2))
        self.assertEqual(inv.available("mouse"), 3)

    def test_reserve_all_remaining(self):
        inv = Inventory({"mouse": 5})
        self.assertTrue(inv.reserve("mouse", 5))
        self.assertEqual(inv.available("mouse"), 0)


if __name__ == "__main__":
    unittest.main()
