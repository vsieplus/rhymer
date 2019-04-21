# Author: Ryan Sie
# Filename: test_rhyme_search.py
# Description: Test functionality to search for rhymes

import unittest
import rhyme_search

fire_pron = ['F', 'AY1', 'ER0']

class TestRhymeSearch(unittest.TestCase):

    # Test helper functions
    def test_word_to_pron(self):
        self.assertEqual(rhyme_search.word_to_pron("fire"), [fire_pron, 
                     ['F', 'AY1', 'R']])
        self.assertEqual(rhyme_search.word_to_pron("fire truck"), 
                     [['F', 'AY1', 'ER0', 'T', 'R', 'AH1', 'K'],
                      ['F', 'AY1', 'R', 'T', 'R', 'AH1', 'K']])
        self.assertIsNone(rhyme_search.word_to_pron("2q6493r7fdhq2fj"))

    def test_stress(self):
        self.assertEqual(rhyme_search.stress(['F', 'AY1', 'R']), ['1'])
        self.assertEqual(rhyme_search.stress(['AY1', 'V', 'IH0', 'N']), ['1', '0'])

    def test_rhymes_by_syllable(self):
        self.assertEqual(rhyme_search.rhymes_by_syllable([('fire', ['F', 'AY1', 'R'], 1), 
                            ('tire', ['T', 'AY1', 'R'], 1), ('ivan', ['AY1', 'V', 'IH0', 'N'], 2)]),
                            [{'fire', 'tire'}, {'ivan'}])

    def test_unstressed(self):
        self.assertEqual(rhyme_search.unstressed(fire_pron), ['F', 'AY0', 'ER0'])


    # Test rhyme searches
    def test_perfect_rhymes(self):
        fire_rhymes = [('tire', ['T', 'AY1', 'ER0'], 2),
                       ('buyer', ['B', 'AY1', 'ER0'], 2),
                       ('liar', ['L', 'AY1', 'ER0'], 2)]
        for rhyme in fire_rhymes:
            self.assertIn(rhyme, rhyme_search.perfect(fire_pron))


if __name__ == '__main__':
    unittest.main()
