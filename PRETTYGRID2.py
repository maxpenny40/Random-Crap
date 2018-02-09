#PRETTYGRID V2

import random

grid = []

pos1 = "\\"
pos2 = "//"


def create1(width,depth):
    for y in range(depth):
        row = []
        for x in range(width):
            if x % 2 == 0:
                row.append(pos1)
            else:
                row.append(pos2)           
        grid.append(row)
        

def create2(width,depth):
    for y in range(depth):
        row = []
        if y % 2 == 0:
            for x in range(width):
                if x % 2 == 0:
                    row.append(pos1)
                else:
                    row.append(pos2)            
            grid.append(row)
        else:
            for x in range(width):
                x += 1
                if x % 2 == 0:
                    row.append(pos1)
                else:
                    row.append(pos2)            
            grid.append(row)

def create3(width,depth):
    for y in range(depth):
        row = []
        if y % 2 == 0:
            for x in range(width):
                row.append(pos1)           
            grid.append(row)
        else:
            for x in range(width):
                  row.append(pos2)           
            grid.append(row)

def create4(width,depth):
    for y in range(depth):
        row = []
        for x in range(width):
            row.append(pos1)           
        grid.append(row)

def create5(width,depth):
    for y in range(depth):
        row = []
        if y % 2 == 0:
            for x in range(width):
                if x % 2 == 0:
                    if grid[x-1] % 2:
                        row.append(pos1)
                    else:
                        pass
                else: #inverse on x axis
                    row.append(pos2)
 
            grid.append(row)
        else: #do inverse on y axis
            for x in range(width):
                x += 1
                if x % 2 == 0:
                    row.append(pos1)
                else:
                    row.append(pos2)            
            grid.append(row)

def start():
    width = int(input('Please input the amount of rows in your grid:\n'))
    depth = int(input('Please input the amount of columns in your grid:\n'))

    choice = input('Would you like to run pattern 1, 2, 3, 4 or 5?\n')
    if choice == '1':
        create1(width,depth)
    elif choice == '2':
        create2(width,depth)
    elif choice == '3':
        create3(width,depth)
    elif choice == '4':
        create4(width,depth)
        
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
    

start()

