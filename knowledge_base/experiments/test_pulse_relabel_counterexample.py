import unittest
from fractions import Fraction as F
from pulse_relabel_counterexample import evolve


class PulseRelabelTest(unittest.TestCase):
    def test_same_observed_totals_different_original_cohort(self):
        a = evolve(100, F(1,4), [0, 0])
        b = evolve(100, F(1,2), [25, F(75,4)])
        self.assertEqual([r['total'] for r in a], [r['total'] for r in b])
        self.assertEqual([r['labeled'] for r in a], [r['labeled'] for r in b])
        self.assertEqual(a[-1]['initial_cohort'], F(225,4))
        self.assertEqual(b[-1]['initial_cohort'], 25)

    def test_stock_balances_and_relabel_limits(self):
        rows = evolve(100, F(1,2), [25, F(75,4)])
        for prev, row in zip(rows, rows[1:]):
            self.assertEqual(prev['total']-row['exit_total']+row['new_entries'], row['total'])
            self.assertEqual(prev['labeled']*F(1,2)+row['relabel'], row['labeled'])
            self.assertLessEqual(row['initial_cohort'], row['labeled'])

    def test_no_exit(self):
        self.assertEqual(evolve(10, 0, [0, 0])[-1]['initial_cohort'], 10)

    def test_invalid(self):
        for args in [(0, 0, []), (1, -1, []), (1, 2, []), (100, F(1,2), [51]), (10, 0, [-1])]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                evolve(*args)


if __name__ == '__main__':
    unittest.main()
