"""
40P
2) Get from input two different times in the format dd:hh:mm:ss and print the difference between them in the
received format dd:hh:mm:ss
dd is number of days
hh is number of hours (00-23)
mm is number od minutes (00-59)
ss is number of seconds (00-59)
"""
from datetime import datetime

print("Formatul primit este: 'dd:hh:mm:ss'\n")
form='%j:%H:%M:%S'

time1=input("Introduceti data 1: \n")
time2=input("Introduceti data 2: \n")

time_diff=datetime.strptime(time1,form)-datetime.strptime(time2,form)
x=str(time_diff).replace(" days, ", ":")
print(x)


