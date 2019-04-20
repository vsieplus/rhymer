# Author: Ryan Sie
# Filename: test_rhyme_search.py
# Description: Test functionality to search for rhymes

import unittest
import rhyme_search

## Test word_to_pron
class TestRhymeSearch(unittest.TestCase):

    def test_word_to_pron(self):
        self.assertEqual(rhyme_search.word_to_pron("fire"), [['F', 'AY1', 'ER0'], 
                     ['F', 'AY1', 'R']])
        self.assertEqual(rhyme_search.word_to_pron("fire truck"), 
                     [['F', 'AY1', 'ER0', 'T', 'R', 'AH1', 'K'],
                      ['F', 'AY1', 'R', 'T', 'R', 'AH1', 'K']])
        self.assertIsNone(rhyme_search.word_to_pron("2q6493r7fdhq2fj"))

if __name__ == '__main__':
    unittest.main()
