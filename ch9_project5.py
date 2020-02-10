'''
Regex Search

Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. The results should be printed to the screen.
'''

import re, os
from pathlib import Path

user_regex = input('Please enter a regular expression to search: ')
regex = re.compile(user_regex)
p = Path.cwd() # sets the current directory as the search
for text_file_path_obj in p.glob('*.txt'): # gets a for loop going through the files as a string instead of path object
    text_file = open(text_file_path_obj)
    text_content = text_file.readlines() # makes a list of strings from the file
    mo = False # set a flag for finding a hit in a file
    for line in text_content:
        if len(regex.findall(line)) > 0:
            print(line)
            mo = True
    if mo == True:
        print(text_file_path_obj)

