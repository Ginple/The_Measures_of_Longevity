"""PR #1 at 370dd15; test import path adapted for this worktree."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "knowledge_base" / "experiments"))
from itertools import combinations, product
import unittest
from complete_case_bounds import complete_case_bounds


class CompleteCaseBoundsTest(unittest.TestCase):
    def test_reported_example_is_conditional(self):
        low, high, lower_witness, upper_witness = complete_case_bounds(190, (57, 33, 6))
        self.assertEqual((low, high), (94, 133))
        for sets, expected in ((lower_witness, low), (upper_witness, high)):
            self.assertEqual([len(s) for s in sets], [57, 33, 6])
            self.assertEqual(190 - len(set().union(*sets)), expected)

    def test_all_small_three_timepoint_cohorts(self):
        for n in range(5):
            subsets = [set(c) for r in range(n + 1) for c in combinations(range(n), r)]
            for missing in product(range(n + 1), repeat=3):
                low, high, a, b = complete_case_bounds(n, missing)
                attainable = set()
                per_time = [[s for s in subsets if len(s) == m] for m in missing]
                for sets in product(*per_time):
                    attainable.add(n - len(set().union(*sets)))
                self.assertEqual((low, high), (min(attainable), max(attainable)))
                for witness, endpoint in ((a, low), (b, high)):
                    self.assertEqual(tuple(map(len, witness)), missing)
                    self.assertEqual(n - len(set().union(*witness)), endpoint)

    def test_no_timepoints_and_empty_cohort(self):
        self.assertEqual(complete_case_bounds(4, ())[:2], (4, 4))
        self.assertEqual(complete_case_bounds(0, (0, 0))[:2], (0, 0))

    def test_invalid_counts_rejected(self):
        for n, counts in [(-1, ()), (3, (-1,)), (3, (4,)), (3, (1.0,)), (True, (1,))]:
            with self.subTest(n=n, counts=counts), self.assertRaises(ValueError):
                complete_case_bounds(n, counts)


if __name__ == '__main__':
    unittest.main()
