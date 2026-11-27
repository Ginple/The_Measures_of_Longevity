from itertools import product
from fractions import Fraction as F
import unittest
from temporal_access_counterexample import simulate, aggregate_upper_bound


class TemporalAccessTest(unittest.TestCase):
    def test_equal_static_bound_different_dynamic(self):
        arrivals, edges = [1, 0], [1, 0]
        aligned = simulate(arrivals, edges, [1, 0])
        misaligned = simulate(arrivals, edges, [0, 1])
        self.assertEqual(aggregate_upper_bound(arrivals, edges, [1, 0]), 1)
        self.assertEqual(aggregate_upper_bound(arrivals, edges, [0, 1]), 1)
        self.assertEqual(aligned[-1][1], 0)
        self.assertEqual(misaligned[-1][1], 1)
        self.assertEqual(sum(x for x, _ in aligned), 1)
        self.assertEqual(sum(x for x, _ in misaligned), 0)

    def test_conservation_and_optimistic_bound_grid(self):
        for vals in product(range(3), repeat=6):
            a, e, r = vals[:2], vals[2:4], vals[4:]
            states = simulate(a, e, r)
            total = sum(p for p, _ in states)
            self.assertEqual(sum(a), total+states[-1][1])
            self.assertLessEqual(total, aggregate_upper_bound(a, e, r))
            for (p, q), edge, receiver in zip(states, e, r):
                self.assertTrue(0 <= p <= min(edge, receiver))
                self.assertGreaterEqual(q, 0)

    def test_fraction_and_waiting_in_source(self):
        self.assertEqual(simulate([F(1, 2), 0], [0, 1], [0, 1]), [(0, F(1, 2)), (F(1, 2), 0)])

    def test_reject_bad_schedules(self):
        for a, e, r in [([], [], []), ([1], [1, 2], [1]), ([1], [-1], [1]), ([1], [1], [-1])]:
            with self.subTest(a=a, e=e, r=r), self.assertRaises(ValueError):
                simulate(a, e, r)
            with self.assertRaises(ValueError):
                aggregate_upper_bound(a, e, r)


if __name__ == '__main__':
    unittest.main()
