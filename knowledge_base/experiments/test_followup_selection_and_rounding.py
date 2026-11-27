import unittest
from fractions import Fraction as F
from followup_selection_and_rounding import observed_arm_bounds, contrast_bounds, recovery_bounds


class FollowupTests(unittest.TestCase):
    def test_bounds_and_completions(self):
        self.assertEqual(observed_arm_bounds(30, 50, 100), (F(3, 10), F(4, 5)))
        self.assertEqual(contrast_bounds((30, 50, 100), (20, 50, 100)), (F(-2, 5), F(3, 5)))
        self.assertEqual(contrast_bounds((8, 10, 10), (2, 10, 10)), (F(3, 5), F(3, 5)))

    def test_ffm_rounding_does_not_explain_27_percent(self):
        lo, hi = recovery_bounds((F(265, 100), F(275, 100)), (F(5, 100), F(15, 100)))
        self.assertGreater(lo, 1)
        self.assertLess(hi, F(106, 100))
        self.assertFalse(lo <= F(27, 100) <= hi)

    def test_invalid_input(self):
        for counts in [(2, 1, 4), (0, 0, 0), (-1, 1, 2), (1.0, 2, 3)]:
            with self.subTest(counts=counts), self.assertRaises(ValueError):
                observed_arm_bounds(*counts)
        with self.assertRaises(ValueError):
            recovery_bounds((F(0), F(2)), (F(0), F(1)))


if __name__ == '__main__':
    unittest.main()
