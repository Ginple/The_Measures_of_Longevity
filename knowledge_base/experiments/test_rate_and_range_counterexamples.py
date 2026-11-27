import unittest
from rate_and_range_counterexamples import fall_summary, ratio_summaries, examples


class RateAndRangeTests(unittest.TestCase):
    def test_recurrence_rate_can_change_without_changing_risk(self):
        x = examples()
        self.assertEqual(x['control']['fall_risk'], x['intervention']['fall_risk'])
        self.assertEqual(x['control']['events'], 100)
        self.assertEqual(x['intervention']['events'], 60)
        self.assertAlmostEqual(x['intervention']['fall_rate_per_person_year'], .6)

    def test_extrema_divided_by_median_are_not_paired_extrema(self):
        result = ratio_summaries([(1, 10)] + [(2, 100)]*8 + [(9, 10)])
        self.assertEqual(result['marginal_extrema_over_median_denominator'], [.01, .09])
        self.assertEqual(result['range_paired_ratios'], [.02, .9])
        self.assertEqual(result['ratio_of_marginal_medians'], .02)

    def test_zero_denominator_and_invalid_counts(self):
        for pairs in ([], [(0, 0)], [(2, 1)], [(-1, 10)], [(True, 10)], [(1.2, 10)]):
            with self.subTest(pairs=pairs), self.assertRaises(ValueError):
                ratio_summaries(pairs)
        for counts in ([], [-1], [True], [1.5]):
            with self.subTest(counts=counts), self.assertRaises(ValueError):
                fall_summary(counts)

    def test_no_falls(self):
        self.assertEqual(fall_summary([0, 0])['fall_rate_per_person_year'], 0)
        self.assertEqual(fall_summary([0, 0])['fall_risk'], 0)


if __name__ == '__main__':
    unittest.main()
