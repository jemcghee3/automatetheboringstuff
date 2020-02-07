#! python3
# mcb.pyw - saves and loads pieces of text to the clipboard.
# Usage: python3 ch9_project3.py save <keyword> - saves clipboard to keyword
#        python3 ch9_project3.py <keyword> - loads keyword to clipboard
#        python3 ch9_project3.py list - loads all keywords to clipboard
#        python3 ch9_project3.py delete <keyword> - removes the keyword from the shelf
#        python3 ch9_project3.py deleteall - removes all keywords from the shelf

'''
Extending the Multi-Clipboard

Extend the multi-clipboard program in this chapter so that it has a delete <keyword> command line argument that will delete a keyword from the shelf. Then add a delete command line argument that will delete all keywords.
'''

import shelve, pyperclip, sys
mcb_shelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    mcb_shelf.pop(str(sys.argv[2]), None)
elif len(sys.argv) == 2:
# List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1].lower() == 'deleteall':
        for key in mcb_shelf.keys():
            del mcb_shelf[key]
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    mcb_shelf.close()
