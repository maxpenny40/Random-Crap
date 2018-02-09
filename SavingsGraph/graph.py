#Savings Program

#Use each part of date as different row?
#Sort scale
import datetime

grid = []

def makegraph(depthscale, target):
    i = 0
    for y in range(int(target/10)+1):
        row = []
        if y == (int(target/10)+1):
            row.append("  ")
        else:
            row.append('%003d' % y)

        depthscale -= 1
        a = 1
        i += 1

        for x in range(50):
            if y == depthscale:
                row.append(" "+'%02d' % a)
            else:
                if x == 10:
                    row.append('__|')
                elif x == 0:
                    row.append('|__|')
                else:
                    row.append("__|")
            a += 1
        grid.append(row)

    cleangrid(grid)

def cleangrid(grid):
    gridstr = str(grid)
    gridstr = gridstr.replace("], [", '\n')
    gridstr = gridstr.replace('[[', '')
    gridstr = gridstr.replace(']]', '')
    gridstr = gridstr.replace(', ', '')
    gridstr = gridstr.replace("'", '')
    print(gridstr)
def idealcoordinates():
    pass

def actualcoordinates():
    pass

def lineofbestfit():
    pass

def start():
    target = 100
    depthscale = int(target/10)
    print(depthscale)
    makegraph(depthscale,target)
    startday = int(input('When would you like to start saving? \nDay: '))
    startmonth = int(input("Month: "))
    startyear = int(input('Year: '))
    startdate = datetime.date(startyear,startmonth,startday)

    target = float(input("What is your savings goal?: "))

    targetday = int(input('When would you like to save this by? \nDay: '))
    targetmonth = int(input('Month: '))
    targetyear = int(input('Year: '))
    targetdate = datetime.date(targetyear, targetmonth, targetday)
    print(targetdate)

    totallength = (targetdate - startdate).days

    print('You have '+str(totallength)+' days to save £'+str(target))
    totallength = round((totallength/7),2)
    savelength = round((target/totallength), 2)

    print('It will take £'+str(savelength)+' per week to save £'+str(target)+' in '+str(totallength)+'weeks.')

    widthscale = totallength
    depthscale = target/10


    makegraph(depthscale)

def error():
    pass

def save():
    pass

def load():
    pass

start()