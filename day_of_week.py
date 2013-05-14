########################################################
# Day of the Week Finder
# Written by Brian Guadalupe
# May 4, 2013
# Finds the day of the week given the following:
# m = month (Jan=1 Feb=2...)
# d = date
# y = year
#
# It also supports dates from the Julian calendar on or
# before October 4, 1582 and dates from the Gregorian
# calendar on or after October 15, 1582.
# 
# For example:
# python day_of_week.py 3 14 1999
########################################################

import sys
from math import trunc

month = sys.argv[1]
day = sys.argv[2]
year = sys.argv[3]

d = 0

def getDayOfWeek(month, day, year):
    a = trunc((14 - month) / 12)
    y = year - a
    m = month + 12 * a - 2
    if year <= 1582 and month <= 10 and day <= 4:
        d = trunc((5 + day + y + (y/4) + (31*m/12)) % 7)
    else:
        d = trunc((day + y + (y/4) - (y/100) + (y/400) + (31*m/12)) % 7)
    return d


if d == 0:
    print "It is a Sunday."
elif d == 1:
    print "It is a Monday."
elif d == 2:
    print "It is a Tuesday."
elif d == 3:
    print "It is a Wednesday."
elif d == 4:
    print "It is a Thursday."
elif d == 5:
    print "It is a Friday."
else:
    print "It is a Saturday."



