# Author: Ryan Sie
# Filename: rhyme_search.py
# Description: Functionality to search for rhymes

import setup 

# Extract pronunciation(s) for a word/phrase
def word_to_pron(word):
    """Function to take a given word (in English spelling), and return its
       corresponding IPA pronunciation(s) (via ARPABET) if it exists. Otherwise
       returns None"""

    # If string given has multiple words, split
    words = word.split()

    # Try to search for pronunciations for each word
    try:
        word_prons = [[pron for pron in setup.PRON_DICT[w]] for w in words]
    except KeyError:
        # If no matching word was found
        return None 

    # Create all possible concatenations of pronunciations
    pronunciations = []

    for pronlist in word_prons:
        pronLen = len(pronunciations)
    
        if pronLen == 0:
            for pron in pronlist:    
                pronunciations.append(pron)
            continue

        # Check if we need to instantiate a new pronunciation
        k = 0
        while len(pronlist) * pronLen > len(pronunciations):
            pronunciations.append(pronunciations[k])
            k = k + 1
 
        # Concatenate each alternation
        for i in (range(len(pronlist))):
            for j in (range(len(pronunciations))):
                pronunciations[j] = pronunciations[j] + pronlist[i]

    return pronunciations 
