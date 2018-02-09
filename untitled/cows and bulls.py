import random
number = []
i = 0

while i < 4:
    number.append(str(random.choice(range(0,9))))
    i += 1

guess = ""
counter = 0

while True:
    n = 0
    bulls = 0
    cows = 0
    if guess == number:
        print('\nYou guessed the correct number!\nAttempts = '+str(counter))
        break
    else:
        guess = str(input('\nPlease enter your guess: '))
        guess = list(guess)
    for x in number:
        if guess[n] == x:
            cows += 1
        elif guess[n] in number:
            bulls += 1
        n += 1
    counter += 1

    print('Cows: '+str(cows)+'  Bulls: '+str(bulls))
