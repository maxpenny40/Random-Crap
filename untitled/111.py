import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
from datetime import timedelta

savingtarget = 200

startday = int(input('When would you like to start saving? \nDay: '))
startmonth = int(input("Month: "))
startyear = int(input('Year: '))
startdatelabel = (str(startmonth)+"/"+str(startday)+"/"+str(startyear))
startdate = dt.date(startyear,startmonth,startday)

targetday = int(input('When would you like to save this by? \nDay: '))
targetmonth = int(input('Month: '))
targetyear = int(input('Year: '))
targetdatelabel = (str(targetmonth)+"/"+str(targetday)+"/"+str(targetyear))
targetdate = dt.date(targetyear, targetmonth, targetday)

alldates = [startdate]
newdate = startdate
while newdate < targetdate:
    newdate += timedelta(weeks = 2)
    alldates.append(newdate)

dfmt = mdates.DateFormatter(' %b %d')

print(startdate, targetdate)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.xaxis.set_major_locator(mdates.DayLocator())
ax.xaxis.set_major_formatter(dfmt)
ax.xaxis.set_minor_locator(mdates.HourLocator())
ax.set_xlim(startdate,targetdate)
ax.plot(startdate,targetdate,linewidth = '2')
fig.set_size_inches(8,4)
plt.show()
