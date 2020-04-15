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
        ball_rhymes = [('bull', ['B', 'UH1', 'L'], 1),
                       ('bill', ['B', 'IH1', 'L'], 1),
                       ('bell', ['B', 'EH1', 'L'], 1)]
        ball_rhymes_para = rhyme_search.para(['B', 'AA1', 'L'])
        for rhyme in ball_rhymes:
            self.assertIn(rhyme, ball_rhymes_para)

    def test_asson_rhymes(self):
        catnip_rhymes = [('catfish', ['K', 'AE1', 'T', 'F', 'IH2', 'SH'], 2),
                         ('rancid', ['R', 'AE1', 'N', 'S', 'IH0', 'D'], 2),
                         ('average', ['AE1', 'V', 'R', 'IH0', 'JH'], 2)]
        catnip_rhymes_para = rhyme_search.asson(['K', 'AE1', 'T', 'N', 'IH0', 'P'])
        for rhyme in catnip_rhymes:
            self.assertIn(rhyme, catnip_rhymes_para)

    def test_identical_rhymes(self):
        leave_rhymes = [('believe', ['B', 'IH0', 'L', 'IY1', 'V'], 2),
                        ('sleeve', ['S', 'L', 'IY1', 'V'], 1),
                        ('cleave', ['K', 'L', 'IY1', 'V'], 1)]
        leave_rhymes_id = rhyme_search.identical(['L', 'IY1', 'V'])
        for rhyme in leave_rhymes:
            self.assertIn(rhyme, leave_rhymes_id)

if __name__ == '__main__':
    unittest.main()
