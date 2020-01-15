# Table Printer - this program takes a list of lists of strings and displays it in a well-organized table, with each column right-justified. Assumed that all the inner lists will contain the same number of strings.


table_data = [['apples', 'oranges', 'cherris', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]

def print_table(user_table):
    col_widths = [0] * len(user_table)
    list_length = [0] * len(user_table)
    for each_list in user_table:
        longest_string = None
        for each_item in each_list:
            list_length[user_table.index(each_list)] += 1
            if longest_string == None or each_item == user_table[0][0]:
                longest_string = each_item
            elif len(longest_string) < len(each_item):
                longest_string = each_item
        col_widths[user_table.index(each_list)] = len(longest_string)
    for y in range(list_length[0]): # assumption is that all lists are the same length, otherwise this would not work.
        for x in range(len(user_table)):
            print(user_table[x][y].rjust(col_widths[x], ' '), end=' ')
        print('')

print_table(table_data)
