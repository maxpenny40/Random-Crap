import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
from datetime import timedelta

years = mdates.YearLocator()
months = mdates.MonthLocator()
yearsFmt = mdates.DateFormatter('%Y')

fig, ax = plt.subplots()

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)

savingtarget = 200

startday = int(input('When would you like to start saving? \nDay: '))
startmonth = int(input("Month: "))
startyear = int(input('Year: '))
startdate = dt.date(startyear,startmonth,startday)


targetday = int(input('When would you like to save this by? \nDay: '))
targetmonth = int(input('Month: '))
targetyear = int(input('Year: '))
targetdate = dt.date(targetyear, targetmonth, targetday)

ax.plot(startdate, targetdate)
ax.set_xlim(startdate, targetdate)

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)

fig.autofmt_xdate()

plt.show()