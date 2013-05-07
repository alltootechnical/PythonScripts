########################################################
# Day of the Week Finder
# Written by Brian Guadalupe
# May 4, 2013
# Finds the day of the week given the following:
# m = month (Jan=1 Feb=2...)
# d = date
# y = year
# It also supports dates from the Julian calendar on or
# before October 4, 1582 and dates from the Gregorian
# calendar on or after October 15, 1582.
########################################################

from math import trunc

while True:
    month = input("month? ")
    day = input("day? ")
    year = input("year? ")

    def getDayOfWeek(month, day, year):
        a = trunc((14 - month) / 12)
        y = year - a
        m = month + 12 * a - 2
        if year <= 1582 and month <= 10 and day <= 4:
            d = trunc((5 + day + y + (y/4) + (31*m/12)) % 7)
        else:
            d = trunc((day + y + (y/4) - (y/100) + (y/400) + (31*m/12)) % 7)
        return d

    def nameDayOfWeek(num):
        if num == 0:
            print "It is a Sunday."
        elif num == 1:
            print "It is a Monday."
        elif num == 2:
            print "It is a Tuesday."
        elif num == 3:
            print "It is a Wednesday."
        elif num == 4:
            print "It is a Thursday."
        elif num == 5:
            print "It is a Friday."
        else:
            print "It is a Saturday."

    print nameDayOfWeek(getDayOfWeek(month, day, year))
