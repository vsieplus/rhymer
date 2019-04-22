# Author: Ryan Sie
# Filename: test_rhyme_search.py
# Description: Test functionality to search for rhymes

import unittest
import rhyme_search

fire_pron = ['F', 'AY1', 'ER0']
fire_pron2 = ['F', 'AY1', 'R']

class TestRhymeSearch(unittest.TestCase):

    # Test helper functions
    def test_word_to_pron(self):
        self.assertEqual(rhyme_search.word_to_pron("fire"), [fire_pron, 
                     fire_pron2])
        self.assertEqual(rhyme_search.word_to_pron("fire truck"), 
                     [['F', 'AY1', 'ER0', 'T', 'R', 'AH1', 'K'],
                      ['F', 'AY1', 'R', 'T', 'R', 'AH1', 'K']])
        self.assertIsNone(rhyme_search.word_to_pron("2q6493r7fdhq2fj"))

    def test_stress(self):
        self.assertEqual(rhyme_search.stress(fire_pron2), ['1'])
        self.assertEqual(rhyme_search.stress(['AY1', 'V', 'IH0', 'N']), ['1', '0'])

    def test_rhymes_by_syllable(self):
        self.assertEqual(rhyme_search.rhymes_by_syllable([('fire', fire_pron2, 1), 
                            ('tire', ['T', 'AY1', 'R'], 1), ('ivan', ['AY1', 'V', 'IH0', 'N'], 2)]),
                            [{'fire', 'tire'}, {'ivan'}])

    def test_stressify(self):
        self.assertEqual(rhyme_search.stressify(fire_pron, rhyme_search.UNSTRESSED), 
                            ['F', 'AY0', 'ER0'])
        self.assertEqual(rhyme_search.stressify(fire_pron, rhyme_search.PRIMARY_STRESS),
                            ['F', 'AY1', 'ER1'])

    def test_sound_pattern(self):
        self.assertEqual(rhyme_search.sound_pattern(fire_pron2, 
                         rhyme_search.ARPABET_CONSONANTS), ['F', '', 'R'])
        self.assertEqual(rhyme_search.sound_pattern(['F', 'AY', 'ER'],
                         rhyme_search.ARPABET_VOWELS), ['', 'AY', 'ER'])
        self.assertEqual(rhyme_search.sound_pattern(['T', 'AY', 'R'], 
                         rhyme_search.ARPABET_CONSONANTS), ['T', '', 'R'])

    # Test rhyme searches
    def test_perfect_rhymes(self):
        fire_rhymes = [('tire', ['T', 'AY1', 'ER0'], 2),
                       ('buyer', ['B', 'AY1', 'ER0'], 2),
                       ('liar', ['L', 'AY1', 'ER0'], 2)]
        for rhyme in fire_rhymes:
            self.assertIn(rhyme, rhyme_search.perfect(fire_pron))


    def test_near_rhymes(self):
        return 0

    def test_syllabic_rhymes(self):
        return 0

    def test_semi_rhymes(self):
        return 0

    def test_para_rhymes(self):
        return 0

    def test_asson_rhymes(self):
        return 0

    def test_identical_rhymes(self):
        return 0

    def test_eye_rhymes(self):
        return 0

if __name__ == '__main__':
    unittest.main()
