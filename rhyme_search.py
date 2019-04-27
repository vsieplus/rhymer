# Author: Ryan Sie
# Filename: rhyme_search.py
# Description: Functionality to search for rhymes

import setup 
import interact
import pron_proc
import re

# Functions to search for various rhymes 
# Each takes a pronunciation given as a list of phones and 
# returns a list of tuples, (word, pron, numSyll) for words for the given rhyme 

# Helper function to return list of tuples of rhymes matching the given final 
# sounds. Takes in a list of sounds to match (ARPABET) + original pronunciation, 
# and returns the list of matching tuples
def match_sounds(sounds, pron):
    return [(word,phon, pron_proc.num_syllables(phon)) for word,phon in setup.ENTRIES
                if phon[-len(sounds):] == sounds and phon != pron]

# Helper function to find words with the matching pattern of sounds
def match_pattern(pattern, pattern_set, pron):
    return [(word, phon, pron_proc.num_syllables(phon)) for word,phon in setup.ENTRIES
                if pron_proc.sound_pattern(pron_proc.stressify(phon, pron_proc.EMPTY_STRESS),
                    pattern_set) == pattern and phon != pron]


# A perfect rhyme occurs when the final stressed syllable vowel and all
# subsequent sounds are identical (i.e. smile ~ file)
def perfect(pron):
    # Locate stressed syllable, and declare sounds we want to match
    post_stress_sounds = pron[pron_proc.stress_idx(pron, pron_proc.PRIMARY_STRESS):]

    # Return tuples of words whose ending matches all sounds following 
    # the stressed syllable
    return match_sounds(post_stress_sounds, pron)
    
# A near rhyme occurs between a stressed and unstressed syllable 
# (i.e. caring ~ wing, turing ~ fluttering)
def near(pron):
    rhymes = []

    # Find near rhymes using primary stress of given pron
    prim_sound_idx = pron_proc.stress_idx(pron, pron_proc.PRIMARY_STRESS)

    # Calculate initial unstressed index
    unstressed_sound_idx = pron_proc.stress_idx(pron, pron_proc.UNSTRESSED)

    # If primary stress exists
    if prim_sound_idx != -1:
        # Retrieve unstressed version of sounds to match
        post_stress_sounds = pron_proc.stressify(pron[prim_sound_idx:], 
            pron_proc.UNSTRESSED)

        rhymes = rhymes + match_sounds(post_stress_sounds, pron)

        # Use only unstressed syllables after primary stress if exists
        if(len(post_stress_sounds) > 1):
            unstressed_sound_idx = pron_proc.stress_idx(post_stress_sounds[1:], 
                                              pron_proc.UNSTRESSED)
    else:
        # Reset primary index to search for unstressed near rhymes below
        prim_sound_idx = 0

    # If unstressed syllables do exist after primary stress or w/out primary
    # stress at all, find near rhymes using the unstressed syll. of given pron
    if unstressed_sound_idx != -1:
        # Retrieve stressed version of sounds to match
        post_stressless_sounds = pron[(prim_sound_idx + unstressed_sound_idx):]
        post_stressless_sounds = pron_proc.stressify(post_stressless_sounds, 
                                           pron_proc.PRIMARY_STRESS)

        rhymes = rhymes + match_sounds(post_stressless_sounds, pron)

    return rhymes

def syllabic(pron):
    return 0

def semi(pron):
    return 0

# A pararhyme occurs when two words have same consonant pattern
# (i.e. tall ~ tell)
def para(pron):
    cnsnt_pattern = pron_proc.sound_pattern(pron, pron_proc.ARPABET_CONSONANTS)

    # Find words with same consonant pattern and 
    return match_pattern(cnsnt_pattern, pron_proc.ARPABET_CONSONANTS, pron)

# Assonance occurs when two words have the same vowel pattern
# (i.e. bottle ~ nozzle)
def asson(pron):
    # Remove stress numbers from pronunciation
    nostress_pron = pron_proc.stressify(pron, pron_proc.EMPTY_STRESS)

    # Extract vowel pattern
    vowel_pattern = pron_proc.sound_pattern(nostress_pron, pron_proc.ARPABET_VOWELS)

    return match_pattern(vowel_pattern, pron_proc.ARPABET_VOWELS, pron)

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
    return [sorted(set([word for word,pron,numSyll in sorted_rhymes 
                if numSyll == i + 1]))
            for i in range(sorted_rhymes[-1][2])]
