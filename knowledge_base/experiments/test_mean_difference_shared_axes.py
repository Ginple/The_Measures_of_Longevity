from fractions import Fraction as F
import unittest

from mean_difference_shared_axes import describe, sample_covariance


class MeanDifferenceSharedAxesTests(unittest.TestCase):
    def test_positive_negative_and_zero(self):
        for life, health, cov in [([70, 80, 90], [60, 65, 70], F(75, 2)),
                                  ([70, 75, 80], [50, 65, 80], F(-100)),
                                  ([68, 68, 72, 72], [58, 62, 58, 62], F(0))]:
            x = describe(life, health)
            self.assertEqual(x['cov_midpoint_gap'], cov)
            self.assertEqual(x['half_difference_of_variances'], cov)

    def test_identity_in_small_exhaustive_grid(self):
        # Enumerate all three-row synthetic records within a small integer grid.
        rows = [(l, h) for l in range(4) for h in range(l + 1)]
        for a in rows:
            for b in rows:
                for c in rows:
                    result = describe([a[0], b[0], c[0]], [a[1], b[1], c[1]])
                    self.assertEqual(result['cov_midpoint_gap'], result['half_difference_of_variances'])

    def test_cross_covariance_cancels_without_independence(self):
        self.assertEqual(sample_covariance([1, 2, 4], [2, 4, 8]), F(14, 3))
        result = describe([11, 12, 14], [2, 4, 8])
        self.assertEqual(result['cov_midpoint_gap'], result['half_difference_of_variances'])

    def test_invalid(self):
        for a, b in [([], []), ([1], [0]), ([1, 2], [1]), ([1, 2], [-1, 1]),
                     ([1, 2], [2, 1]), ([True, 2], [0, 1]), ([1.0, 2], [0, 1])]:
            with self.subTest(a=a, b=b), self.assertRaises(ValueError):
                describe(a, b)
        with self.assertRaises(ValueError):
            sample_covariance([1], [2])


if __name__ == '__main__':
    unittest.main()
