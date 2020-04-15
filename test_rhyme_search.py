# Author: Ryan Sie
# Filename: test_rhyme_search.py
# Description: Test functionality to search for rhymes

import unittest
import rhyme_search

fire_pron = ['F', 'AY1', 'ER0']
fire_pron2 = ['F', 'AY1', 'R']

store_pron = ['S', 'T', 'AO1', 'R']

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
        fire_rhymes_perfect = rhyme_search.perfect(fire_pron)
        for rhyme in fire_rhymes:
            self.assertIn(rhyme, fire_rhymes_perfect)

    def test_near_rhymes(self):
        caring_rhymes = [('wing', ['W', 'IH1', 'NG'], 1),
                         ('sing', ['S', 'IH1', 'NG'], 1),
                         ('king', ['K', 'IH1', 'NG'], 1)]
        caring_rhymes_near = rhyme_search.near(['K', 'EH1', 'R', 'IH0', 'NG'])
        for rhyme in caring_rhymes:
            self.assertIn(rhyme, caring_rhymes_near)

    def test_syllabic_rhymes(self):
        fire_rhymes = [('later', ['L', 'EY1', 'T', 'ER0'], 2),
                       ('cater', ['K', 'EY1', 'T', 'ER0'], 2),
                       ('scooter', ['S', 'K', 'UW1', 'T', 'ER0'], 2)]
        fire_rhymes_syllabic = rhyme_search.syllabic(fire_pron)
        for rhyme in fire_rhymes:
            self.assertIn(rhyme, fire_rhymes_syllabic)

        self.assertFalse(rhyme_search.syllabic(['K', 'R', 'IY0', 'EY1', 'T']))

    def test_semi_rhymes(self):
        store_rhymes  = [('forecast', ['F', 'AO1', 'R', 'K', 'AE2', 'S', 'T'], 2),
                         ('boring', ['B', 'AO1', 'R', 'IH0', 'NG'], 2)]
        store_rhymes_semi = rhyme_search.semi(store_pron)
        for rhyme in store_rhymes:
            self.assertIn(rhyme, store_rhymes_semi)

        self.assertIn(('hook', ['HH', 'UH1', 'K'], 1), 
                      rhyme_search.semi(['B', 'UH1', 'K', 'S', 'T', 'AO2', 'R']))

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
