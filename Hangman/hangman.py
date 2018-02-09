import pygame, random

pygame.init()

wordlist = ['Guy', 'Dylan', 'Farrer', 'Adam', 'Josh', 'David']

word = random.choice(wordlist)
word.lower()
word = list(word)

totalword = []
for x in word:
    totalword.append('?')



def checker():
    i = 0
    guess = str(input('Please guess a letter: '))
    while i < len(word):
        if word[i] == guess:
            totalword[i] = guess
            print('You have guessed the letter '+str(i+1)+'\n')
            print(totalword)
        else:
            print('fail')
        i += 1
    checker()

checker()