import unittest
from time_origin_counterexample import observed_risk, examples


class TimeOriginCounterexampleTests(unittest.TestCase):
    def test_equal_windows_opposite_directions(self):
        x = examples()
        self.assertEqual(x['early_peak'], {'baseline_origin': .5, 'delayed_origin': .35})
        self.assertEqual(x['late_peak'], {'baseline_origin': .35, 'delayed_origin': .5})

    def test_window_boundaries(self):
        days = [30, 31, 395, 396, None]
        self.assertEqual(observed_risk(days, 30), 2/5)

    def test_empty_and_invalid_window(self):
        for args in [([], 0, 365), ([1], -1, 365), ([1], 0, 0)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                observed_risk(*args)


if __name__ == '__main__':
    unittest.main()
