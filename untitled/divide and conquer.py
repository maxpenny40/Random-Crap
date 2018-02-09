low = int(input('Please input the lower bound'))
high = int(input('Please enter the upper bound'))

range = [low, high]

decision = ''
num = high/2
while True:
    
    num = round(num, 0)
    print(num)
    decision = input("Please press L if guess > your number,"
                     " H if guess < your number, or 'correct' if this is your number: ")
    if decision == 'L':
        num = num/2
    elif decision == "H":
        num = (num/2)*3
    elif decision == "correct":
        break
    else:
        print('ERROR')
        break