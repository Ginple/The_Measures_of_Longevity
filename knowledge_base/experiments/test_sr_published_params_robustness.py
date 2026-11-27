import unittest
import sr_published_params_robustness as r


class PublishedParamsRobustness(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.res = r.level_matched(r.KARIN_2025_HUMAN, d=0.2)

    def test_levels_matched(self):
        p, q = self.res['lower_production'], self.res['raise_removal_matched']
        self.assertAlmostEqual(p['mean_X_alive_at_70'], q['mean_X_alive_at_70'], delta=0.01)

    def test_crossing_survives_published_parameters(self):
        self.assertTrue(r.crossing(self.res))

    def test_removal_steeper_late_hazard(self):
        p, q = self.res['lower_production'], self.res['raise_removal_matched']
        self.assertGreater(q['gompertz_slope_60_85'], p['gompertz_slope_60_85'])

    def test_both_beat_untreated(self):
        u = self.res['untreated']['life_expectancy']
        self.assertGreater(self.res['lower_production']['life_expectancy'], u)
        self.assertGreater(self.res['raise_removal_matched']['life_expectancy'], u)


if __name__ == '__main__':
    unittest.main()
