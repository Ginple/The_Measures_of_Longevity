"""Synthetic sensitivity illustration: accurate reads do not imply accurate weights."""
from fractions import Fraction as F
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'knowledge_base' / 'experiments'))
from two_mixture_inversion import reconstruct, error_amplification


class WeightCalibrationTests(unittest.TestCase):
    def test_weight_error_escapes_readout_only_bound(self):
        x1, x2 = F(4, 5), F(1, 5)
        actual_p, actual_q = F(1, 2), F(51, 100)
        assumed_q = F(13, 25)
        ya = actual_p*x1 + (1-actual_p)*x2
        yb = actual_q*x1 + (1-actual_q)*x2
        self.assertEqual((ya, yb), (F(1, 2), F(253, 500)))
        self.assertEqual(reconstruct(ya, yb, actual_p, actual_q), (x1, x2))
        self.assertEqual(reconstruct(ya, yb, actual_p, assumed_q), (F(13, 20), F(7, 20)))
        self.assertEqual(error_amplification(actual_p, assumed_q, 0, 0), (0, 0))
        # The nonzero error is outside this bound's contract: weights are wrong.
        self.assertEqual(abs(x1-F(13, 20)), F(3, 20))


if __name__ == '__main__':
    unittest.main()
