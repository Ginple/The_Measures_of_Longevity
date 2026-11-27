import math
import unittest
import sr_snapshot_identifiability as m

COARSE = {'dt': 0.1, 'dx': 0.2}


class QuasiSteadyTest(unittest.TestCase):
    def test_production_and_removal_give_identical_level_but_different_recovery(self):
        b, d = m.BASE, 0.2
        for t in (40.0, 60.0, 70.0, 80.0):
            xa = m.quasi_steady_level(t, b['eta'] * (1 - d), b['beta'], b['kappa'])
            xb = m.quasi_steady_level(t, b['eta'], b['beta'] / (1 - d), b['kappa'])
            self.assertAlmostEqual(xa, xb, places=12)
            ratio = m.relaxation_rate(xb, b['beta'] / (1 - d), b['kappa']) / m.relaxation_rate(xa, b['beta'], b['kappa'])
            self.assertAlmostEqual(ratio, 1 / (1 - d), places=12)

    def test_collapse_and_identification_round_trip(self):
        self.assertEqual(m.quasi_steady_level(100.0, 0.05, 5.0, 0.5), math.inf)
        beta, kappa = 3.7, 0.8
        x1, x2 = 1.0, 4.0
        got = m.identify_beta_kappa(x1, m.relaxation_rate(x1, beta, kappa), x2, m.relaxation_rate(x2, beta, kappa))
        self.assertAlmostEqual(got[0], beta, places=9)
        self.assertAlmostEqual(got[1], kappa, places=9)

    def test_invalid(self):
        for f, args in [(m.quasi_steady_level, (1, 0, 1, 1)), (m.relaxation_rate, (-1, 1, 1)),
                        (m.identify_beta_kappa, (1, 1, 1, 1))]:
            with self.subTest(f=f.__name__), self.assertRaises(ValueError):
                f(*args)
        with self.assertRaises(ValueError):
            m.survival_curve({**m.BASE, 'eps': 0})


class FirstPassageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.summary, cls.runs = m.scenarios(**COARSE)

    def test_survival_is_a_monotone_probability(self):
        s = [r[1] for r in self.runs['untreated']]
        self.assertTrue(all(0 <= v <= 1 + 1e-9 for v in s))
        self.assertTrue(all(b <= a + 1e-12 for a, b in zip(s, s[1:])))

    def test_baseline_is_human_like_but_illustrative(self):
        u = self.summary['untreated']
        self.assertTrue(75 < u['median_age_at_death'] < 85)
        self.assertTrue(0.06 < u['gompertz_slope_60_85'] < 0.12)

    def test_threshold_raises_survival_while_survivors_read_older(self):
        u, t = self.summary['untreated'], self.summary['raise_threshold']
        self.assertGreater(t['life_expectancy'], u['life_expectancy'])
        self.assertGreater(t['mean_X_alive_at_70'], u['mean_X_alive_at_70'])

    def test_pulse_reads_younger_transiently(self):
        u, p = self.summary['untreated'], self.summary['removal_pulse']
        self.assertLess(p['mean_X_alive_at_61'], u['mean_X_alive_at_61'] - 0.3)
        self.assertLess(abs(p['mean_X_alive_at_70'] - u['mean_X_alive_at_70']), 0.1)

    def test_level_matched_interventions_cross_in_survival(self):
        lp = self.summary['lower_production']
        db = m.match_removal_to_level(lp['mean_X_alive_at_70'], iters=14, **COARSE)
        b = m.BASE
        rm = m.summarize(m.survival_curve(b, start=(60.0, {**b, 'beta': b['beta'] / (1 - db)}), **COARSE))
        self.assertAlmostEqual(rm['mean_X_alive_at_70'], lp['mean_X_alive_at_70'], delta=0.01)
        self.assertGreater(rm['S70'], lp['S70'])                  # removal ahead early
        self.assertLess(rm['S90'], lp['S90'])                     # production ahead late
        self.assertLess(rm['life_expectancy'], lp['life_expectancy'])

    def test_damage_age_is_identity_on_untreated(self):
        un = self.runs['untreated']
        self.assertAlmostEqual(m.damage_age(un, self.summary['untreated']['mean_X_alive_at_70']), 70.0, delta=0.2)


if __name__ == '__main__':
    unittest.main()
