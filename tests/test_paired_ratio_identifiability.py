import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "knowledge_base" / "experiments"))

import unittest
from fractions import Fraction
from paired_ratio_identifiability import enumerate_pairings, example


class PairingTests(unittest.TestCase):
    def test_four_run_exhaustive_result(self):
        x = example()
        self.assertEqual(x['feasible_pairings'], 24)
        self.assertAlmostEqual(x['ratio_of_marginal_medians'], .1)
        self.assertAlmostEqual(x['lowest_paired_median']['median_ratio'], .05)
        self.assertAlmostEqual(x['highest_paired_median']['median_ratio'], .225)

    def test_excludes_impossible_counts_and_handles_duplicates(self):
        pairings = enumerate_pairings([2, 10], [5, 20])
        self.assertEqual(len(pairings), 1)
        self.assertEqual(pairings[0]['denominators'], (5, 20))
        self.assertEqual(pairings[0]['median'], Fraction(9, 20))
        self.assertEqual(len(enumerate_pairings([1, 1], [2, 2])), 1)

    def test_reject_bad_inputs_and_unmatchable(self):
        for ns, ds in [([], []), ([1], []), ([1], [0]), ([True], [2]), ([3], [2]), ([1]*9, [2]*9)]:
            with self.subTest(ns=ns, ds=ds), self.assertRaises(ValueError):
                enumerate_pairings(ns, ds)


if __name__ == '__main__':
    unittest.main()
