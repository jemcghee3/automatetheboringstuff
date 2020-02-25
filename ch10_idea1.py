#! python3
# Add a prefix to the start of the filename.

import re, os, shutil

# Create a regex that matches files.

file_pattern = re.compile(r'''^(.*?) # all text before the extension
        \.              # the period, escaped
        (.*?)$          # the extension
        ''', re.VERBOSE)

# Loop over the fles in the working directory.

for old_filename in os.listdir('.'):
    mo = file_pattern.search(old_filename)

# Skip files without a match.

    if mo == None:
        continue

# Get the different parts of the filename.

    before_part = mo.group(1)
    extension_part = mo.group(2)

# Form the new filename.

    new_filename = 'spam_' + before_part + '.' + extension_part

# Get the full, absolute file paths.

    abs_working_dir = os.path.abspath('.')
    old_filename = os.path.join(abs_working_dir, old_filename)
    new_filename = os.path.join(abs_working_dir, new_filename)

# Rename the files.

    print(f'Renaming "{old_filename}" to "{new_filename}"...')

# shutil.move(old_filename, new_filename) # uncomment after testing
