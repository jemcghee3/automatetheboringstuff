'''
Sandwich Maker
Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:

Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.

'''

import pyinputplus

bread_type = {'wheat':1, 'white':2, 'sourdough':3}
protein_type = {'chicken':3, 'tukey':3, 'ham':2, 'tofu':1}
cheese = ('yes', 'no')
cheese_type = {'cheddar':1, 'swiss':2, 'mozzarella':2}
condiments = ('mayo', 'mustard', 'lettuce', 'tomato', 'done')
condiments_choice = list()
all_condiments = ''

print('Welcome to the Sandwich Maker. What kind of sandwich would you like?')
bread_choice = pyinputplus.inputMenu(list(bread_type.keys()), lettered=True, numbered=False)
print('You have selected a sandwich with %s bread.' % bread_choice)
print('What kind of protein would you ike on your sandwich?')
protein_choice = pyinputplus.inputMenu(list(protein_type.keys()), lettered=True, numbered=False)
print('You have selected a %s sandwich on %s.' % (protein_choice, bread_choice))
print('Would you like cheese on that?')
cheese_yn = pyinputplus.inputYesNo()
if cheese_yn == 'yes':
    print('What kind of cheese would you like?')
    cheese_choice = pyinputplus.inputMenu(list(cheese_type.keys()), lettered=True, numbered=False)
else:
    cheese_choice = 'no'
while True:
    print('What condiments would you like? Select \'done\' when finished.')
    new_condiment = pyinputplus.inputMenu(list(condiments), lettered=True, numbered=False)
    if new_condiment == 'done':
        break
    if new_condiment in condiments_choice:
        continue
    else:
        condiments_choice.append(new_condiment)
if len(condiments_choice) == 0:
    all_condiments = 'nothing'
else:
    all_condiments = ', '.join(condiments_choice)

print('You have chosen a %s sandwich on %s with %s cheese and %s on it.' % (protein_choice, bread_choice, cheese_choice, all_condiments))

price = bread_type[bread_choice] + protein_type[protein_choice] + cheese_type.get(cheese_choice, 0)
print('Your total cost per sandwich is $' + str(price) + '.')
print('How many sandwiches would you like?')
multiple = pyinputplus.inputInt(min=1)
total_price = price * multiple
print('Thank you. Your total is $' + str(total_price) + '.')
