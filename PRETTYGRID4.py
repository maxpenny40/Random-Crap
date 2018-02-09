#PRETTYPYGAMEGRID

import pygame, random, time
size = 16
pos1 = "\\"
pos2 = "//"

def drawgrid(width,depth):
    grid = []
    for y in range(depth):
        row = []
        for x in range(width):
            if x % 2 == 0:
                row.append(pos1)
            else:
                row.append(pos2)           
        grid.append(row)

    print(grid)
        
def patterncreate(width,depth):
    grid = []
    choice = input('Would you like to run pattern 1, 2, 3, 4 or 5?\n')
    if choice == '1':
        for y in range(depth):
            row = []
            for x in range(width):
                row.append(pos1)
            grid.append(row)
    elif choice == '2':
        create2(width,depth)
    elif choice == '3':
        create3(width,depth)
    elif choice == '4':
        create4(width,depth)


 
"""
def rotate():

def print():

def update():

def tracker():

def striptracker():

def nextpattern():

def ranreplace():
"""
def start():
    width = int(input('Please input the amount of rows in your grid:\n'))
    depth = int(input('Please input the amount of columns in your grid:\n'))

    patterncreate(width,depth)
    
    gridstr = str(grid)
    gridstr = gridstr.replace("], [",'\n')
    gridstr = gridstr.replace('[[' ,'')
    gridstr = gridstr.replace(']]' ,'')
    gridstr = gridstr.replace(', ' ,' ')
    gridstr = gridstr.replace("'" ,'')
    print(gridstr)

    again = input('Would you like to add to your pattern? (y/n):\n').lower()
    if again == 'y':
        start()
    elif again == 'n':
        print('Thanks for using our program')
    else:
        print('Error.')
    

BLUE = (0,191,255)
PURPLE = (255,0,255)

pygame.init()

start()
