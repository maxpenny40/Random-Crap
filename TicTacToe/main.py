# Basic 3 in a row game

import sys


def thegrid(grid):
    width = 4
    depth = 3

    for y in range(depth):
        row = []
        for x in range(width):
            row.append('|  ')
        grid.append(row)
        stripped = row
        stripper(stripped)


def stripper(stripped):

    stripped = str(grid)
    stripped = stripped.replace("], [", '\n')
    stripped = stripped.replace('[[', '')
    stripped = stripped.replace(']]', '')
    stripped = stripped.replace("'", '')
    stripped = stripped.replace(',', '')
    print(stripped)


def played():
    i = 0
    x = 0
    while True:
        if i % 2 == 0:
            player = 1
            piece = '| *'

        else:
            player = 2
            piece = '| $'

        try:
            choice = (int(input('\nPlayer ' + str(player) + ' - Please choose a column (1,3) to put your piece into\n'))) - 1

        except:
            print('Please enter a valid value')
            poscheck(choice, piece, rownum)

        if choice < 3 and choice > -1:
            poscheck(choice, piece, rownum)
            i += 1
            x += 1
        else:
            print('Please choose a valid option')


def poscheck(choice, piece, rownum):
    while rownum >= 0:
        if grid[rownum][choice] != '|  ':
            rownum -= 1
            poscheck(choice, piece, rownum)
        else:
            grid[rownum][choice] = piece
            stripped = grid
            stripper(stripped)
        wincheck(grid)
        break
    if rownum == -1:
        print('\nThere is no more space in that column')

def wincheck(grid):
    win = False
    p1 = '| O'
    p2 = '| X'
    if grid[0][0] == p1 and grid[0][1] == p1 and grid[0][2] == p1:
        win = True
    elif grid[1][0] == p1 and grid[1][1] == p1 and grid[1][2] == p1:
        win = True
    elif grid[2][0] == p1 and grid[2][1] == p1 and grid[2][2] == p1:
        win = True
    elif grid[0][0] == p1 and grid[1][0] == p1 and grid[2][0] == p1:
        win = True
    elif grid[1][0] == p1 and grid[1][1] == p1 and grid[1][2] == p1:
        win = True
    elif grid[2][0] == p1 and grid[2][1] == p1 and grid[2][2] == p1:
        win = True
    elif grid[0][0] == p1 and grid[1][1] == p1 and grid[2][2] == p1:
        win = True
    elif grid[0][2] == p1 and grid[1][1] == p1 and grid[2][0] == p1:
        win = True
    elif grid[0][0] == p2 and grid[0][1] == p2 and grid[0][2] == p2:
        win = True
    elif grid[1][0] == p2 and grid[1][1] == p2 and grid[1][2] == p2:
        win = True
    elif grid[2][0] == p2 and grid[2][1] == p2 and grid[2][2] == p2:
        win = True
    elif grid[0][0] == p2 and grid[1][0] == p2 and grid[2][0] == p2:
        win = True
    elif grid[1][0] == p2 and grid[1][1] == p2 and grid[1][2] == p2:
        win = True
    elif grid[2][0] == p2 and grid[2][1] == p2 and grid[2][2] == p2:
        win = True
    elif grid[0][0] == p2 and grid[1][1] == p2 and grid[2][2] == p2:
        win = True
    elif grid[0][2] == p2 and grid[1][1] == p2 and grid[2][0] == p2:
        win = True

    if win == True:
        print('\nYou win!')
        sys.exit()




grid = []
rownum = 2

thegrid(grid)
played()
