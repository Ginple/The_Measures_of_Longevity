import unittest
from fractions import Fraction as F
from selectivity_identification import table, world


class SelectivityIdentificationTest(unittest.TestCase):
    def test_conditional_denominator_reversal(self):
        a, b = table(30, 20, 20, 30), table(6, 4, 44, 46)
        self.assertEqual(a['n'], b['n'])
        self.assertEqual(a['marker_count'], b['marker_count'])
        self.assertEqual(a['marker_given_label'], F(3, 5))
        self.assertEqual(b['marker_given_label'], F(3, 5))
        self.assertEqual((a['label_given_marker'], b['label_given_marker']), (F(3, 5), F(3, 25)))

    def test_both_randomized_worlds_observationally_identical(self):
        for c in (0, 1):
            for p in (0, 1):
                self.assertEqual(world(c, p), world(c, p, indirect=False))
        outcomes = {(c, p): world(c, p)['outcome'] for c in (0, 1) for p in (0, 1)}
        self.assertEqual(outcomes[(1,1)]-outcomes[(1,0)]-outcomes[(0,1)]+outcomes[(0,0)], 20)
        self.assertEqual(world(1, 0)['label'], world(1, 1)['label'])

    def test_mediator_effect_not_identified(self):
        self.assertEqual(world(1, 0, 1)['outcome'] - world(1, 0, 0)['outcome'], 20)
        self.assertEqual(world(1, 0, 1, False)['outcome'] - world(1, 0, 0, False)['outcome'], 0)

    def test_invalid_inputs(self):
        for args in [(-1, 1, 1, 1), (0, 0, 2, 3), (0, 2, 0, 3)]:
            with self.assertRaises(ValueError):
                table(*args)
        for args in [(2, 0), (1, -1), (1, 0, 2)]:
            with self.assertRaises(ValueError):
                world(*args)


if __name__ == '__main__':
    unittest.main()
