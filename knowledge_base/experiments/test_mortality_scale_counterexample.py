import unittest
from mortality_scale_counterexample import compare_hazard_and_probability_scaling


class MortalityScaleTests(unittest.TestCase):
    def test_non_equivalence(self):
        x = compare_hazard_and_probability_scaling(.2, 1.79)
        self.assertAlmostEqual(x['direct_multiple'], .358)
        self.assertAlmostEqual(x['proportional_hazard_probability'], 1 - .8**1.79)
        self.assertGreater(x['direct_multiple'], x['proportional_hazard_probability'])

    def test_equality_at_identity_or_zero(self):
        for q, h in ((0, 1.79), (.2, 1), (.2, 0)):
            x = compare_hazard_and_probability_scaling(q, h)
            self.assertAlmostEqual(x['direct_multiple'], x['proportional_hazard_probability'])

    def test_invalid(self):
        for q, h in ((1, 1), (-1, 1), (.2, -1), (float('nan'), 1), (.2, float('inf'))):
            with self.subTest(q=q, h=h), self.assertRaises(ValueError):
                compare_hazard_and_probability_scaling(q, h)


if __name__ == '__main__':
    unittest.main()
