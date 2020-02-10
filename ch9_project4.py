'''
Mad Libs

Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurrences and prompt the user to replace them.

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck

The following text file would then be created:

The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.
'''

from pathlib import Path
import re

madlib_file = open(Path.cwd() / 'madlibs.txt')
madlib_content = madlib_file.read()
mad_words = ('ADJECTIVE', 'NOUN', 'ADVERB', 'VERB')
for item in mad_words:
# Count the number of adjectives, prompt for mad adjectives.
    mad_regex = re.compile(item)
#    print(mad_regex)
    mo = mad_regex.findall(madlib_content) #give the count of the number of the mad word
#    print(mo)
    madlib_content = madlib_content.split(item) # split by the word to make a gap
#    print(madlib_content)
    madlib = list()
    for i in range(len(mo)):
        mad_word = input('Enter a(n) %s:\n' % item.lower())
        madlib.append(mad_word)
#        print(madlib)
        working_set = [madlib_content[0], madlib_content[1]] #there will always be one trailing section to finish the sentence
#        print('Working set: %s' % working_set)
        madlib_content[0] = madlib[i].join(working_set)
#        print('for loop madlib_content: %s ' % madlib_content) 
        del madlib_content[1] # remove the tail that has been joined
#        print('end of for loop madlib_content: %s ' % madlib_content)
    madlib_content = madlib_content[0] # make the single item list into a string
#    print('Madlib_content: %s ' % madlib_content)
print(madlib_content)
save_file = Path('finished_madlibs.txt')
save_file.write_text(madlib_content)
