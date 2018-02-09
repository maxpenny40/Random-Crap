# Brute Force Program
# Guesses one letter at a time, not whole string - not applicable to real world scenario

import random, string

def brute():
    word = str(input('Please input a password: '))
    word = list(word)
    totalword = []
    i = 0
    click = 0

    while totalword != word:
        guess = ''
        while word[i] != guess:
            guess = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + ' ', k=1))
            if word[i] == guess:
                totalword.append(guess)
            print(guess)
            click += 1
        i += 1
    """
    guess = ''
    while word != guess:
        guess = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + ' ', k=1))
        print(guess)
    """
    print("\n"+str(click)+"\n")
    print("".join(map(str, totalword)))

brute()

