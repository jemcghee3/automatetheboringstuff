spam = ['apples', 'bananas', 'tofu', 'cats']

for i in range(len(spam) - 1):
    print(spam[i] + ', ', end='')

# This currently prints everything correctly but each list item on its own line.
# Need to move it to one line.

print('and ' + spam[-1])
