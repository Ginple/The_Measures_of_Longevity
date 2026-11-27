import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "knowledge_base" / "experiments"))

import unittest
from fractions import Fraction as F
from two_mixture_inversion import reconstruct, error_amplification


class TwoMixtureInversionTests(unittest.TestCase):
    def test_exact_all_grid_points(self):
        grid = [F(i, 5) for i in range(6)]
        for pa in grid:
            for pb in grid:
                if pa == pb:
                    continue
                for x1 in grid:
                    for x2 in grid:
                        ya, yb = pa*x1+(1-pa)*x2, pb*x1+(1-pb)*x2
                        self.assertEqual(reconstruct(ya, yb, pa, pb), (x1, x2))

    def test_sharp_error_example(self):
        p, q, e, y = F(1, 2), F(51, 100), F(1, 1000), F(1, 2)
        x = reconstruct(y, y, p, q)
        changed = reconstruct(y+e, y-e, p, q)
        self.assertEqual(changed, (F(401, 1000), F(601, 1000)))
        self.assertEqual(tuple(abs(a-b) for a, b in zip(x, changed)),
                         error_amplification(p, q, e, e))
        self.assertEqual(error_amplification(p, q, e, e), (F(99, 1000), F(101, 1000)))

    def test_wider_weight_separation_reduces_equal_error_bound(self):
        e = F(1, 1000)
        near = error_amplification(F(1, 2), F(51, 100), e, e)
        far = error_amplification(F(1, 4), F(3, 4), e, e)
        self.assertEqual(far, (F(1, 500), F(1, 500)))
        self.assertGreater(near[0], far[0])
        self.assertGreater(near[1], far[1])

    def test_singular_infeasible_and_invalid(self):
        for args in [(0, 0, F(1, 2), F(1, 2)), (1, 0, F(1, 2), F(1, 2)),
                     (1, 0, F(49, 100), F(51, 100)), (2, 0, 0, 1)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                reconstruct(*args)
        for args in [(0, 0, 0, 0), (0, 1, -1, 0), (0, 2, 0, 0)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                error_amplification(*args)

    def test_reversing_measurement_order_and_zero_error(self):
        p, q, ya, yb = F(1, 4), F(3, 4), F(7, 20), F(13, 20)
        self.assertEqual(reconstruct(ya, yb, p, q), reconstruct(yb, ya, q, p))
        self.assertEqual(error_amplification(p, q, 0, 0), (0, 0))
        self.assertEqual(error_amplification(p, q, F(1, 100), F(2, 100)),
                         error_amplification(q, p, F(2, 100), F(1, 100)))


if __name__ == '__main__':
    unittest.main()
