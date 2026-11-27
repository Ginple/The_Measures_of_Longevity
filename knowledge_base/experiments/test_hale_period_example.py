from fractions import Fraction as F
import unittest
from hale_period_example import hale, slope_difference


class HalePeriodExampleTest(unittest.TestCase):
    def test_exact_synthetic_table(self):
        self.assertEqual(hale(100, [1000, 800], [F(1, 10), F(1, 4)]), (18, 15, 3))
        self.assertEqual((20*F(1) + 80*F(7, 2))/100, 3)
        self.assertNotIn(3, (F(1), F(7, 2)))

    def test_separates_elapsed_intervals_from_inclusive_years(self):
        a, b = slope_difference(F(13, 2), 2000, 2019)
        self.assertEqual(a, F(13, 38))
        self.assertEqual(b, F(13, 40))
        self.assertEqual(a/b, F(20, 19))

    def test_zero_and_complete_health_loss(self):
        self.assertEqual(hale(10, [100], [0]), (10, 10, 0))
        self.assertEqual(hale(10, [100], [1]), (10, 0, 10))

    def test_bad_inputs(self):
        for n, years, losses in [(0, [1], [0]), (1, [], []), (1, [1, 2], [0]),
                                  (1, [-1], [0]), (1, [1], [F(3, 2)])]:
            with self.subTest(n=n, years=years, losses=losses), self.assertRaises(ValueError):
                hale(n, years, losses)
        with self.assertRaises(ValueError):
            slope_difference(1, 2000, 2000)


if __name__ == '__main__':
    unittest.main()
