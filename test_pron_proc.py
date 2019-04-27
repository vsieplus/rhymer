# Author: Ryan Sie
# Filename: test_pron_proc.py
# Description: Test functionality for pronunciation processing functions

import unittest
import pron_proc
import rhyme_search

fire_pron = ['F', 'AY1', 'ER0']
fire_pron2 = ['F', 'AY1', 'R']

class TestPronProc(unittest.TestCase):

    # Test helper functions
    def test_word_to_pron(self):
        self.assertEqual(pron_proc.word_to_pron("fire"), [fire_pron, 
                     fire_pron2])
        self.assertEqual(pron_proc.word_to_pron("fire truck"), 
                     [['F', 'AY1', 'ER0', 'T', 'R', 'AH1', 'K'],
                      ['F', 'AY1', 'R', 'T', 'R', 'AH1', 'K']])
        self.assertIsNone(pron_proc.word_to_pron("2q6493r7fdhq2fj"))

    def test_stress(self):
        self.assertEqual(pron_proc.stress(fire_pron2), ['1'])
        self.assertEqual(pron_proc.stress(['AY1', 'V', 'IH0', 'N']), ['1', '0'])

    def test_stressify(self):
        self.assertEqual(pron_proc.stressify(fire_pron, pron_proc.UNSTRESSED), 
                            ['F', 'AY0', 'ER0'])
        self.assertEqual(pron_proc.stressify(fire_pron, pron_proc.PRIMARY_STRESS),
                            ['F', 'AY1', 'ER1'])

    def test_sound_pattern(self):
        self.assertEqual(pron_proc.sound_pattern(fire_pron2, 
                         pron_proc.ARPABET_CONSONANTS), ['F', '', 'R'])
        self.assertEqual(pron_proc.sound_pattern(['F', 'AY', 'ER'],
                         pron_proc.ARPABET_VOWELS), ['', 'AY', 'ER'])
        self.assertEqual(pron_proc.sound_pattern(['T', 'AY', 'R'], 
                         pron_proc.ARPABET_CONSONANTS), ['T', '', 'R'])



if __name__ == '__main__':
    unittest.main()
