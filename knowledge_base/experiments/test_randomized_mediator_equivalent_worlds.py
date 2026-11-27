from fractions import Fraction as F
import unittest

from randomized_mediator_equivalent_worlds import mediator, outcome, summarize


class RandomizedMediatorEquivalentWorldsTests(unittest.TestCase):
    def test_observed_distribution_and_total_effect_identical(self):
        a, b = summarize('mediated'), summarize('direct')
        self.assertEqual(a['observed'], b['observed'])
        self.assertEqual(a['observed'], {(0, 0, 0): F(3, 8), (0, 1, 1): F(1, 8),
                                        (1, 0, 0): F(1, 8), (1, 1, 1): F(3, 8)})
        self.assertEqual(a['total_effect'], F(1, 2))
        self.assertEqual(a['total_effect'], b['total_effect'])

    def test_natural_effects_differ(self):
        a, b = summarize('mediated'), summarize('direct')
        self.assertEqual((a['natural_direct_effect_at_M0'], a['natural_indirect_effect_at_Z1']),
                         (F(0), F(1, 2)))
        self.assertEqual((b['natural_direct_effect_at_M0'], b['natural_indirect_effect_at_Z1']),
                         (F(1, 2), F(0)))
        for result in (a, b):
            self.assertEqual(result['total_effect'], result['natural_direct_effect_at_M0'] +
                             result['natural_indirect_effect_at_Z1'])

    def test_every_mediator_value_occurs_in_each_arm(self):
        a = summarize('mediated')['observed']
        for z in (0, 1):
            for m in (0, 1):
                self.assertGreater(sum(p for (zz, mm, _), p in a.items() if (zz, mm) == (z, m)), 0)

    def test_controlled_mediator_and_invalid_world(self):
        for z in (0, 1):
            for u in (0, 1):
                self.assertEqual(outcome('mediated', z, mediator(z, u), u),
                                 outcome('direct', z, mediator(z, u), u))
                self.assertEqual(outcome('mediated', z, 1, u) - outcome('mediated', z, 0, u), 1)
                self.assertEqual(outcome('direct', z, 1, u) - outcome('direct', z, 0, u), 0)
        with self.assertRaises(ValueError):
            outcome('unknown', 0, 0, 0)


if __name__ == '__main__':
    unittest.main()
