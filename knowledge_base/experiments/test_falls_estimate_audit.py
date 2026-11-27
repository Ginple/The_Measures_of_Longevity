import unittest
from falls_estimate_audit import absolute_projection, risk_ratio, report


class FallsEstimateAuditTests(unittest.TestCase):
    def test_projection_and_uncertainty_limits(self):
        result = absolute_projection(550, .74, (.65, .85))
        self.assertAlmostEqual(result['expected_per_thousand'], 407)
        self.assertEqual(result['conditional_ci_per_thousand'], [357.5, 467.5])
        self.assertAlmostEqual(result['fewer_per_thousand'], 143)

    def test_rounding_cannot_explain_reported_value(self):
        result = report()
        self.assertLess(result['rounding_upper_bound_for_projection'], 460.5)

    def test_denominator_sensitivity_without_claiming_meta_effect(self):
        result = report()
        self.assertAlmostEqual(result['harp_rr_paper_denominators'], 0.9389389389)
        self.assertAlmostEqual(result['harp_rr_review_appendix_denominators'], 0.8730694981)
        self.assertLess(result['harp_rr_review_appendix_denominators'], result['harp_rr_paper_denominators'])

    def test_validation(self):
        for args in [(float('nan'), .7, (.6, .8)), (1001, .7, (.6, .8)), (1, .7, (.8, .9)), (1, .7, (-1, .9))]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                absolute_projection(*args)
        for args in [(1, 0, 1, 2), (4, 3, 1, 2), (1, 2, 0, 2), (True, 2, 1, 2)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                risk_ratio(*args)


if __name__ == '__main__':
    unittest.main()
