from fractions import Fraction as F
import unittest
from adaptive_capacity_example import simulate


class AdaptiveCapacityTest(unittest.TestCase):
    def test_reversal_equal_totals(self):
        even_a, even_c = [1, 1], [F(1, 2), F(3, 2)]
        pulse_a, pulse_c = [F(3, 2), F(1, 2)], [F(3, 2), F(1, 2)]
        even, pulse = simulate(even_a, even_c), simulate(pulse_a, pulse_c)
        self.assertEqual(sum(even_a), sum(pulse_a))
        self.assertEqual(sum(even_c), sum(pulse_c))
        self.assertEqual(even, [(F(1, 2), F(1, 2)), (F(3, 2), 0)])
        self.assertEqual(pulse, [(F(3, 2), 0), (F(1, 2), 0)])
        self.assertEqual(sum(s for s, q in even), sum(s for s, q in pulse))
        self.assertGreater(sum(q for s, q in even), sum(q for s, q in pulse))

    def test_mass_balance_and_capacity_grid(self):
        for a in range(4):
            for c in range(4):
                states = simulate([a, 1], [c, 1], initial=1)
                self.assertEqual(1+a+1, sum(s for s, q in states)+states[-1][1])
                self.assertLessEqual(states[0][0], c)
                self.assertLessEqual(states[1][0], 1)
                self.assertTrue(all(q >= 0 for _, q in states))

    def test_reject_invalid(self):
        for a, c, initial in [([], [], 0), ([1], [], 0), ([-1], [1], 0),
                              ([1], [-1], 0), ([1], [1], -1)]:
            with self.subTest(a=a, c=c, initial=initial), self.assertRaises(ValueError):
                simulate(a, c, initial)


if __name__ == '__main__':
    unittest.main()
