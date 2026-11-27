from fractions import Fraction
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'knowledge_base' / 'experiments'))
from rounded_percentage_denominators import candidate_denominators


class RoundedDenominatorTests(unittest.TestCase):
    def test_57_row_has_unique_integer_even_without_search_cap(self):
        # 29.75 <= 5700/n <= 29.85 implies 190 < n < 192.
        self.assertGreater(Fraction(5700, 1) / Fraction('29.85'), 190)
        self.assertLess(Fraction(5700, 1) / Fraction('29.75'), 192)
        self.assertEqual(candidate_denominators([(57, '29.8')], 57, 1000), [191])
        self.assertNotIn(190, candidate_denominators([(57, '29.8')], 190, 191))

    def test_consistency_across_reported_rows(self):
        rows = [(3, '1.6'), (2, '1.0'), (1, '0.5'), (4, '2.1'),
                (5, '2.6'), (8, '4.2'), (42, '22.0'),
                (33, '17.3'), (57, '29.8'), (6, '3.1')]
        self.assertEqual(candidate_denominators(rows, 57, 1000), [191])

    def test_rounding_boundaries_are_conservative(self):
        # 1/8 = 12.5%, halfway between displayed 12 and 13 at integer precision.
        self.assertEqual(candidate_denominators([(1, '12')], 8, 8, 0), [8])
        self.assertEqual(candidate_denominators([(1, '13')], 8, 8, 0), [8])
        self.assertEqual(candidate_denominators([(0, '0.0')], 1, 3), [1, 2, 3])

    def test_reject_invalid_inputs(self):
        for rows in [[(-1, '1.0')], [(True, '1.0')], [(1, '1.00x')], [(1, '1.05')], [(1, '101')], [(1, 1.0)]]:
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                candidate_denominators(rows, 1, 10)
        with self.assertRaises(ValueError):
            candidate_denominators([], 0, 10)


if __name__ == '__main__':
    unittest.main()
