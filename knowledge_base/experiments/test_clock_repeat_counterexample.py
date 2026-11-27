import unittest
from clock_repeat_counterexample import summarize


class ClockRepeatTest(unittest.TestCase):
    def test_more_labels_do_not_add_people(self):
        a, b, c = (summarize(n) for n in (1, 12, 120))
        self.assertEqual((a['people'], b['people'], c['people']), (2, 2, 2))
        self.assertEqual((a['clock_labels'], b['clock_labels'], c['clock_labels']), (3, 36, 360))
        for row in (a, b, c):
            self.assertAlmostEqual(row['grand_mean'], 1.0)
            self.assertAlmostEqual(row['se_person_mean'], 1.0)
        self.assertGreater(a['se_clock_means'], b['se_clock_means'])
        self.assertGreater(b['se_clock_means'], c['se_clock_means'])
        self.assertAlmostEqual(b['se_clock_means'], (24 / 35) ** 0.5 / 6)

    def test_invalid_repeats(self):
        for value in (0, -1, 1.0, True):
            with self.assertRaises(ValueError):
                summarize(value)


if __name__ == '__main__':
    unittest.main()
