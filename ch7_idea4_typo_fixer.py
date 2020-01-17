# this script fixes common typos such as multiples spaces between words, accidentally repeated words, or multiple exclamation marks at the end of sentences.

import pyperclip, re

double_exclaim_regex = re.compile(r'!{2,}') # matches 2 or more !

# yank from clipboard
text = pyperclip.paste()

text = text.split() # breaks string into a list, removes double white spaces.
for n in range(len(text) - 2):
    if text[n] != text[n+1]:
        continue
    text.remove(text[n])
text = ' '.join(text) # this works on unformatted strings but will have issues with new lines

text = double_exclaim_regex.sub(r'!', text) # sub one exclamation for multiple instances

# send to clipboard

pyperclip.copy(text)

print('Text modified to remove double spaces, doubled words, and doubled exclamation marks.')
