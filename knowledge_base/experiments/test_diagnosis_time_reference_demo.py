from fractions import Fraction as F
import unittest

from diagnosis_time_reference_demo import predict, shift_reference


class DiagnosisTimeReferenceDemoTests(unittest.TestCase):
    def test_exact_predictions_survive_reference_shift(self):
        for a in range(-1, 2):
            for b in range(-1, 2):
                for slope in range(-1, 2):
                    for reference in range(-2, 3):
                        adjusted_b = shift_reference(b, slope, reference)
                        for case, time in [(0, 0), (1, 1), (1, 2), (1, 3)]:
                            self.assertEqual(predict(a, b, slope, case, time),
                                             predict(a, adjusted_b, slope, case,
                                                     time - reference * case))

    def test_synthetic_example(self):
        self.assertEqual(shift_reference(0, 1, 2), F(2))
        self.assertEqual(predict(0, 0, 1, 1, 2), F(2))
        self.assertEqual(predict(0, 0, 1, 0, 0), F(0))

    def test_zero_slope_and_exact_fraction(self):
        self.assertEqual(shift_reference(F(1, 3), 0, 2), F(1, 3))
        self.assertEqual(shift_reference(F(1, 3), F(1, 2), F(1, 2)), F(7, 12))

    def test_reject_invalid_inputs(self):
        for args in [(0, 0, 1, True, 1), (0, 0, 1, 2, 1),
                     (0, 0, 1, 0, 1), (0.0, 0, 1, 1, 1)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                predict(*args)
        with self.assertRaises(ValueError):
            shift_reference(0, 1, 1.5)


if __name__ == '__main__':
    unittest.main()
