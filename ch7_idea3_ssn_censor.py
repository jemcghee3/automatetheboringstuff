# This script removes social security numbers from a document and replaces them with ***-**-****

import pyperclip, re

# build the regex

ssn_regex = re.compile(r'\d{3}-\d{2}-\d{4}') # requires the - between numbers, so won't find regular 10-digit numbers but will miss unhyphenated SSNs.

# copy text from clipboard
text = str(pyperclip.paste())

# are there any social security numbers? used for final print statement.
matches = []
for groups in ssn_regex.findall(text):
    matches.append(groups) # this creates a group full of SSNs

# replace social security numbers with censored version
text = ssn_regex.sub('***-**-****', text)

# output back to clipboard
pyperclip.copy(text)
if len(matches) == 0:
    print('No social security numbers found.')
else:
    print('Redacted version copied to clipboard')

