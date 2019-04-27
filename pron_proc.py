# Author: Ryan Sie
# Filename: pron_proc.py
# Description: Functionality to process pronunciations

import setup 
import interact
import re

# Stress constants
EMPTY_STRESS = ''
UNSTRESSED = '0'
PRIMARY_STRESS = '1'
SECONDARY_STRESS = '2'

# ARPABET SYMBOLS
ARPABET_CONSONANTS = ['B', 'CH', 'D', 'DH', 'DX', 'EM', 'EN', 'EL', 'F', 'G'
                      'HH', 'H', 'JH', 'K', 'L', 'M', 'N', 'NX', 'NG', 'P', 'Q',
                      'R', 'S', 'SH', 'T', 'TH', 'V', 'W', 'WH', 'Y', 'Z', 'ZH']
ARPABET_VOWELS = ['AA', 'AE', 'AH', 'AO', 'AW', 'AX', 'AXR', 'AY', 'EH', 'ER',
                  'EY', 'IH', 'IX', 'IY', 'OW', 'OY', 'UH', 'UW', 'UX']

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
def stressify(sounds, STRESS):
    stressed_sounds = []
    for phon in sounds:
        stressed_sounds.append(re.sub('[0-9]', STRESS, phon))

    return stressed_sounds

# Helper function to return the specified pattern of sounds in SOUNDS from pron
def sound_pattern(pron, SOUNDS):
    return [phon if phon in SOUNDS else '' for phon in pron]
