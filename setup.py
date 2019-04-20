# Author: Ryan Sie
# Filename: setup.py
# Description: Import nltk + Pronunciation dictionary

# Import nltk
import nltk

# Store CMU Pronunciation Entries + Dictionary 
ENTRIES = nltk.corpus.cmudict.entries()
PRON_DICT = nltk.corpus.cmudict.dict()
