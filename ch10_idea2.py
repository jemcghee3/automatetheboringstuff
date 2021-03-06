#! python3
# Renames filenames with European DD-MM-YYYY date format
# to American MM-DD-YYYY.

import re, os, shutil

# Create a regex that matches files with the European date format.

date_pattern = re.compile(r'''^(.*?) # all text before the date
        ((0|1|2|3)?\d)- # one or two digits for the day
        ((0|1)?\d)-     # one or two digits for the month
        ((19|20)\d\d)   # four digits for the year
        (.*?)$          # all text after the date
        ''', re.VERBOSE)

# Loop over the fles in the working directory.

for euro_filename in os.listdir('.'):
    mo = date_pattern.search(euro_filename)

# Skip files without a date.

    if mo == None:
        continue

# Get the different parts of the filename.

    before_part = mo.group(1)
    day_part = mo.group(2)
    month_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

# Form the American-style filename.

    amer_filename = before_part + month_part + '-' + day_part + '-' + year_part + after_part

# Get the full, absolute file paths.

    abs_working_dir = os.path.abspath('.')
    amer_filename = os.path.join(abs_working_dir, amer_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

# Rename the files.

    print(f'Renaming "{euro_filename}" to "{amer_filename}"...')

# shutil.move(euro_filename, amer_filename) # uncomment after testing
