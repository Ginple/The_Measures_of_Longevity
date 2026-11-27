from fractions import Fraction as F
import unittest
from cargo_fate_bounds import bounds, witness


class CargoFateBoundsTest(unittest.TestCase):
    def test_artificial_worlds_same_measurements(self):
        self.assertEqual(bounds(0, 6, 2), (0, 4))
        self.assertEqual(witness(0, 6, 2, 4), 0)
        self.assertEqual(witness(0, 6, 2, 1), 3)
        self.assertEqual(bounds(0, 6, 2, 0, 0), (4, 4))

    def test_other_exit_intervals_are_sharp(self):
        self.assertEqual(bounds(0, 6, 2, 1, 3), (1, 3))
        self.assertEqual(bounds(0, 6, 2, 1, 100), (0, 3))
        for d in (F(1), F(2), F(3)):
            other = witness(0, 6, 2, d)
            self.assertTrue(1 <= other <= 3)
            self.assertEqual(d + other, 4)

    def test_exhaustive_small_grid(self):
        for start in range(4):
            for uptake in range(4):
                for end in range(start+uptake+1):
                    low, high = bounds(start, uptake, end)
                    self.assertEqual(low, 0)
                    self.assertEqual(high, start+uptake-end)
                    for d in (low, high, (low+high)/2):
                        other = witness(start, uptake, end, d)
                        self.assertEqual(start+uptake-d-other, end)
                        self.assertGreaterEqual(other, 0)

    def test_invalid_inputs(self):
        for args in [(-1, 2, 0), (0, 1, 2), (0, 6, 2, 5, 6),
                     (0, 6, 2, 3, 2), (0, 1, 0, -1, 1)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                bounds(*args)
        for value in [-1, 5]:
            with self.assertRaises(ValueError):
                witness(0, 6, 2, value)


if __name__ == '__main__':
    unittest.main()
