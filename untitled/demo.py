# Simon

import random, time

sequence = []

def newattempt():
    sequence.append(str(random.randint(1,4)))

    print("".join(sequence))
    time.sleep(1.5)
    i = 0
    while i < 20:
        print('\n')
        i += 1


def start():
    print('Welcome to Simon\nPlease attempt to reconstruct the following sequence')
    tick = 1
    while True:
        newattempt()
        guess = list(input("PLease enter the sequence: "))
        if guess == seque
            nce:
            print('Correct!\n')
            tick += 1
        else:
            print('Failed!\nYour sequence: '+str("".join(guess))+'\nCorrect Sequence: '+str("".join(sequence)))
            print('You made it to the '+str(tick)+' term in the sequence!')
            break

start()