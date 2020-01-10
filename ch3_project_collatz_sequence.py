def collatz():
    global number
    if number % 2 == 0:
        print(number // 2)
        number = number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        number = 3 * number + 1
    else:
        print('Error!')

while True:
    print('Please enter an integer.')
    try:
        number = int(input())
        break
    except:
        continue

while number != 1:
    collatz()
