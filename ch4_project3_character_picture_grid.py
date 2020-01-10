grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# for x in range(len(grid)):
#    for y in range(len(grid[0])):
#        print(grid[x][y])
# this prints it all in a verticle line

# print('This prints it all in a verticle line above this point')

# for x in range(len(grid)):
#    for y in range(len(grid[0])):
#        print(grid[x][y], end='')
# this prints it all in a horizontal line

# print('This prints it all in a horizontal line above this post')

# for x in range(len(grid)):
#    print(grid[x][y], end='')
# this prints what I want to be the bottom row

# print('This prints what I want to be the bottom row')

for y in range(len(grid[0])):
    for x in range(len(grid)):
        print(grid[x][y], end='')
    print('')
# This prints what I want, but as a horizontal line.

print('<3')

# x = 0
# y = 0
# while y < len(grid[0]):
#    while x < (len(grid)):
#        print(grid[x][y], end='')
#        x += 1
#    y += 1
# This prints what I want as the top line.

# print('This prints what I want as the top line.')



