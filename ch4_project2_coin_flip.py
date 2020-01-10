# This program flips a coin 10,000 times.
# It then determines what percentage of the coin flips contain a streak of six heads or tails in a row.
# This program includes streaks longer than six to be a 'streak of six' since the instructions are ambiguous. In this case, a streak of seven 'heads' would count as two different streaks of six.

import random
number_of_streaks = 0
set_of_results = []

for experiment_number in range(10000):
# Code that creates a list of 10,000 'heads' or 'tails' values.
    set_of_results.append(random.randint(0,1))
    print('Result ' + str(experiment_number))
    if set_of_results[-7:-1] == [0, 0, 0, 0, 0, 0] or set_of_results[-7:-1] == [1, 1, 1, 1, 1, 1]:
        number_of_streaks += 1
        print('Number of streaks is ' + str(number_of_streaks))

# Code that cheks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: ' + str((number_of_streaks / 100)) + '%')

