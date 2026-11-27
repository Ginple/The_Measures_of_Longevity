"""Set arithmetic only: these tests do not validate published sample counts."""
import importlib.util
import itertools
from pathlib import Path
import unittest

P = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('calerie_bounds', P / 'knowledge_base/experiments/calerie_denominator_bounds.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class BoundsTests(unittest.TestCase):
    def test_bounds_exhaustive_small_sets(self):
        for n in range(6):
            subsets = [set(i for i in range(n) if mask & (1 << i)) for mask in range(1 << n)]
            for a, b in itertools.product(subsets, repeat=2):
                lower, upper = module.intersection_bounds(n, len(a), len(b))
                self.assertLessEqual(lower, len(a & b))
                self.assertLessEqual(len(a & b), upper)
                if len(a | b) == n:
                    self.assertEqual(module.exact_partition_if_union(len(a), len(b), n),
                                     (len(a-b), len(b-a), len(a & b)))

    def test_invalid_union(self):
        for args in [(3, 3, 7), (4, 1, 3), (-1, 1, 1), (1.0, 1, 1), (True, 1, 1)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                module.exact_partition_if_union(*args)

    def test_reported_scenarios(self):
        self.assertEqual(module.exact_partition_if_union(125, 117, 128), (11, 3, 114))
        self.assertEqual(module.exact_partition_if_union(66, 68, 69), (1, 3, 65))
        self.assertEqual(module.exact_partition_if_union(65, 68, 69), (1, 4, 64))

if __name__ == '__main__':
    unittest.main()
