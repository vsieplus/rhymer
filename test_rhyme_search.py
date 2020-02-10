# Author: Ryan Sie
# Filename: test_rhyme_search.py
# Description: Test functionality to search for rhymes

import unittest
import rhyme_search

fire_pron = ['F', 'AY1', 'ER0']
fire_pron2 = ['F', 'AY1', 'R']

class TestRhymeSearch(unittest.TestCase):
    
    def test_rhymes_by_syllable(self):
        self.assertEqual(rhyme_search.rhymes_by_syllable([('fire', fire_pron2, 1), 
                            ('tire', ['T', 'AY1', 'R'], 1), ('ivan', ['AY1', 'V', 'IH0', 'N'], 2)]),
                            [['fire', 'tire'], ['ivan']])

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
        fire_rhymes = [('later', ['L', 'EY1', 'T', 'ER0'], 2),
                       ('cater', ['K', 'EY1', 'T', 'ER0'], 2),
                       ('scooter', ['S', 'K', 'UW1', 'T', 'ER0'], 2)]
        for rhyme in fire_rhymes:
            self.assertIn(rhyme, rhyme_search.syllabic(fire_pron))

        self.assertFalse(rhyme_search.syllabic(['K', 'R', 'IY0', 'EY1', 'T']))

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
