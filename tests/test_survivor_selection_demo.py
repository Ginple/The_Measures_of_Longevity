"""Verify the invented counterexample, not the biology or clinical validity."""
import importlib.util
from fractions import Fraction
from pathlib import Path
import sys
import unittest

P = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('survivor_selection_demo', P/'knowledge_base/experiments/survivor_selection_demo.py')
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

class SurvivorSelectionTests(unittest.TestCase):
    def test_identical_marginals_but_opposite_principal_effects(self):
        a, b = module.summarize(module.WORLD_A), module.summarize(module.WORLD_B)
        for k in ('total', 'surv0', 'surv1', 'marginal0', 'marginal1', 'mean0', 'mean1', 'naive_difference'):
            self.assertEqual(a[k], b[k], k)
        self.assertEqual(a['naive_difference'], Fraction(40, 3))
        self.assertEqual(a['always_survivor_effect'], -10)
        self.assertEqual(b['always_survivor_effect'], 5)

    def test_undefined_mean_rejected(self):
        with self.assertRaises(ValueError):
            module.summarize((module.Type(10, None, 5),))
        with self.assertRaises(ValueError):
            module.summarize((module.Type(0, 1, 2),))

if __name__ == '__main__':
    unittest.main()
