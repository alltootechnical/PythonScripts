########################################################
# Hypotenuse Calculator
# Written by Brian Guadalupe
# May 6, 2013
# Calculates the hypotenuse (longest leg) given the
# two other legs
# It uses the Pythagorean Theorem:
#  2    2    2
# a  + b  = c
#        _________
#       / 2    2
# c = \/ a  + b
########################################################

import math

while True:
    a = input("What is the smaller leg? ")
    b = input("What is the longer leg? ")

    def findHypotenuse(a, b):
        c = math.sqrt(a**2 + b**2)
        return c

    c = findHypotenuse(a, b)

    print "     .          ________________"
    print "     |\         | a = " + str(a) 
    print "     | \        | b = " + str(b)
    print "     |  \       "
    print "     |   \                    "
    print "     |    \                   "
    print "     |     \                  "
    print "     |      \  " + str(c)
    print "   b |       \                "
    print "     |        \               "
    print "     |         \              "
    print "     |          \             "
    print "     |_          \            "
    print "     |_|__________\           "
    print "           a"



