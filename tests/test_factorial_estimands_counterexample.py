import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "knowledge_base" / "experiments"))

import unittest
from factorial_estimands_counterexample import contrasts, examples


class FactorialEstimandsTests(unittest.TestCase):
    def test_additive_does_not_imply_synergy(self):
        a = examples()['additive']
        self.assertAlmostEqual(a['combined_vs_neither'], -.4)
        self.assertAlmostEqual(a['additive_interaction'], 0)
        self.assertAlmostEqual(a['a_effect_if_b0'], a['a_effect_if_b1'])

    def test_marginal_and_specific_contrasts_are_distinct(self):
        x = examples()['heterogeneous']
        self.assertAlmostEqual(x['a_effect_if_b0'], -.2)
        self.assertAlmostEqual(x['a_effect_if_b1'], .1)
        self.assertAlmostEqual(x['equal_weight_marginal_a'], -.05)
        self.assertAlmostEqual(x['combined_vs_neither'], -.1)
        self.assertAlmostEqual(x['additive_interaction'], .3)

    def test_factor_exchange_and_errors(self):
        a = contrasts(.4, .2, .3, .1)
        b = contrasts(.4, .3, .2, .1)
        self.assertAlmostEqual(a['a_effect_if_b0'], b['b_effect_if_a0'])
        self.assertAlmostEqual(a['additive_interaction'], b['additive_interaction'])
        for x in (-.1, 1.1, float('nan'), float('inf')):
            with self.subTest(x=x), self.assertRaises(ValueError):
                contrasts(.1, .2, .3, x)


if __name__ == '__main__':
    unittest.main()
