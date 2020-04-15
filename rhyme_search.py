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

    # If primary stress is after unstressed
    if prim_sound_idx > unstressed_sound_idx:
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
    if unstressed_sound_idx > prim_sound_idx:
        # Retrieve stressed version of sounds to match
        post_stressless_sounds = pron[(prim_sound_idx + unstressed_sound_idx):]
        post_stressless_sounds = pron_proc.stressify(post_stressless_sounds, 
                                           pron_proc.PRIMARY_STRESS)

        rhymes = rhymes + match_sounds(post_stressless_sounds, pron)

    return rhymes

# Syllabic rhyme - final syllables match, but unstressed
def syllabic(pron):
    # Check if last syllable unstressed
    stress_pattern = pron_proc.stress(pron)

    if stress_pattern[-1] != pron_proc.UNSTRESSED:
        return []

    # Locate unstressed syllable, and declare sounds we want to match
    final_syll = pron[pron_proc.stress_idx(pron, pron_proc.UNSTRESSED, 
                      len(stress_pattern) - 1):]

    # Return tuples of words whose ending matches all sounds following 
    # the stressed syllable
    return match_sounds(final_syll, pron)

# A semirhyme occurs when the stressed syllable + subsequent sounds of 
# one word matches another, but the other has an extra trailing syllable
# Ex. store ~ forecast (->), bookstore ~ book (<-)
def semi(pron):
    prim_stress_idx = pron_proc.stress_idx(pron, pron_proc.PRIMARY_STRESS)

    stress_pattern = pron_proc.stress(pron)

    # Look for (->) type semirhymes
    post_stress_sounds = pron[prim_stress_idx:]
    front_semirhymes = []
    for word,phon in setup.ENTRIES:
        phon_prim_stress_idx = pron_proc.stress_idx(phon, pron_proc.PRIMARY_STRESS)
        phon_post_stress = phon[phon_prim_stress_idx:]
        if (post_stress_sounds == phon_post_stress[:len(post_stress_sounds)] and
                pron_proc.num_syllables(post_stress_sounds) == 
                pron_proc.num_syllables(phon_post_stress) - 1):
            front_semirhymes.append((word, phon, pron_proc.num_syllables(phon)))

    # (<-) type semirhymes
    back_semirhymes = []
    # check if the stressed syllable is penultimate
    syllables = pron_proc.syllabify_helper(pron)
    for i in range(len(stress_pattern)):
        if stress_pattern[i] == pron_proc.PRIMARY_STRESS:
            stressed_syll_no_onset = list(syllables[i][1:])
            stressed_syll_no_onset = [phon for seg in stressed_syll_no_onset for phon in seg]
            back_semirhymes.extend(match_sounds(stressed_syll_no_onset, pron))
            break
    
    return front_semirhymes + back_semirhymes

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

    stress_pattern = pron_proc.stress(pron)

    # Extract vowel pattern - consider both with/without onset
    vowel_pattern = pron_proc.sound_pattern(nostress_pron, pron_proc.ARPABET_VOWELS)
    vowel_pattern_no_onset = vowel_pattern[pron_proc.stress_idx(pron, stress_pattern[0]):]

    return (match_pattern(vowel_pattern, pron_proc.ARPABET_VOWELS, pron) + 
            match_pattern(vowel_pattern_no_onset, pron_proc.ARPABET_VOWELS, pron))

# perfect rhyme in which the onset of the stressed syllable
# also matches - leave ~ believe
def identical(pron):
    syllables = pron_proc.syllabify_helper(pron)
    stressed_syll_after = syllables[pron_proc.stressed_syll_idx(pron, pron_proc.PRIMARY_STRESS):]
    stressed_syll_after = [p for syll in stressed_syll_after 
                             for phone in syll for p in phone]
    return match_sounds(stressed_syll_after, pron)

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
