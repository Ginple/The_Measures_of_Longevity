import unittest
from fractions import Fraction as F
from two_type_sharp_bounds import type1_bounds, change_bounds


class TwoTypeBoundsTests(unittest.TestCase):
    def test_example_and_endpoints(self):
        h = F(1, 2)
        self.assertEqual(type1_bounds(F(3, 5), h, h), (F(1, 5), F(1)))
        self.assertEqual(type1_bounds(F(2, 5), h, h), (F(0), F(4, 5)))
        self.assertEqual(change_bounds(F(3, 5), F(2, 5), (h, h), (h, h)), (F(-1), F(3, 5)))
        for x1, x2, y in [(F(1, 5), F(1), F(3, 5)), (F(4, 5), F(0), F(2, 5)),
                          (F(1), F(1, 5), F(3, 5)), (F(0), F(4, 5), F(2, 5))]:
            self.assertEqual(h*x1 + h*x2, y)

    def test_zero_and_full_weight(self):
        self.assertEqual(type1_bounds(F(3, 10), 0, F(1, 2)), (0, 1))
        self.assertEqual(type1_bounds(F(3, 10), 1, 1), (F(3, 10), F(3, 10)))
        self.assertEqual(type1_bounds(0, F(1, 2), 1), (0, 0))
        self.assertEqual(type1_bounds(1, F(1, 2), 1), (1, 1))

    def test_bounds_contain_grid_and_are_attainable(self):
        grid = [F(i, 10) for i in range(11)]
        for p in grid:
            for x1 in grid:
                for x2 in grid:
                    y = p*x1 + (1-p)*x2
                    lo, hi = type1_bounds(y, p, p)
                    self.assertLessEqual(lo, x1)
                    self.assertGreaterEqual(hi, x1)
                    if p < 1:
                        for endpoint in (lo, hi):
                            witness = (y-p*endpoint)/(1-p)
                            self.assertTrue(0 <= witness <= 1)

    def test_uncertain_weight_and_invalid(self):
        self.assertEqual(type1_bounds(F(2, 5), F(1, 2), F(4, 5)), (0, F(4, 5)))
        for bad in [(F(-1, 10), 0, 1), (1, F(3, 4), F(1, 2)), (1, 0, 2)]:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                type1_bounds(*bad)


if __name__ == '__main__':
    unittest.main()
