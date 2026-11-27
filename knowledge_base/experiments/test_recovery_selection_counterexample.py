import unittest
from recovery_selection_counterexample import summary, world


class RecoverySelectionTest(unittest.TestCase):
    def test_same_marginals_opposite_common_group_effect(self):
        a, b = summary(world('A')), summary(world('B'))
        self.assertEqual(a['history_arms'], b['history_arms'])
        self.assertEqual(a['history_arms']['0'], {'eligible': 50, 'positive': 20, 'positive_fraction_among_eligible': '2/5'})
        self.assertEqual(a['history_arms']['1'], {'eligible': 50, 'positive': 30, 'positive_fraction_among_eligible': '3/5'})
        self.assertEqual(a['always_eligible'], 25)
        self.assertEqual(b['always_eligible'], 25)
        self.assertEqual(a['effect_in_always_eligible'], '1')
        self.assertEqual(b['effect_in_always_eligible'], '-3/5')

    def test_valid_potential_outcomes_and_counts(self):
        for name in ('A', 'B'):
            units = world(name)
            for u in units:
                for h in (0, 1):
                    self.assertIn(u[f'y{h}'], (0, 1) if u[f'r{h}'] else (None,))
            types = [(u['r0'], u['r1']) for u in units]
            for t in ((True, True), (True, False), (False, True), (False, False)):
                self.assertEqual(types.count(t), 25)

    def test_invalid_world_and_empty(self):
        with self.assertRaises(ValueError):
            world('C')
        with self.assertRaises(ValueError):
            summary([])


if __name__ == '__main__':
    unittest.main()
