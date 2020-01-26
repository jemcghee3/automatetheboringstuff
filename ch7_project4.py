'''
Regex Version of the strip() Method
Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.

'''

import re

text = '    This is a test of using regex as a strip method. There are blank spaces before and after this string.    '
print('Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.\n')

print(text)

def replace(any_text):
    removed_characters = input('Please enter the characters you wish to remove from the string, or press to remove blank spaces: ')
    if len(removed_characters) == 0:
        start_empty_regex = re.compile(r'^ +')
        end_empty_regex = re.compile(r' +$')
        any_text = start_empty_regex.sub('', any_text)
        any_text = end_empty_regex.sub('', any_text)
    else:
        strip_regex = re.compile(removed_characters)
        any_text = strip_regex.sub('', any_text)
    print('\nYour text has been modified as follows:')
    print(any_text)    

replace(text)
