import unittest
from fractions import Fraction as F
from post_randomization_trajectory_counterexample import observed, do_x_mean, y


class TestPostRandomizationTrajectory(unittest.TestCase):
    def test_observational_worlds_identical_and_normalized(self):
        self.assertEqual(observed('A'), observed('B'))
        self.assertEqual(sum(observed('A').values()), 1)
        self.assertEqual(observed('A'), {(0, 0, 0): F(1, 4),
                                         (0, 1, 1): F(1, 4),
                                         (1, 1, 1): F(1, 2)})

    def test_same_observed_association_different_interventions(self):
        self.assertEqual((do_x_mean('A', 0), do_x_mean('A', 1)), (0, 1))
        self.assertEqual((do_x_mean('B', 0), do_x_mean('B', 1)), (F(3, 4), F(3, 4)))

    def test_z_randomized_in_both_worlds_and_no_positivity_at_z1(self):
        for world in ('A', 'B'):
            data = observed(world)
            self.assertEqual(sum(p for (z, _, _), p in data.items() if z == 0), F(1, 2))
            self.assertEqual(sum(p for (z, x, _), p in data.items() if z == 1 and x == 0), 0)
            self.assertEqual(sum(p for (z, _, outcome), p in data.items() if z == 1 and outcome == 1), F(1, 2))

    def test_invalid_inputs_rejected(self):
        with self.assertRaises(ValueError):
            do_x_mean('A', 2)
        with self.assertRaises(ValueError):
            y('invalid', 0, 0, 0)


if __name__ == '__main__':
    unittest.main()
