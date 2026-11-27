import unittest
from screening_endpoints_counterexample import Arm, examples, median_ratio_demo


class ScreeningCounterexamples(unittest.TestCase):
    def setUp(self):
        data = examples()
        self.c = data['control']
        self.w = data['intervention_worlds']

    def test_proportion_change_does_not_identify_population_incidence_change(self):
        x = self.w['extra_early_overdiagnoses_same_late_and_mortality']
        self.assertEqual((self.c['late_fraction_among_diagnosed'], x['late_fraction_among_diagnosed']), (.8, .4))
        self.assertEqual(self.c['late_risk_all_randomized'], x['late_risk_all_randomized'])
        self.assertEqual(x['overdiagnoses'], 100)

    def test_identical_observed_stage_counts_distinct_mortality(self):
        a = self.w['same_stage_shift_no_mortality_benefit']
        b = self.w['same_stage_shift_with_mortality_benefit']
        self.assertEqual((a['early'], a['late']), (b['early'], b['late']))
        self.assertEqual(a['cancer_death_risk_all_randomized'], self.c['cancer_death_risk_all_randomized'])
        self.assertLess(b['cancer_death_risk_all_randomized'], a['cancer_death_risk_all_randomized'])

    def test_invalid_inputs_rejected(self):
        for args in [(100, 90, 11, 1, 0), (100, 10, 10, 21, 0), (100, 10, 10, 1, 21), (0, 0, 0, 0, 0), (100, -1, 0, 0, 0)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                Arm(*args)

    def test_median_of_ratios_can_differ_from_ratio_of_medians(self):
        data = median_ratio_demo()
        self.assertAlmostEqual(data['ratio_of_medians'], 2 / 3)
        self.assertEqual(data['median_of_runwise_ratios'], .5)

    def test_empty_diagnosed_fraction_not_defined(self):
        self.assertIsNone(Arm(100, 0, 0, 0).metrics()['late_fraction_among_diagnosed'])

    def test_bool_and_fractional_count_rejected(self):
        for bad in (True, 1.5):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                Arm(100, bad, 10, 1)


if __name__ == '__main__':
    unittest.main()
