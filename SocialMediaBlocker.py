# Importing Python Libraries
from datetime import datetime as dt
import  time

print(time.localtime(time.time()))

date = dt.now()
if dt(date.year,date.month,date.day,8) < date < dt(date.year,date.month,date.day,18):
    print("I am in Office now, Kindly Call me Later")
else:
    print("Fun Hours")



import calendar
cal = calendar.prcal(2000)

print(cal)