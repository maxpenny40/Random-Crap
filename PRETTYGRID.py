#PRETTYGRIDPROJECT V1.0

import random

grid = []

def create(width,depth):
    for y in range(depth):
        row = []
        for x in range(width):
            row.append(random.randint(1,4))       
        grid.append(row)
        print(row)

width = int(input('Please input the amount of rows in your grid:\n'))
depth = int(input('Please input the amount of columns in your grid:\n'))

create(width,depth)

print("\nrandomised!\n")

for rowindex, row in enumerate(grid):
    for cellindex, cellvalue in enumerate(row):
        row[cellindex] = random.randint(1,4)
        #print(grid)
        #print('')
#This changes a cell one by one, and prints each change

n=0
while n < len(grid):
    print(grid[n])
    n += 1



"""
z=0
for index, grid[z] in enumerate(grid[z]):
    grid[index] = 3
    z += 1

print(grid)
"""


gridstr = str(grid)
gridstr = gridstr.replace("], [",'\n')
gridstr = gridstr.replace('[[' ,'')
gridstr = gridstr.replace(']]' ,'')
print(gridstr)


