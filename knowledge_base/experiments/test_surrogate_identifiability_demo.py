"""Checks for the synthetic surrogate counterexample (stdlib unittest)."""
import unittest
from contextlib import redirect_stdout
from io import StringIO

from surrogate_identifiability_demo import correlation, run


class SurrogateDemoTests(unittest.TestCase):
    def test_correlations(self):
        self.assertAlmostEqual(correlation([1, 2, 3], [3, 4, 5]), 1)
        self.assertAlmostEqual(correlation([1, 2, 3], [5, 4, 3]), -1)

    def test_invalid_inputs(self):
        for x, y in [([], []), ([1], [1]), ([1, 2], [1]), ([1, 1], [2, 3])]:
            with self.subTest(x=x, y=y), self.assertRaises(ValueError):
                correlation(x, y)

    def test_counterexample_outputs_both_directions(self):
        stream = StringIO()
        with redirect_stdout(stream):
            run()
        out = stream.getvalue()
        self.assertIn('beneficial world: -1', out)
        self.assertIn('harmful world:    +1', out)
        self.assertIn('Synthetic deterministic example', out)


if __name__ == '__main__':
    unittest.main()
