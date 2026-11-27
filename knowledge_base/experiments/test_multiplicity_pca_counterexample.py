import unittest

from multiplicity_pca_counterexample import pca90, fwer_independent, fwer_equicorrelated


class MultiplicityTest(unittest.TestCase):
    def test_pca_count_and_independent_formula(self):
        self.assertEqual(pca90(16, 0), 15)
        expected = fwer_independent(16, .05 / 15)
        self.assertAlmostEqual(fwer_equicorrelated(16, 0, .05 / 15), expected, places=9)
        self.assertGreater(expected, .05)

    def test_correlated_counterexample_and_bonferroni(self):
        self.assertEqual(pca90(16, .9), 1)
        p = fwer_equicorrelated(16, .9, .05)
        self.assertGreater(p, .05)
        self.assertLess(fwer_equicorrelated(16, .9, .05 / 16), .05)
        self.assertAlmostEqual(p, fwer_equicorrelated(16, .9, .05, intervals=12000), places=8)

    def test_invalid_inputs(self):
        for args in ((1, 0), (3, 1), (3, -0.1)):
            with self.assertRaises(ValueError):
                pca90(*args)
        with self.assertRaises(ValueError):
            fwer_equicorrelated(4, .5, .05, intervals=5)


if __name__ == '__main__':
    unittest.main()
