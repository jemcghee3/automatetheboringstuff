# This script cleans up dates in different American formats MM-DD-YYYY and puts them in a European format of DD-MM-YYYY

import pyperclip, re

# build a regex search

date_regex = re.compile(r'''(
        (\d{1,2})        # finds 1 or 2 numbers. group[0] will be months
        (-|/|\.)         # finds - / and . as separators. space is intentionall excluded
        (\d{1,2})        # finds 1 or 2 numbers. group[3] will be days
        (-|/|\.)         # another seperator
        (\d{2,4})        # two digit or four digit year
        )''', re.VERBOSE)

# Find matches in clipboard text
text = pyperclip.paste()

matches = []
for groups in date_regex.findall(text):
    eu_date = '.'.join([groups[3],groups[1],groups[5]]) # reorders the dates to eu standard
    matches.append(eu_date)

# Copy matches to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard.')
    print('n'.join(matches))
else:
    print('No addresses found found.')
