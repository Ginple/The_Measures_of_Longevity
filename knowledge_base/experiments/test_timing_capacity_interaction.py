from fractions import Fraction as F
import unittest
from timing_capacity_interaction import simulate, score


class TimingCapacityTest(unittest.TestCase):
    def test_four_cells_and_interaction(self):
        even, pulse = [1, 1], [F(3, 2), F(1, 2)]
        vals = [score(even, F(3, 2)), score(pulse, F(3, 2)),
                score(even, F(3, 4)), score(pulse, F(3, 4))]
        self.assertEqual(vals, [0, 0, F(3, 4), F(5, 4)])
        self.assertEqual(vals[3] - vals[2] - vals[1] + vals[0], F(1, 2))

    def test_balance_and_capacity(self):
        for capacity in [F(0), F(1, 4), F(3, 4), F(3, 2)]:
            for arrivals in [[0, 0], [1, 1], [F(3, 2), F(1, 2)]]:
                states = simulate(arrivals, capacity)
                self.assertEqual(sum(arrivals), sum(s for s, _ in states) + states[-1][1])
                self.assertTrue(all(0 <= s <= capacity and q >= 0 for s, q in states))

    def test_initial_backlog_and_empty_service(self):
        self.assertEqual(simulate([0, 0], 1, 1), [(1, 0), (0, 0)])

    def test_invalid(self):
        for args in [([], 1), ([-1], 1), ([1], -1), ([1], 1, -1)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                simulate(*args)


if __name__ == '__main__':
    unittest.main()
