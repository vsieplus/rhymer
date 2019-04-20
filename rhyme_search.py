# Author: Ryan Sie
# Filename: rhyme_search.py
# Description: Functionality to search for rhymes

import setup 
import interact

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

# Functions to search for various rhymes 
# Each takes a pronunciation given as a list of phones and 
# returns a list of words (in English orthography) for the given rhyme type

def perfect(pron):
    return 0

def near(pron):
    return 0

def syllabic(pron):
    return 0

def semi(pron):
    return 0

def para(pron):
    return 0

def asson(pron):
    return 0

def identical(pron):
    return 0

def eye(pron):
    return 0

def rhyme_type_to_func(rtype):
    """Switch statement for determining behavior depending on specified
        type of rhyme"""
    type_dict = {
        interact.TYPES[interact.PERFECT_IDX]: perfect,
        interact.TYPES[interact.NEAR_IDX]: near,
        interact.TYPES[interact.SYLLABIC_IDX]: syllabic,
        interact.TYPES[interact.SEMI_IDX]: semi,
        interact.TYPES[interact.PARA_IDX]: para,
        interact.TYPES[interact.ASSON_IDX]: asson,
        interact.TYPES[interact.ID_IDX]: identical,
        interact.TYPES[interact.EYE_IDX]: eye,
    }

    rhyme_func = type_dict.get(rtype)

    # Return result of the corresponding function
    return rhyme_func()

