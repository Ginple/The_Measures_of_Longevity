from fractions import Fraction as F
import unittest

from cox_common_scale_demo import event_probability


class CoxCommonScaleDemoTests(unittest.TestCase):
    def test_risk_set_examples(self):
        weights = [2, 8, 16]
        self.assertEqual([event_probability(weights, i) for i in range(3)],
                         [F(1, 13), F(4, 13), F(8, 13)])
        self.assertEqual(event_probability([F(x, 10) for x in weights], 1), F(4, 13))

    def test_common_factor_cancels_for_all_small_risk_sets(self):
        for a in range(1, 5):
            for b in range(1, 5):
                for c in range(1, 5):
                    weights = [a, b, c]
                    for scale in [F(1, 10), F(1), F(10), F(7, 3)]:
                        for i in range(3):
                            self.assertEqual(event_probability(weights, i),
                                             event_probability([w * scale for w in weights], i))

    def test_nonuniform_scaling_need_not_cancel(self):
        self.assertNotEqual(event_probability([1, 1], 0), event_probability([1, 10], 0))

    def test_reject_invalid_inputs(self):
        for weights, index in [([], 0), ([1, 0], 0), ([1, -1], 0), ([1.0], 0),
                               ([True], 0), ([1], True), ([1], -1), ([1], 1)]:
            with self.subTest(weights=weights, index=index), self.assertRaises(ValueError):
                event_probability(weights, index)


if __name__ == '__main__':
    unittest.main()
