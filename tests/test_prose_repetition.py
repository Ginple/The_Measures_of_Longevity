"""Non-vacuity test for tools/prose_repetition.py: a shared sentence must be counted."""
import tempfile
import unittest
from pathlib import Path

import prose_repetition as pr

SHARED = 'Every number in this chapter answers only the question its study design can answer.'


class ProseRepetitionTest(unittest.TestCase):
    def test_shared_sentence_is_counted_and_unique_text_is_not(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            en = root / 'books/manuscript/en'
            en.mkdir(parents=True)
            for i in range(5):
                (en / f'CH0{i}_x.md').write_text(
                    f'# Chapter {i}\n\n{SHARED} Chapter {i} discusses its own topic number {i} at some length here.\n',
                    encoding='utf-8')
            r = pr.analyse(root, k=3)['en']
            self.assertTrue(r['comparable'])
            for c in r['chapters']:
                self.assertEqual((c['repeated'], c['sentences']), (1, 2))
            self.assertEqual(r['most_repeated'][0]['chapters'], 5)

    def test_headings_quotes_and_tables_are_excluded(self):
        self.assertEqual(pr.body_sentences('# ' + SHARED + '\n\n> ' + SHARED + '\n\n| ' + SHARED + ' |', 'en'), [])


if __name__ == '__main__':
    unittest.main()
