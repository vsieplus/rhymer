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
    if(parsedCmd[0] == interact.COMMANDS[interact.QUIT_IDX]):
        break;

    # Parse user input
    parseResult = interact.commands_to_str(parsedCmd)

    # If not 'rhyme' or 'stats', we already printed what we needed to, so reloop
    if not parseResult in ['rhyme', 'stats']:
        continue

    # Otherwise, determine what behavior to run
    if parseResult == 'rhyme':
        print(2) 

    if parseResult == 'stats':
        print(3)

# Exit Script
print(interact.EXIT)
sys.exit(0)
