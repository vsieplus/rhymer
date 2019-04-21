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
        print(interact.WORD_NOT_FOUND.format(interact.USER_WORD))
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

# Helper function to determine stress pattern of a pronunciation
def stress(pron):
    return [char for phone in pron for char in phone if char.isdigit()]

# Helper function to determine number of syllables
def num_syllalbes(pron):
    return len(stress(pron))

# Functions to search for various rhymes 
# Each takes a pronunciation given as a list of phones and 
# returns a list of pairs, (word, pron) for words fitting the given rhyme 

# A perfect rhyme occurs when the final stressed syllable vowel and all
# subsequent sounds are identical (i.e. smile ~ file)
def perfect(pron):
    # Locate stressed syllable, and declare sounds we want to match
    stress_idx = [i for i in range(len(pron)) for char in pron[i] if char == '1']
    stressed_syllable = pron[stress_idx[0]:]

    return [(word,phon, num_syllables(phon)) for word,phon in setup.ENTRIES
                if phon[-len(stressed_syllable):] == stressed_syllable]

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

# Switch statement to retrieve correct rhyme_search function
def rhyme_type_to_func(rtype):
    """Switch statement for determining behavior depending on specified
        type of rhyme"""
    type_dict = {
        interact.R_TYPES[interact.PERFECT_IDX]: perfect,
        interact.R_TYPES[interact.NEAR_IDX]: near,
        interact.R_TYPES[interact.SYLLABIC_IDX]: syllabic,
        interact.R_TYPES[interact.SEMI_IDX]: semi,
        interact.R_TYPES[interact.PARA_IDX]: para,
        interact.R_TYPES[interact.ASSON_IDX]: asson,
        interact.R_TYPES[interact.ID_IDX]: identical,
        interact.R_TYPES[interact.EYE_IDX]: eye,
    }

    return type_dict.get(rtype)

# Helper function to take a list of rhyme pairs, and sort them by 
# number of syllables. Returns a list of lists, where each inner list
# corresponds to rhymes containing a certain number of syllables
def rhymes_by_syllable(rhymes):
    # First sort tuples by number of syllables
    sorted_rhymes = sorted(rhymes, key = lambda rhyme: rhyme[2]))

    # Return list of lists of words, each list containing words of the same
    # number of syllables
    return [[word if numSyll == i] for i in range(sorted_rhymes[-1][2]) 
                                   for word,pron,numSyll in sorted_rhymes]
