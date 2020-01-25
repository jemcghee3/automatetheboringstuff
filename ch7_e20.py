import re

number_regex = re.compile(r'[^,\d]((\d{1,3})(,\d{3})*)[^,\d]')

text = '''How would you write a regex that matches a number with commas for every three digits? It must match the following:
 888 
999
'42'
'1,234'
'6,368,745'
but not the following:

'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)
'''

mo = number_regex.findall(text) # this returns a list of strings/tuples
for item in mo:
    print(item[0].strip()) # strip the newline and return only group(0) to get the whole number
