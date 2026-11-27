from fractions import Fraction
import unittest

from familywise_illustration import familywise_independent


class FamilywiseIllustrationTests(unittest.TestCase):
    def test_exact_probability(self):
        self.assertEqual(familywise_independent(20, Fraction(1, 20)), 1 - Fraction(19, 20)**20)
        self.assertAlmostEqual(float(familywise_independent(20, Fraction(1, 20))), .6415140776)

    def test_boundaries(self):
        self.assertEqual(familywise_independent(0, Fraction(1, 20)), 0)
        self.assertEqual(familywise_independent(1, Fraction(1, 20)), Fraction(1, 20))
        self.assertEqual(familywise_independent(2, Fraction(1)), 1)

    def test_finite_union_bound_and_bonferroni(self):
        for n in range(1, 21):
            for alpha in (Fraction(0), Fraction(1, 100), Fraction(1, 20), Fraction(1, 2), Fraction(1)):
                p = familywise_independent(n, alpha)
                self.assertGreaterEqual(p, alpha)
                self.assertLessEqual(p, min(Fraction(1), n * alpha))
        target = Fraction(1, 20)
        self.assertLessEqual(familywise_independent(20, target / 20), target)

    def test_invalid(self):
        for n, alpha in [(True, Fraction(1, 20)), (-1, Fraction(1, 20)), (1, .05), (2, Fraction(5, 4))]:
            with self.subTest(n=n, alpha=alpha), self.assertRaises(ValueError):
                familywise_independent(n, alpha)


if __name__ == '__main__':
    unittest.main()
