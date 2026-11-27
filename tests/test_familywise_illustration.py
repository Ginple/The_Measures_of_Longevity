from fractions import Fraction
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'knowledge_base' / 'experiments'))
from familywise_illustration import familywise_independent


class FamilywiseIllustrationTests(unittest.TestCase):
    def test_exact_probability(self):
        self.assertEqual(familywise_independent(20, Fraction(1, 20)), 1 - Fraction(19, 20)**20)
        self.assertAlmostEqual(float(familywise_independent(20, Fraction(1, 20))), .6415140776)

    def test_boundaries(self):
        self.assertEqual(familywise_independent(0, Fraction(1, 20)), 0)
        self.assertEqual(familywise_independent(1, Fraction(1, 20)), Fraction(1, 20))
        self.assertEqual(familywise_independent(2, Fraction(1)), 1)

    def test_invalid(self):
        for n, alpha in [(True, Fraction(1, 20)), (-1, Fraction(1, 20)), (1, .05), (2, Fraction(5, 4))]:
            with self.subTest(n=n, alpha=alpha), self.assertRaises(ValueError):
                familywise_independent(n, alpha)


if __name__ == '__main__':
    unittest.main()
