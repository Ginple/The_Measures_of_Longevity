import unittest
from truncation_by_death_counterexample import add_type, population, report


class TruncationByDeathTests(unittest.TestCase):
    def test_observationally_identical_but_different_sace(self):
        a, b = report('A'), report('B')
        self.assertEqual(a['observed_arms'], b['observed_arms'])
        for arm in ('0', '1'):
            self.assertEqual(a['observed_arms'][arm]['n'], 100)
            self.assertEqual(a['observed_arms'][arm]['survivors'], 75)
            self.assertEqual(a['observed_arms'][arm]['survivor_score_1'], 50)
        self.assertEqual(a['latent_sace'], 0)
        self.assertEqual(b['latent_sace'], .5)
        self.assertEqual(a['composite_treatment_minus_control'], 0)
        self.assertEqual(b['composite_treatment_minus_control'], 0)

    def test_balanced_assignments_and_well_defined_potentials(self):
        for world in ('A', 'B'):
            people = population(world)
            self.assertEqual(sum(p.treatment for p in people), 100)
            for p in people:
                self.assertEqual(p.y0 is not None, p.survives0)
                self.assertEqual(p.y1 is not None, p.survives1)
                self.assertIn(p.y0, (None, 0, 1))
                self.assertIn(p.y1, (None, 0, 1))

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            population('C')
        for n in (0, 1, -2):
            with self.assertRaises(ValueError):
                add_type([], n, True, True, 1, 1)


if __name__ == '__main__':
    unittest.main()
