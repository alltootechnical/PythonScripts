########################################################
# 12% VAT Finder
# Written by Brian Guadalupe
# May 5, 2013
# Finds the subtotal and 12% VAT given the total in PhP
# Note: This code is designed for use within the 
# Philippines. Tax computation may vary from area to
# area, so feel free to edit this code to fit
#
# subtotal = total / 1.12 [or total / (1 + tax%)]
# 12%vat = subtotal * 0.12 [or subtotal * tax%]
########################################################

from decimal import *
getcontext().prec = 10 # 2 decimal places are typical

while True:
    total = input("What is the total? ")
    subtotal = Decimal(total) / Decimal(1.12)  # Mom taught me the
    vat = Decimal(subtotal) * Decimal(0.12)    # formula, so yes

    print "Subtotal     " + str(subtotal)
    print "12% VAT       " + str(vat)
    print "------------------------------"
    print "Total        " + str(total)
