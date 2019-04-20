# Author: Ryan Sie
# Filename: interact.py
# Description: Interaction functionality for rhymer

# Interaction Strings
COMMANDS = ['rhyme', 'stats', 'rhymeTypes', 'rhymeTypes2', 'help', 'quit']
RHYME_IDX = 0
STATS_IDX = 1
RHYME_TYPES_IDX = 2
RHYME_TYPES2_IDX = 3
HELP_IDX = 4
QUIT_IDX = 5

UNRECOGNIZED_COMMAND = "\n\t Unrecognized Command {}.\n"
WRONG_ARGS  = "\n\tCommand {} used with incorrect number of args. (See 'help')\n"
INVALID_TYPE = "\n\tInvalid rhyme type {}\n"


PROMPT = ">> "
WORD_NOT_FOUND = "\n\t Word {} not found.\n"
RHYMES_NOT_FOUND = "\n\t No {} rhymes found for the word {}. :(\n"

CMD_IDX = 0
WORD_IDX = 1
TYPE_IDX = 2

WELCOME = "\nWelcome to Rhymer! It's time to rhyme!"
HELP = """\nUsage:
        \trhyme <word> <type>   : Display rhymes for a word of the given type
        \tstats <word>          : Display overall stats for a word
        \trhymeTypes            : Display different types of rhymes with examples
        \trhymeTypes2           : Display different types of rhymes with examples
        \thelp                  : Display this message
        \tquit                  : Stop rhyming"""
EXIT = "Is it already time? Well thanks for the rhymes!"

# Rhyme Types with examples
TYPES = ['perfect', 'near', 'syllabic', 'semi', 'para', 'assonance',
         'identical', 'eye']
PERFECT_IDX = 0
NEAR_IDX = 1
SYLLABIC_IDX = 2
SEMI_IDX = 3
PARA_IDX = 4
ASSON_IDX = 5
ID_IDX = 6
EYE_IDX = 7

RHYME_TYPES = """\nRhyme Types:\n
'perfect'   - rhyme in which the final stressed vowel + all subsequent
              sounds are identical. Can be classified by # of syllables:\n
\t  'rhyme' ~  'sublime'       [single]
\t  'table' ~  'cable'         [double]
\t'comical' ~  'astronomical'  [dactylic]\n
'near'      - rhyme between an unstressed and stressed syllable\n
\t 'hello'  ~  'yellow'\n
'syllabic'  - rhyme in which final syllables match, but are unstressed\n
\t 'paper'  ~  'lover'\n
'semi'      - rhyme in which one word has an extra syllable at the end\n
\t 'store'  ~  'forecast'"""

RHYME_TYPES2 = """\nMore Rhyme Types:\n
'para'      - rhyme in which all consonants match\n
\t  'love'  ~  'live'\n
'assonance' - all vowels in a word match\n
\t'bottle'  ~  'nozzle'\n
'identical' - perfect rhyme in which the onset of the stressed syllable
              also matches\n
\t 'leave'  ~  'believe\n
'eye'       - a 'spelling' rhyme, where final sounds are spelled 
              identically, but the sounds are not identical\n
\t  'love'  ~  'move'"""

SEARCHING = "\nSearching for {} rhymes of the word {}...\n"
STATS = "\nCalculating stats for the word {}...\n"

# User input variables
USER_WORD = ''
USER_RHYME_TYPE = ''

# Helper function to ensure correct arguments used with 'rhyme' or 'stats'
def parse_word(parsedCmd):
    """ Ensure that correct arguments are used with 'rhyme' and 'stats'"""
    cmd = parsedCmd[CMD_IDX]

    if cmd == COMMANDS[RHYME_IDX]:
        # Check for incorrect args
        if(len(parsedCmd) != 3):
            return WRONG_ARGS.format(cmd)

        # Make sure valid rhyme type given
        if(not parsedCmd[TYPE_IDX] in TYPES):
            return INVALID_TYPE.format(parsedCmd[TYPE_IDX])

        # Otherwise, set word + type and return corresponding string
        USER_WORD = parsedCmd[WORD_IDX]
        USER_RHYME_TYPE = parsedCmd[TYPE_IDX]
        return SEARCHING.format(parsedCmd[TYPE_IDX], parsedCmd[WORD_IDX])
    elif cmd == COMMANDS[STATS_IDX]:
        # Same thing
        if(len(parsedCmd) != 2):
            return WRONG_ARGS.format(cmd)
        
        USER_WORD = parsedCmd[WORD_IDX]
        return STATS.format(parsedCmd[WORD_IDX])

# Switch statement to determine behavior based on user inputted command
# Returns command index of specified command 
def commands_to_str(parsedCmd):    
    """Effective switch statement for parsing user inputted command"""
    switch = {
        COMMANDS[RHYME_IDX]: parse_word(parsedCmd),
        COMMANDS[STATS_IDX]: parse_word(parsedCmd),
        COMMANDS[RHYME_TYPES_IDX]: RHYME_TYPES,
        COMMANDS[RHYME_TYPES2_IDX]: RHYME_TYPES2,
        COMMANDS[HELP_IDX]: HELP,
    }

    print(switch.get(parsedCmd[CMD_IDX], 
                     UNRECOGNIZED_COMMAND.format(parsedCmd[CMD_IDX])))

    return parsedCmd[CMD_IDX]
