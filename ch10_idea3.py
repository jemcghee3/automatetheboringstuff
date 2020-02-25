#! python3
# Remove the zeros from files such as spam0042.txt

import re, os, shutil

# Create a regex that matches files.

file_pattern = re.compile(r'''^(.*?) # all text before zeros
        (0+)            # the zero piece
        (\d+)           # digits, one or more times
        \.              # the period, to catch the numbers at the end of the file name
        (.*?)$          # all text afterwards
        ''', re.VERBOSE)

# Loop over the fles in the working directory.

for old_filename in os.listdir('.'):
    mo = file_pattern.search(old_filename)

# Skip files without a match.

    if mo == None:
        continue

# Get the different parts of the filename.

    before_part = mo.group(1)
    zeros   = mo.group(2)   # not used in rebuilding file name!
    digit_part = mo.group(3)
    end_part = mo.group(4)

# Form the new filename.

    new_filename = before_part + digit_part + '.' + end_part

# Get the full, absolute file paths.

    abs_working_dir = os.path.abspath('.')
    old_filename = os.path.join(abs_working_dir, old_filename)
    new_filename = os.path.join(abs_working_dir, new_filename)

# Rename the files.

    print(f'Renaming "{old_filename}" to "{new_filename}"...')

# shutil.move(old_filename, new_filename) # uncomment after testing
