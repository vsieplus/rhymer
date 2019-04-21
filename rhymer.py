# Author: Ryan Sie
# Filename: rhymer.py
# Description: Main script for rhymer program

"""Welcome to Rhymer! A Rhyming dictionary for all your rhyming needs.
   
Usage: python rhymer.py 
"""
# Import modules
import sys
import interact
import rhyme_search
import stats_search

# Ensure correct command line usage
if(len(sys.argv) != 1):
    print(__doc__)
    sys.exit(0)

# Initial User prompt
print(interact.WELCOME)
print(interact.HELP)

userInput = ''

# Keep prompting user for input until they want to quit
while True:
    # Update user command
    userInput = ''

    while not userInput:
        userInput = input(interact.PROMPT)
   
    # Parse command, print corresponding response
    parsedCmd = userInput.split()

    # Break from loop if user wants to quit
    if(parsedCmd[interact.CMD_IDX] == interact.COMMANDS[interact.QUIT_IDX]):
        break;

    # Parse user input
    parseResult = interact.commands_to_str(parsedCmd)

    # If not 'rhyme' or 'stats', we already printed what we needed to,
    # or if invalid arg provided (word not set), then reloop
    if (not (parseResult in interact.COMMANDS[:interact.STATS_IDX] and 
             interact.USER_WORD)):
        continue

    # Otherwise, determine what behavior to run
    if parseResult == interact.COMMANDS[interact.RHYME_IDX]:
        # Extract pronunciation
        pronunciations = rhyme_search.word_to_pron(interact.USER_WORD)

        if pronunciations is None:
            continue

        # Retrieve the appropriate rhyming function
        rhyme_search = rhyme_search.rhyme_type_to_func(interact.USER_RHYME_TYPE)

        # For each pronunciation, search for rhymes, printing results
        for i in range(len(pronunciations)):
            rhymes = rhyme_search(pronunciations[i])

            # if none found
            if rhymes == []:
                print(interact.RHYMES_NOT_FOUND.format(interact.USER_RHYME_TYPE,
                        interact.USER_WORD))
                continue

            # otherwise print each rhyme for pronunciation
            print(interact.RHYMES_FOUND.format(interact.USER_RHYME_TYPE,
                    i, interact.USER_WORD, "".join(pronunciations[i])))

            # Print according to number of syllables
            syllable_rhymes = rhyme_search.rhymes_by_syllable(rhymes)

            for j in range(len(syllable_rhymes)):
                print(interact.SYLLALBE_RHYME.format(j), 
                      ", ".join(syllable_rhymes[j]))


    if parseResult == 'stats':
        print(3)

    # Reset user word
    interact.USER_WORD = ''

# Exit Script
print(interact.EXIT)
sys.exit(0)
