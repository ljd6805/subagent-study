import unittest

from minishop.cart import Cart


class CartTest(unittest.TestCase):
    def test_subtotal(self):
        cart = Cart()
        cart.add("keyboard", 45000)
        cart.add("mouse", 15000, qty=2)
        self.assertEqual(cart.subtotal(), 75000)

    def test_total_with_discount(self):
        cart = Cart()
        cart.add("monitor", 200000)
        self.assertEqual(cart.total(discount_percent=10), 180000)


if __name__ == "__main__":
    unittest.main()
