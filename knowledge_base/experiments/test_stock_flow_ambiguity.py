import unittest
from fractions import Fraction as F
from stock_flow_ambiguity import equilibrium, balance


class StockFlowTest(unittest.TestCase):
    def test_equal_stock_different_flow(self):
        self.assertEqual(equilibrium(1, 1), equilibrium(2, 2))
        self.assertEqual(balance(1, 1, 1), balance(1, 2, 2))

    def test_same_exit_different_input(self):
        self.assertEqual(equilibrium(2, 1), 2 * equilibrium(1, 1))
        self.assertEqual(balance(2, 2, 1), 0)

    def test_failure(self):
        for j, k in [(-1, 1), (1, 0), (1, -1)]:
            with self.assertRaises(ValueError):
                equilibrium(j, k)
        for args in [(-1, 1, 1), (1, -1, 1), (1, 1, -1)]:
            with self.assertRaises(ValueError):
                balance(*args)

    def test_fraction(self):
        self.assertEqual(equilibrium(F(1, 3), F(2, 3)), F(1, 2))


if __name__ == '__main__':
    unittest.main()
