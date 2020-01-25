'''
Strong Password Detection
Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.

'''


import re

test_password = input('This program detects strong passwords of eight or more characters, with both upper and lower case, and at least one digit.\nPlease enter a password: ')

# find one of each required character
password_digit_regex = re.compile(r'\d')
password_lowercase_regex = re.compile(r'[a-z]')
password_uppercase_regex = re.compile(r'[A-Z]')
# find the right length of characters
password_length_regex = re.compile(r'.{8,}')

mo_digit = password_digit_regex.search(test_password)
mo_lowercase = password_lowercase_regex.search(test_password)
mo_uppercase = password_uppercase_regex.search(test_password)
mo_length = password_length_regex.search(test_password)

# if the search returns anything, then the value of the variable is not None. If none are none, then the password meets all conditions.

if mo_digit != None and mo_lowercase != None and mo_uppercase != None and mo_length != None:
    print('Your password is strong.')
else:
    print('That\'s a password an idiot would use on his luggage!')
