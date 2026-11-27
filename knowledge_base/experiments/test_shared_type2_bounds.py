"""Finite rational checks of synthetic shared-type constraints, not biological data."""
from fractions import Fraction as F
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'knowledge_base' / 'experiments'))
from shared_type2_bounds import shared_type2_change_bounds
from two_type_sharp_bounds import constrained_change_bounds


class SharedType2BoundsTests(unittest.TestCase):
    def test_common_value_narrows_and_can_point_identify(self):
        h, y0, y1, a, b = F(1, 2), F(3, 5), F(2, 5), F(2, 5), F(3, 5)
        self.assertEqual(constrained_change_bounds(y0, y1, h, h, (a, b), (a, b)),
                         (F(-3, 5), F(-1, 5)))
        self.assertEqual(shared_type2_change_bounds(y0, y1, h, h, a, b),
                         ((F(-2, 5), F(-2, 5)), (a, b)))
        self.assertEqual(shared_type2_change_bounds(y0, y1, h, F(1, 3), a, b),
                         ((F(-3, 5), F(-2, 5)), (a, b)))

    def test_individually_feasible_jointly_impossible(self):
        self.assertEqual(constrained_change_bounds(0, 1, F(1, 2), F(1, 2), (0, 1), (0, 1)), (1, 1))
        with self.assertRaisesRegex(ValueError, 'no common'):
            shared_type2_change_bounds(0, 1, F(1, 2), F(1, 2), 0, 1)
        with self.assertRaises(ValueError):
            shared_type2_change_bounds(0, 1, 0, 1, 0, 1)
        with self.assertRaises(ValueError):
            shared_type2_change_bounds(0, 1, 1, 1, 1, 0)

    def test_boundary_weights_and_singleton_feasible_set(self):
        self.assertEqual(shared_type2_change_bounds(F(1, 3), F(2, 3), 1, 1, 0, 1),
                         ((F(1, 3), F(1, 3)), (F(0), F(1))))
        self.assertEqual(shared_type2_change_bounds(0, F(1, 2), F(1, 2), 1, 0, 1),
                         ((F(1, 2), F(1, 2)), (F(0), F(0))))
        with self.assertRaises(ValueError):
            shared_type2_change_bounds(F(1, 2), F(1, 2), 0, 1, 0, 1)

    def test_exact_grid_feasibility_and_attainment(self):
        grid = [F(i, 4) for i in range(5)]
        positive = grid[1:]
        for p0 in positive:
            for p1 in positive:
                for x2 in grid:
                    for x0 in grid:
                        for x1 in grid:
                            y0 = p0*x0 + (1-p0)*x2
                            y1 = p1*x1 + (1-p1)*x2
                            (lo, hi), (a, b) = shared_type2_change_bounds(y0, y1, p0, p1, 0, 1)
                            self.assertTrue(a <= x2 <= b and lo <= x1-x0 <= hi)
                            actual = []
                            for witness in (a, b):
                                w0 = (y0-(1-p0)*witness)/p0
                                w1 = (y1-(1-p1)*witness)/p1
                                self.assertTrue(0 <= w0 <= 1 and 0 <= w1 <= 1)
                                actual.append(w1-w0)
                            self.assertEqual((min(actual), max(actual)), (lo, hi))


if __name__ == '__main__':
    unittest.main()
