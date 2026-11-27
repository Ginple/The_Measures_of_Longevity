"""Regression for an intentionally constructed post-randomization selection example."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'knowledge_base' / 'experiments'))
from post_randomization_selection_demo import demo


class PostRandomizationSelectionDemoTests(unittest.TestCase):
    def test_balanced_randomization_different_selected_composition(self):
        arms = demo()['arms']
        self.assertEqual((arms['control']['all_n'], arms['control']['all_positive']), (100, 50))
        self.assertEqual((arms['treatment']['all_n'], arms['treatment']['all_positive']), (100, 50))
        self.assertEqual((arms['control']['selected_n'], arms['control']['selected_positive']), (75, 25))
        self.assertEqual((arms['treatment']['selected_n'], arms['treatment']['selected_positive']), (75, 50))
        self.assertEqual(arms['control']['selected_risk'], '1/3')
        self.assertEqual(arms['treatment']['selected_risk'], '2/3')
        self.assertEqual(arms['selected_difference_treatment_minus_control'], '1/3')


if __name__ == '__main__':
    unittest.main()
