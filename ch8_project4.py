'''
Write Your Own Multiplication Quiz
To see how much PyInputPlus is doing for you, try re-creating the multiplication quiz project on your own without importing it. This program will prompt the user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9. You’ll need to implement the following features:

If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
The user gets three tries to enter the correct answer before the program moves on to the next question.
Eight seconds after first displaying the question, the question is marked as incorrect even if the user enters the correct answer after the 8-second limit.
'''

import random, time

number_of_questions = 10
correct_answers = 0
time_limit = 8

print('This is a multiplication quiz. There are %s questions and you have %s seconds to answer each. You have 3 chances per question.' % (number_of_questions, time_limit))
for questions in range(10):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    tries = 0
    while tries < 3:
        print('What is %s * %s?' % (num1, num2))
        start_time = time.monotonic()
        guess = input()
        tries +=1
        if time.monotonic() - start_time > time_limit:
            print('Sorry, you took longer than %s seconds to answer.' % time_limit)
            time.sleep(1)
            break
        try:
            guess = float(guess) # as float because someone could be wrong and enter a float
        except:
            print('Incorrect!') # if it's not a number, it can't be right
            time.sleep(1)
            continue
        if guess == num1 * num2:
            print('Correct!')
            time.sleep(1) # 1 second before moving on
            correct_answers += 1
            break
        else:
            print('Incorrect!')
            time.sleep(1)
            continue

print('You got %s out of %s correct.' % (correct_answers, number_of_questions))
