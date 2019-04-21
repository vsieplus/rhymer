# Author: Ryan Sie
# Filename: rhyme_search.py
# Description: Functionality to search for rhymes

import setup 
import interact
import re

# Stress constants
UNSTRESSED = '0'
PRIMARY_STRESS = '1'
SECONDARY_STRESS = '2'

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
def num_syllables(pron):
    return len(stress(pron))

# Helper function to determine index of first specified stress in a pronunciation
# Takes in a pronunciation (list of phones), and a stress character:
# '0' - unstressed || '1' - primary || '2' - secondary || ... 
# Returns index if found, or -1 if no primary stress present
def stress_idx(pron, stress):
    for i in range(len(pron)):
        for char in pron[i]:
            if char == stress:
                return i

    return -1

# Helper function to return an stressed version of the given sounds, based
# on the given stress
def stressify(sounds, stress):
    stressed_sounds = []
    for phon in sounds:
        stressed_sounds.append(re.sub('[0-9]', stress, phon))

    return stressed_sounds

# Functions to search for various rhymes 
# Each takes a pronunciation given as a list of phones and 
# returns a list of tuples, (word, pron, numSyll) for words for the given rhyme 

# Helper function to return list of tuples of rhymes matching the given final 
# sounds. Takes in a list of sounds to match (ARPABET) + original pronunciation, 
# and returns the list of matching tuples
def match_sounds(sounds, pron):
    return [(word,phon, num_syllables(phon)) for word,phon in setup.ENTRIES
                if phon[-len(sounds):] == sounds and phon != pron]

# A perfect rhyme occurs when the final stressed syllable vowel and all
# subsequent sounds are identical (i.e. smile ~ file)
def perfect(pron):
    # Locate stressed syllable, and declare sounds we want to match
    post_stress_sounds = pron[stress_idx(pron, PRIMARY_STRESS):]

    # Return tuples of words whose ending matches all sounds following 
    # the stressed syllable
    return match_sounds(post_stress_sounds, pron)
    
# A near rhyme occurs between a stressed and unstressed syllable 
# (i.e. caring ~ wing, turing ~ fluttering)
def near(pron):
    rhymes = []

    # Find near rhymes using primary stress of given pron
    prim_sound_idx = stress_idx(pron, PRIMARY_STRESS)

    # Calculate initial unstressed index
    unstressed_sound_idx = stress_idx(pron, UNSTRESSED)

    # If primary stress exists
    if prim_sound_idx != -1:
        # Retrieve unstressed version of sounds to match
        post_stress_sounds = stressify(pron[prim_sound_idx:], UNSTRESSED)

        rhymes = rhymes + match_sounds(post_stress_sounds, pron)

        # Use only unstressed syllables after primary stress if exists
        if(len(post_stress_sounds) > 1):
            unstressed_sound_idx = stress_idx(post_stress_sounds[1:], 
                                              UNSTRESSED)
    else:
        # Reset primary index to search for unstressed near rhymes below
        prim_sound_idx = 0

    # If unstressed syllables do exist after primary stress or w/out primary
    # stress at all, find near rhymes using the unstressed syll. of given pron
    if unstressed_sound_idx != -1:
        # Retrieve stressed version of sounds to match
        post_stressless_sounds = pron[(prim_sound_idx + unstressed_sound_idx):]
        post_stressless_sounds = stressify(post_stressless_sounds, 
                                           PRIMARY_STRESS)

        rhymes = rhymes + match_sounds(post_stressless_sounds, pron)

    return rhymes

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
# number of syllables. Returns a list of sets, where each inner set
# corresponds to rhymes containing a certain number of syllables
def rhymes_by_syllable(rhymes):
    # First sort tuples by number of syllables
    sorted_rhymes = sorted(rhymes, key = lambda rhyme: rhyme[2])

    # Return list of set of words, each set containing words of the same
    # number of syllables, for 1 <= numSyll <= max(rhymes.numSyll)
    return [set([word for word,pron,numSyll in sorted_rhymes 
                    if numSyll == i + 1])
            for i in range(sorted_rhymes[-1][2])]
