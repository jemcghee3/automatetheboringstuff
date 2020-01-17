# This program finds website URLs that begin with http:// or https://

import pyperclip, re

# define the regex

http_regex = re.compile(r'(http(s)?://)(\w+.\w+)(.\w+)?(.\w+)?') # s is optional character, then one or more word characters

# Find matches in clipboard text.
text = str(pyperclip.paste())


matches = []
for groups in http_regex.findall(text):
    url = ''.join([groups[0], groups[1], groups[2]])
    if groups[3] != '':
        url += groups[3]
    if groups[4] != '':
        url += groups[4]
    matches.append(url)

# Copy results to clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No URLs found.')
