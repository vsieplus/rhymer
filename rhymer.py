# Author: Ryan Sie
# Filename: rhymer.py
# Description: Main script for rhymer program

"""Welcome to Rhymer! A Rhyming dictionary for all your rhyming needs.
   
Usage: python rhymer.py 
"""
# Import modules
import sys
import setup
import interact

# Ensure correct command line usage
if(len(sys.argv) != 1):
    print(__doc__)
    sys.exit(0)

# Setup

# Initial User prompt
print(interact.WELCOME)
print(interact.HELP)

userInput = ''

# Keep prompting user for input until they want to quit
while not userInput is None:
    # Update user command
    userInput = ''

    while not userInput:
        userInput = input(interact.PROMPT)
   
    # Parse command, print corresponding response
    parsedCmd = userInput.split()

    # Break from loop if user wants to quit
    if(parsedCmd[0] == interact.COMMANDS[interact.QUIT_IDX]):
        break;

    print(interact.commands_to_str(parsedCmd))


# Exit Script
print(interact.EXIT)
sys.exit(0)
