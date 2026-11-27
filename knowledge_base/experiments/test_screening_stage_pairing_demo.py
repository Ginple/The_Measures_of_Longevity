from itertools import product
import unittest

from screening_stage_pairing_demo import summarize


class ScreeningStagePairingTests(unittest.TestCase):
    def test_three_worlds_have_same_margins_but_different_pairings(self):
        control = ['IV', 'IV', 'III', 'O']
        worlds = [['III', 'IV', 'III', 'O'], ['O', 'IV', 'III', 'III'],
                  ['III', 'III', 'IV', 'O']]
        outcomes = [summarize(zip(control, world)) for world in worlds]
        self.assertEqual([r['control_IV_to_intervention_III'] for r in outcomes], [1, 0, 2])
        self.assertTrue(all(r['control'] == outcomes[0]['control'] for r in outcomes))
        self.assertTrue(all(r['intervention'] == outcomes[0]['intervention'] for r in outcomes))

    def test_all_permutations_reveal_range_given_these_margins(self):
        control = ['IV', 'IV', 'III', 'O']
        values = set()
        for treated in product(('III', 'IV', 'O'), repeat=4):
            r = summarize(zip(control, treated))
            if r['intervention'] == {'III': 2, 'IV': 1, 'O': 1}:
                values.add(r['control_IV_to_intervention_III'])
        self.assertEqual(values, {0, 1, 2})

    def test_input_validation(self):
        for pairs in ([], [('IV',)], [('IV', 'bad')], [('IV', None)],
                      [('IV', [])], [3]):
            with self.subTest(pairs=pairs), self.assertRaises(ValueError):
                summarize(pairs)


if __name__ == '__main__':
    unittest.main()
