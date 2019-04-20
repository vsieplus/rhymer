# Author: Ryan Sie
# Filename: test_rhyme_search.py
# Description: Test functionality to search for rhymes

import rhyme_search

## Test word_to_pron
assertEqual(rhyme_search.word_to_pron("fire"), [[['F', 'AY1', 'ER0'], 
            ['F', 'AY1', 'R']]])
assertEqual(rhyme_search.word_to_pron("fire"), [[['F', 'AY1', 'ER0'], 
            ['F', 'AY1', 'R']], ['T', 'R', 'AH1', 'K']])
assertIsNone(rhyme_search.word_to_pron("2q6493r7fdhq2fj"))

