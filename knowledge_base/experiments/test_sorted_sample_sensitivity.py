"""Synthetic selection sensitivity, not a tissue prevalence calculation."""
from fractions import Fraction as F
import unittest

from sorted_sample_sensitivity import sample_from_population, population_from_sample, population_bounds


class SortedSampleSensitivityTests(unittest.TestCase):
    def test_fictional_60_percent_multiple_population_fractions(self):
        q = F(3, 5)
        for ratio, actual in [(F(1, 10), F(15, 16)), (F(1), F(3, 5)), (F(10), F(3, 23))]:
            self.assertEqual(population_from_sample(q, ratio), actual)
            self.assertEqual(sample_from_population(actual, ratio), q)

    def test_assumption_sensitive_sharp_endpoints(self):
        q = F(3, 5)
        self.assertEqual(population_bounds(q, F(1, 2), 2), (F(3, 7), F(3, 4)))
        for k in range(5, 21):
            t = population_from_sample(q, F(k, 10))
            self.assertTrue(F(3, 7) <= t <= F(3, 4))
            self.assertEqual(sample_from_population(t, F(k, 10)), q)

    def test_exact_inverse_grid_and_boundary(self):
        for denominator in range(1, 12):
            for n in range(denominator + 1):
                t = F(n, denominator)
                for r in (F(1, 10), F(1, 2), F(1), F(3), F(10)):
                    self.assertEqual(population_from_sample(sample_from_population(t, r), r), t)

    def test_selection_rates_exhaustive_rational_grid(self):
        # Independently count expected selected masses for all feasible
        # positive inclusion probabilities on a small rational grid.
        for t_num in range(6):
            t = F(t_num, 5)
            for u in range(1, 6):
                for v in range(1, 6):
                    p_plus, p_minus = F(u, 5), F(v, 5)
                    positive_mass = t * p_plus
                    negative_mass = (1 - t) * p_minus
                    direct = positive_mass / (positive_mass + negative_mass)
                    self.assertEqual(sample_from_population(t, p_plus / p_minus), direct)
                    self.assertEqual(population_from_sample(direct, p_plus / p_minus), t)

    def test_zero_and_one_sample_bounds(self):
        self.assertEqual(population_bounds(0, F(1, 2), 2), (0, 0))
        self.assertEqual(population_bounds(1, F(1, 2), 2), (1, 1))
        for q in (F(-1, 2), F(3, 2)):
            with self.assertRaises(ValueError):
                population_bounds(q, F(1, 2), 2)

    def test_invalid_input(self):
        for f, r in [(F(-1, 2), 1), (F(3, 2), 1), (F(1, 2), 0), (F(1, 2), -1)]:
            for fn in (sample_from_population, population_from_sample):
                with self.subTest(fn=fn.__name__, f=f, r=r), self.assertRaises(ValueError):
                    fn(f, r)
        for lo, hi in ((0, 1), (2, 1), (-1, 2)):
            with self.assertRaises(ValueError):
                population_bounds(F(1, 2), lo, hi)


if __name__ == '__main__':
    unittest.main()
