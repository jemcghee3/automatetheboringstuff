# this script fixes common typos such as multiples spaces between words, accidentally repeated words, or multiple exclamation marks at the end of sentences.

import pyperclip, re

double_exclaim_regex = re.compile(r'!{2,}') # matches 2 or more !
double_space_regex = re.compile(r' {2,}') #matches 2 or more spaces
double_word_regex = re.compile(r'\b(\w+)\s+\1\b') # matches a word (group 1) followed by group 1 again (i.e. the same word)

# yank from clipboard
text = pyperclip.paste()

text = double_exclaim_regex.sub(r'!', text) # sub one exclamation for multiple instances
text = double_space_regex.sub(r' ', text) # sub one space for multiple spaces
text = double_word_regex.sub(r'\1', text) # sub the word in for both words   
# send to clipboard

pyperclip.copy(text)

print('Text modified to remove double spaces, doubled words, and doubled exclamation marks.')
