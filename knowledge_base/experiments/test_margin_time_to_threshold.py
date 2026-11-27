import math
import unittest

from margin_time_to_threshold import (R_PROP, crossover_years, gain_from_level, gain_from_rate,
                                      run, years_linear, years_proportional)


class MarginTimeToThresholdTest(unittest.TestCase):
    def test_rate_parameter_from_twenty_percent_per_decade(self):
        self.assertAlmostEqual(math.exp(-10 * R_PROP), 0.8, places=12)

    def test_level_gain_is_independent_of_distance(self):
        g = 1.1
        for v0 in (19.0, 25.0, 40.0):
            self.assertAlmostEqual(years_proportional(v0 * g) - years_proportional(v0), gain_from_level(g), places=9)

    def test_rate_cut_scales_with_remaining_time(self):
        t = years_proportional(30.0)
        slower = years_proportional(30.0, r=R_PROP * 0.9)
        self.assertAlmostEqual(slower - t, gain_from_rate(t, 0.1), places=9)

    def test_crossover_is_where_both_gains_match(self):
        t_star = crossover_years(1.1, 0.1)
        self.assertAlmostEqual(gain_from_rate(t_star, 0.1), gain_from_level(1.1), places=9)

    def test_cross_sectional_linear_overstates_years_at_these_parameters(self):
        for row in run()['grid_men']:
            self.assertGreater(row['years_linear_cross_sectional'], row['years_proportional_longitudinal_upper'])

    def test_at_or_below_threshold_is_zero(self):
        self.assertEqual(years_linear(18.0), 0.0)
        self.assertEqual(years_proportional(17.0), 0.0)


if __name__ == '__main__':
    unittest.main()
