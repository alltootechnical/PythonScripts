#!/usr/bin/python
# -*- coding: utf-8 -*-
# Triangle Utility Pack
#
# 68 functions defined
# 
# "Not yet final!" -Brian

from __future__ import division
import math
import cmath # we'll use this later
from fractions import gcd # ditto

print "Triangle Utility Pack v0.7b (Jan03)"
print "Written by Brian Guadalupe"
print "Started in December 18, 2013"

print "\nLoading..."

# declare functions to be used
    
def sin(x):
    return math.sin(x)
    
def cos(x):
    return math.cos(x)
    
def tan(x):
    return math.tan(x)

def asin(x):
    return math.asin(x)

def acos(x):
    return math.acos(x)

def atan(x):
    return math.atan(x)
    
def rad(x):
    return math.radians(x)
    
def deg(x):
    return math.degrees(x)

def sqrt(x):
    return math.sqrt(x)

def floor(x):
    return math.floor(x)

def getFactorPairs(val):
    return [(i, int (val / i)) for i in range (1, int (val ** 0.5) + 1) if val % i == 0]

def isPrime(p):
  if p == 2:
      return True 
  elif p <= 1 or p % 2 == 0:
      return False
  else:
    for i in range(3, int(sqrt(p))+1, 2): 
      if p % i == 0: return False
    return True

def C(n, k):
    f = math.factorial
    return f(n)/(f(k)*f(n-k))

def isolve(a,b,c):
    q, r = divmod(a,b)
    if r == 0:
        return ([0, int (c/b)])
    else:
        sol = isolve(b, r, c)
        u = sol[0]
        v = sol[1]
        return ([v, u - q*v])

def simpson(f,a,b,n):         # for integration
    A = 0
    if n % 2 == 1:
        n = n + 1
    h = float(b-a)/n
    A = f(a) + f(b)
    x = a
    i = 1
    while i < n:
        x = x + h
        if i % 2 == 1:
            A = A + 4*f(x)
        else:
            A = A + 2*f(x)
        i = i + 1
    return A*h/3


def dfn(f):
    def df (x, h=0.1e-5):
        return (f(x+h/2) - f(x-h/2))/h
    return df

# for linear congruence solver

def eulerphi(n):
    tot, pos = 0, n-1
    while pos > 0:
        if gcd(pos,n)==1: tot += 1
        pos -= 1
    return tot

def mod(a,b):    # modulo function that works with negative numbers           
    return ((a%b)+b)%b

def gcdext(p,q):  # extended Euclidean algorithm
    if q == 0:
        return [p,1,0]

    vals = gcdext(q, mod(p,q))
    d = vals[0]
    a = int(vals[2])
    b = int(vals[1] - vals[2]*floor(p/q))

    return [d,a,b]
 
def divides(a,b):
    if a % b > 0:
        return False
    return True

def lincongr(a,b,m):
    a = mod(a,m)
    b = mod(b,m)
    m = abs(m)
    
    res = gcdext(a,m)
    solutions = list()
    
    if not divides(b,res[0]):
        return solutions

    sln1 = mod((res[1]*(b/res[0])),m)
    slnn = 0

    for i in range(0,res[0]):
        slnn = mod((sln1 + i*(m/res[0])),m)
        solutions.append(int(slnn))
        solutions.sort()

    return solutions

# determinants

def det22(a, b, c, d):
    return a*d - b*c

def det33(a, b, c, d, e, f, g, h, i):
    return a*det22(e, f, h, i) - b*det22(d, f, g, i) + c*det22(d, e, g, h)

def det44(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
    return a*det33(f, g, h, j, k, l, n, o, p) - b*det33(e, g, h, i, k, l, m, o, p) + c*det33(e, f, h, i, j, l, m, n, p) - d*det33(e, f, g, i, j, k, m, n, o)

def det55(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y):
    return a*det44(g, h, i, j, l, m, n, o, q, r, s, t, v, w, x, y) - b*det44(f, h, i, j, k, m, n, o, p, r, s, t, u, w, x, y) + c*det44(f, g, i, j, k, l, n, o, p, q, s, t, u, v, x, y) - d*det44(f, g, h, j, k, l, m, o, p, q, r, t, u, v, w, y) + e*det44(f, g, h, i, k, l, m, n, p, q, r, s, u, v, w, x)

print "All functions loaded!"
print "\nTRIANGLE UTILITY PACK"
print "====================="

# main program

def tripack():
    print "\nChoices:"
    print "[1] any triangle solver"
    print "[2] right triangle solver"
    print "[3] 30-60-90 side finder"
    print "[4] 45-45-90 side finder"
    print "[5] area of a triangle"
    print "[6] Pythagorean triples"
    print "[7] ----------"
    print "[8] special tools"
    print "[9] about"
    print "[0] exit"
    menu0 = input ("Choose one: ")   
    menu1_opts = {}

    
    # actual subroutines

    def trisolve():
        aA = 0
        aB = 0
        aC = 0
        sa = 0
        sb = 0
        sc = 0
        sa2 = 0
        sb2 = 0
        sc2 = 0
        aA2 = 0
        aB2 = 0
        aC2 = 0
        
        print "\nANY TRIANGLE SOLVER"
        print "Choices:"
        print "[1] three sides"
        print "[2] two sides and the included angle"
        print "[3] two sides and a non-included angle"
        print "[4] two angles and the included side"
        print "[5] two angles and a non-included side"
        print "[6] three angles"
        print "[0] return to previous menu"
        menu_01 = input ("Choose one: ")

        menu_01opts = {}

        def sss():
            print "\nGiven:"
            sa = input ("side a? ")
            sb = input ("side b? ")
            sc = input ("side c? ")
            
            aA = deg ( acos((sb**2 + sc**2 - sa**2) / (2 * sb * sc)))
            aB = deg ( acos((sc**2 + sa**2 - sb**2) / (2 * sa * sc)))
            aC = 180 - (aA + aB)

            print "\nResults:"
            print ("angle A = " + str (aA) + " degrees")
            print ("angle B = " + str (aB) + " degrees")
            print ("angle C = " + str (aC) + " degrees")
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

        def sas():
            print "\nGiven:"
            sa = input ("side a? ")
            sb = input ("side b? ")
            aA = input ("included angle? ")
            
            sc = sqrt (sa**2 + sb**2 - (2 * sa * sb * cos (rad (aA))))
            aB = deg (asin ((sin (rad (aA)) * sa) / sc))
            aC = 180 - (aA + aB)

            print "\nResults:"
            print ("angle A = " + str (aB) + " degrees")
            print ("angle B = " + str (aC) + " degrees")
            print ("side c = " + str (sc))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

        def ssa():
            print "\nGiven:"
            sb = input ("side b? ")
            sc = input ("side c? ")
            aB = input ("a non-included angle? ")

            aC = deg (asin ((sc * (sin (rad (aB)))) / sb))
            aA = 180 - (aB + aC)
            sa = (sin (rad (aA)) * sb) / (sin (rad (aB)))

            aC2 = 180 - aC
            aA2 = 180 - (aB + aC2)
            sa2 = (sin (rad (aA2)) * sb) / (sin (rad (aB)))

            print "\nTwo possible results:"
            print ("angle A = " + str (aA) + " degrees")
            print ("angle C = " + str (aC) + " degrees")
            print ("side a = " + str (sa))
            print "         and         "
            print ("angle A = " + str (aA2) + " degrees")
            print ("angle C = " + str (aC2) + " degrees")
            print ("side a = " + str (sa2))
            print "\nNote: Check out preview.tinyurl.com/WhyTwoAnswers for the explanation."
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

        def asa():
            print "\nGiven:"
            aA = input ("angle A? ")
            aB = input ("angle B? ")
            sc = input ("included side? ")
            
            aC = 180 - (aA + aB)
            sa = (sc * sin (rad (aA))) / (sin (rad (aC)))
            sb = (sc * sin (rad (aB))) / (sin (rad (aC)))

            print "\nResults:"
            print ("angle C = " + str (aC) + " degrees")
            print ("side a = " + str (sa))
            print ("side b = " + str (sb))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

        def aas():
            print "\nGiven:"
            aA = input ("angle A? ")
            aC = input ("angle C? ")
            sb = input ("a non-included side? ")
            
            aB = 180 - (aA + aC)
            sa = (sc * sin (rad (aA))) / (sin (rad (aC)))
            sb = (sc * sin (rad (aB))) / (sin (rad (aC)))

            print "\nResults:"
            print ("angle B = " + str (aB) + " degrees")
            print ("side a = " + str (sa))
            print ("side b = " + str (sb))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

        def aaa():
            print "\nAn AAA triangle is impossible to solve further"
            print "since there are no given sides to show us size..."
            print "We know the shape but not how big it is."

            print "\nYou are going to need to know at least one side"
            print "to proceed further... sorry!"
            
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

        menu_01opts = {1 : sss, 2 : sas, 3 : ssa, 4 : asa, 5 : aas, 6 : aaa, 0 : tripack}

        menu_01opts[menu_01]()
        
    def rtsolvr():
        print "\nRIGHT TRIANGLE SOLVER\nChoices:"
        print "[1] angle A & side a"
        print "[2] angle A & side b"
        print "[3] angle A & side c"
        print "[4] side a & side c"
        print "[5] side a & side b"
        print "[0] return to previous menu"
        menu_1 = input ("Choose one: ")
        
    
        def aasa():
            aB = 0
            sb = 0
            sc = 0
    
            print "\nGiven:"
            aA = input ("angle A? ")
            sa = input ("side a? ")
            
            aB = 90 - aA
            sb = sa / tan (rad (aA))
            sc = sa / sin (rad (aA))
            
            print "\nResults:"
            print ("angle B = " + str (aB) + " degrees")
            print ("side b = " + str (sb))
            print ("side c = " + str (sc))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()
            
        def aasb():
            aB = 0
            sa = 0
            sc = 0
            
            print "\nGiven:"
            aA = input ("angle A? ")
            sb = input ("side b? ")
            
            aB = 90 - aA
            sa = sb * tan (rad (aA))
            sc = sb / cos (rad (aA))
        	
            print "\nResults:"
            print ("angle B = " + str (aB) + " degrees")
            print ("side a = " + str (sa))
            print ("side c = " + str (sc))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()
            
        def aasc():
            aB = 0
            sa = 0
            sb = 0
            
            print "\nGiven:"
            aA = input ("angle A? ")
            sc = input ("side c? ")
            
            aB = 90 - aA
            sa = sc * sin (rad (aA))
            sb = sc * cos (rad (aA))
            
            print "\nResults:"
            print ("angle B = " + str (aB) + " degrees")
            print ("side a = " + str (sa))
            print ("side b = " + str (sb))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()
            
        def sasc():
            aA = 0
            aB = 0
            sb = 0
    
            print "\nGiven:"
            sa = input ("side a? ")
            sc = input ("side c? ")
            
            
            aA = deg (asin (sa / sc))
            aB = 90 - aA
            sb = sqrt (sc**2 - sa**2)
            
            print "\nResults:"
            print ("angle A = " + str (aA) + " degrees")
            print ("angle B = " + str (aB) + " degrees")
            print ("side b = " + str (sb))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()
            
        def sasb():
            aA = 0
            aB = 0
            sc = 0
            
            print "\nGiven:"
            sa = input ("side a? ")
            sb = input ("side b? ")
            
            
            aA = deg (atan (sa / sb))
            aB = 90 - aA
            sc = sqrt (sa**2 + sb**2)
            
            print "\nResults:"
            print ("angle A = " + str (aA) + " degrees")
            print ("angle B = " + str (aB) + " degrees")
            print ("side c = " + str (sc))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()
    
        if menu_1 == 1:
            aasa()
        elif menu_1 == 2:
            aasb()
        elif menu_1 == 3:
            aasc()
        elif menu_1 == 4:
            sasc()
        elif menu_1 == 5:
            sasb()
        elif menu_1 == 0:
            tripack()
    
    
    def tsnsf():
        print "\n30-60-90 SIDE FINDER"
        print "Choices:"
        print "[1] angle A = 30 degrees"
        print "[2] angle A = 60 degrees"
        print "[0] return to previous menu"
        menu2 = input ("Choose one: ")
        
        def thirty():
            print "\nGiven:"
            print "[1] side a"
            print "[2] side b"
            print "[3] side c"
            print "[0] return to previous menu"
            menu21 = input ("Choose one: ")
            
            def thirty_a():
                sa = input ("\nside a? ")
                
                sb = 0
                sc = 0
                
                sb = sa * sqrt (3)
                sc = 2 * sa
                
                print "\nResults:"
                print ("side b = " + str (sb))
                print ("side c = " + str (sc))
                inp = raw_input ("\nPress [Enter] to go back")

                if inp == "":
                    tripack()
                
            def thirty_b():
                sb = input ("\nside b? ")
                
                sa = 0
                sc = 0
                
                sa = sb * (sqrt (3) / 3)
                sc = sb * (2 * sqrt (3) / 3)
                
                print "\nResults:"
                print ("side a = " + str (sa))
                print ("side c = " + str (sc))
                inp = raw_input ("\nPress [Enter] to go back")

                if inp == "":
                    tripack()
                
            def thirty_c():
                sc = input ("\nside c? ")
                
                sa = 0
                sb = 0
                
                sa = sc / 2
                sb = sc * (sqrt (3) / 2)
                
                print "\nResults:"
                print ("side a = " + str (sa))
                print ("side b = " + str (sb))
                inp = raw_input ("\nPress [Enter] to go back")

                if inp == "":
                    tripack()
            
            if menu21 == 1:
                thirty_a()
            elif menu21 == 2:
                thirty_b()
            elif menu21 == 3:
                thirty_c()
            elif menu21 == 0:
                tsnsf()
        
        def sixty():
            print "\nGiven:"
            print "[1] side a"
            print "[2] side b"
            print "[3] side c"
            print "[0] return to previous menu"
            menu22 = input ("Choose one: ")
            
            def sixty_a():
                sa = input ("\nside a? ")
                
                sb = 0
                sc = 0
                
                sb = sa * (sqrt (3) / 3)
                sc = sa * (2 * sqrt (3) / 3)
                                
                print "\nResults:"
                print ("side b = " + str (sb))
                print ("side c = " + str (sc))
                inp = raw_input ("\nPress [Enter] to go back")

                if inp == "":
                    tripack()
                
            def sixty_b():
                sb = input ("\nside b? ")
                
                sa = 0
                sc = 0
                
                sa = sb * sqrt (3)
                sc = 2 * sb
                
                print "\nResults:"
                print ("side a = " + str (sa))
                print ("side c = " + str (sc))
                inp = raw_input ("\nPress [Enter] to go back")

                if inp == "":
                    tripack()
                
            def sixty_c():
                sc = input ("\nside c? ")
                
                sa = 0
                sb = 0
                
                sa = sc * (sqrt (3) / 2)
                sb = sc / 2
                                
                print "\nResults:"
                print ("side a = " + str (sa))
                print ("side b = " + str (sb))
                inp = raw_input ("\nPress [Enter] to go back")

                if inp == "":
                    tripack()
                
            if menu22 == 1:
                sixty_a()
            elif menu22 == 2:
                sixty_b()
            elif menu22 == 3:
                sixty_c()
            elif menu22 == 0:
                tsnsf()
        
        if menu2 == 1:
            thirty()
        elif menu2 == 2:
            sixty()
        elif menu2 == 0:
            tripack()
        
    def ffnsf():
        print "\nGiven:"
        print "[1] side a"
        print "[2] side b"
        print "[3] side c"
        print "[0] return to previous menu"
        menu3 = input ("Choose one: ")
        
        def fortyfive_a():
            sa = input ("\nside a? ")
            
            sb = 0
            sc = 0
            
            sb = sa 
            sc = sa * (sqrt (2))
                            
            print "\nResults:"
            print ("side b = " + str (sb))
            print ("side c = " + str (sc))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

            
        def fortyfive_b():
            sb = input ("\nside b? ")
            
            sa = 0
            sc = 0
            
            sa = sb
            sc = sb * (sqrt (2))
            
            print "\nResults:"
            print ("side a = " + str (sa))
            print ("side c = " + str (sc))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

            
        def fortyfive_c():
            sc = input ("\nside c? ")
            
            sa = 0
            sb = 0
            
            sa = sc / (sqrt (2))
            sb = sa
                            
            print "\nResults:"
            print ("side a = " + str (sa))
            print ("side b = " + str (sb))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

        
        if menu3 == 1:
            fortyfive_a()
        elif menu3 == 2:
            fortyfive_b()
        elif menu3 == 3:
            fortyfive_c()
        elif menu3 == 0:
            tripack()
    
    def area():
        print "\nAREA OF A TRIANGLE"
        print "Choices:"
        print "[1] base and altitude"
        print "[2] two sides and the included angle"
        print "[3] three sides"
        print "[4] two angles and a side"
        print "[5] a side / equilateral"
        print "[6] semiperimeter and inradius"
        print "[0] return to previous menu"
        menu4 = input ("Choose one: ")
        
        def theusual():
            print "\nGiven:"
            base = input ("base?")
            alt = input ("altitude?")
            
            area = 0
            
            area = (1 / 2) * base * alt
            
            print "\nResult:"
            print ("area = " + str (area))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()
                
        def withtrig():
            print "\nGiven:"
            side1 = input ("first side? ")
            side2 = input ("second side? ")
            angle = input ("included angle? ")
            
            area = 0
            
            area = (1 / 2) * side1 * side2 * sin (rad (angle))
            
            print "\nResult:"
            print ("area = " + str (area))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()
        
        def herons():
            print "\nGiven:"
            side1 = input ("first side? ")
            side2 = input ("second side? ")
            side3 = input ("third side? ")
            
            s = 0
            area = 0
            
            s = (side1 + side2 + side3) / 2
            area = sqrt (s * (s - side1) * (s - side2) * (s - side3))
            
            print "\nResult:"
            print ("area = " + str (area))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()
        
        def evenmoretrig():
            print "\nGiven:"
            angle1 = input ("first angle? ")
            angle2 = input ("second angle? ")
            side = input ("a side? ")
            
            area = 0
            angle3 = 0
            
            angle3 = 180 - (angle1 + angle2)
            area = (side**2 * sin (rad (angle2)) * sin (rad (angle3))) / (2 * sin (rad (angle1)))
            
            print "\nResult:"
            print ("area = " + str (area))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()
            
        def oneside():
            print "\nGiven"
            side = input ("side? ")
            
            area = 0
            
            area = (sqrt (3) / 4) * side ** 2
            
            print "\nResult:"
            print ("area = " + str (area))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()
        
        def spandir():
            print "\nGiven"
            sper = input ("semiperimeter?")
            inrad = input ("inradius?")
            
            area = 0
            
            area = sper * inrad
            
            print "\nResult:"
            print ("area = " + str (area))
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()
            
        
        if menu4 == 1:
            theusual()
        elif menu4 == 2:
            withtrig()
        elif menu4 == 3:
            herons()
        elif menu4 == 4:
            evenmoretrig()
        elif menu4 == 5:
            oneside()
        elif menu4 == 6:
            spandir()
        elif menu4 == 0:
            tripack()

    def pythtriples():
        print "\nPYTHAGOREAN TRIPLES"
        print "Choices:"
        print "[1] check if Pythagorean triple"
        print "[2] generate triple given a side"
        print "[0] return to the previous menu"
        menu6 = input ("Choose one: ")

        def checktriple():
            print "\nGiven:"
            a = input ("side a? ")
            b = input ("side b? ")
            c = input ("side c? ")

            if c == sqrt (a**2 + b**2):
                print "\nIt's a Pythagorean triple!"
            else:
                print "\nNope, not a Pythagorean triple..."

            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

        def gettriple():
            a = 0
            b = 0
            c = 0
            factpairs = []
            n = 0
            
            print "\nGiven:"
            sb = input ("a side? ")

            if sb % 2 == 0:
                b = sb / 2
                factpairs = getFactorPairs (b)

                if len (factpairs) == 1:
                    print "\nThere is a possible triple:"
                    
                else:
                    print "\nThere are " + str (len (factpairs)) + " possible triples:"

                for n in range (0, len (factpairs)):
                
                    fp1 = [int (i[0]) for i in factpairs][n]
                    fp2 = [int (i[1]) for i in factpairs][n]

                    a = (fp2**2 - fp1**2)
                    c = (fp2**2 + fp1**2)

                    print ("a = " + str (a) + "  b = " + str (sb) + "  c = " + str (c))

                inp = raw_input ("\nPress [Enter] to go back")

                if inp == "":
                    tripack()

            elif sb % 2 == 1:
                factpairs = getFactorPairs (sb)

                if len (factpairs) == 1:
                    print "\nThere is a possible triple:"
                    
                else:
                    print "\nThere are " + str (len (factpairs)) + " possible triples:"
        

                for n in range (0, len (factpairs)):
                
                    fp1 = [int (i[0]) for i in factpairs][n]
                    fp2 = [int (i[1]) for i in factpairs][n]

                    a = int (((fp2**2) / 2 - (fp1**2)  / 2))
                    c = int (((fp2**2) / 2 + (fp1**2)  / 2))

                    print ("a = " + str (a) + "  b = " + str (sb) + "  c = " + str (c))

                inp = raw_input ("\nPress [Enter] to go back")

                if inp == "":
                    tripack()

        if menu6 == 1:
            checktriple()
        elif menu6 == 2:
            gettriple()
        elif menu6 == 0:
            tripack()

    def menu7():
        print "\nHi there!"
        print "Stay tuned for the next update!"

        inp = raw_input ("\nPress [Enter] to go back")

        if inp == "":
            tripack()


    def spectools():
        print "\nSPECIAL TOOLS"
        print "Choices:"
        print "[1] Diophantine equation solver"
        print "[2] check if prime number"
        print "[3] get factor pairs"
        print "[4] linear congruence solver"
        print "[5] quadratic equation solver"
        print "[6] numerical integration"
        print "[7] numerical differentiation"
        print "[8] systems of equations solver"
        print "[0] return to the previous menu"
        menu8 = input ("Choose one: ")

        menu8_opts = {}

        def ldesolve():
            print "\nGiven: \nax + by = c"
            a = input ("\na? ")
            b = input ("b? ")
            c = input ("c? ")

            x0, y0 = 0, 0

            sln = isolve (a, b, c)
            x0 = sln[0]
            y0 = sln[1]

            d = gcd (a, b)

            if x0 > 0:
                 xn = str (int (b/d)) + "n + " + str (x0)
            elif x0 == 0:
                 xn = str (int (b/d)) + "n"
            elif x0 < 0:
                 xn = str (int (b/d)) + "n - " + str (abs (x0))
                 
            if y0 > 0:
                 yn = str (int (-a/d)) + "n + " + str (y0)
            elif y0 == 0:
                 yn = str (int (-a/d)) + "n"
            elif y0 < 0:
                 yn = str (int (-a/d)) + "n - " + str (abs (y0))
                        
            print "\nParticular solution:"
            print "x0 = " + str (x0)
            print "y0 = " + str (y0)
            
            print "\nGeneral solution:"
            print "x = " + xn
            print "y = " + yn
            

            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

        def primecheck():
            num = input ("\ninteger? ")

            print "\nResult:"

            if isPrime(num) == True:
                print "It is a prime!"
            else:
                print "Nope, not a prime..."

            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

        def fpairs():
            num = input ("\ninteger? ")

            fplist = getFactorPairs (num)

            if len (fplist) == 1:
                    print "\nThere is a factor pair:"
                    
            else:
                print "\nThere are " + str (len (fplist)) + " factor pairs:"

            for i in range (0, len (fplist)):
                print (str (fplist[i]))
                
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

        def lcsolve():
            print "\nGiven: \nax == b (mod n)"
            a = input ("\na? ")
            b = input ("b? ")
            n = input ("n? ")

            k = lincongr (a, b, n)
            g = gcd (a, n)
            t = eulerphi (int (n/g))

            print "\nResult:"
            if len(k) == 0:
                print "No solutions found"
            elif g >= 1 and k > 0:
                print "x == " + str (k)
            
            
            print "gcd(" + str (a) + ", " + str (n) + ") = " + str (g)
            print "phi(" + str (int (n/g)) + ") = " + str (t)
                       

            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

        def quad():
            x1 = 0
            x2 = 0

            area = 0
            xcor = 0
            ycor = 0
            yint = 0
            delta = 0
            rsum = 0
            rprod = 0
            xlst = []
            vert = ()
            
            print "\nGiven:"
            print "ax^2 + bx + c = 0"

            a = input ("\na? ")
            b = input ("b? ")
            c = input ("c? ")

        
            delta = b**2 - 4*a*c
            if delta >= 0:
                x1 = (-b + sqrt (delta)) / 2*a
                x2 = (-b - sqrt (delta)) / 2*a
            elif delta < 0:
                x1 = (-b + cmath.sqrt (delta)) / 2*a
                x2 = (-b - cmath.sqrt (delta)) / 2*a
            xlst = [x1, x2]
            xcor = -b / 2*a
            ycor = a*(xcor**2) + b*xcor +c
            vert = (xcor, ycor)
            rsum = -b / a
            rprod = c / a
            
            area = ((a * x2**3) / 3 + (b * x2**2) / 2 + c * x2) - ((a * x1**3) / 3 + (b * x1**2) / 2 + c * x1)

            print "\nResult:"

            if delta == 0:
                print ("root = " + str (x1))
            else:
                print ("roots = " + str (xlst))
            
            if delta > 0:
                print ("discriminant = " + str (delta) + " (two real roots)")
            elif delta == 0:
                print ("discriminant = " + str (delta) + " (one real root)")
            elif delta < 0:
                print ("discriminant = " + str (delta) + " (two complex roots)")
                
            print ("vertex = " + str (vert))
            print ("sum of roots = " + str (rsum))
            print ("product of roots = " + str (rprod))
            print ("axis of symmetry: x = " + str (xcor))

            if delta >= 0:
                print ("area w.r.t. x-axis = " + str (area))
            elif delta < 0:
                print ("area w.r.t. x-axis = not applicable")

            if a > 0:
                print ("opening of parabola: upwards")
            elif a == 0:
                print ("opening of parabola: not applicable / linear graph")
            elif a < 0:
                print ("opening of parabola: downwards")

            if a > 0:
                print ("minimum value: " + str (ycor) + " at x = " + str (xcor))
            elif a < 0:
                print ("maximum value: " + str (ycor) + " at x = " + str (xcor))

            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

        def integrate():
            print "\nGiven:"
            fn = input ("function? (enter as lambda) ")
            a = input ("lower limit? ")
            b = input ("upper limit? ")
            n = raw_input ("tolerance? ([Enter] for default value) ")

            if n == "":
                n = 10**6

            res = simpson (fn, a, b, n)

            print "\nResult:"
            print "int(f(x)) dx = " + str (res)
        
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

        def derive():
            print "\nGiven:"
            fn = input ("function? (enter as lambda) ")
            x = input ("value? ")
            h = raw_input ("tolerance? ([Enter] for default value) ")

            if h == "":
                h = 1e-5
            else:
                h = float (h)
               
            fnprime = dfn (fn, h)   

            res = fnprime (x)

            print "\nResult:"
            print " d(f(x))"
            print "--------- = " + str (res)
            print "   dx"

      
            inp = raw_input ("\nPress [Enter] to go back")

            if inp == "":
                tripack()

        def syseq():
            print "\nHow many unknowns?"
            print "[2] ax + by = c"
            print "[3] ax + by + cz = d"
            print "[4] ax + by + cz + dw = e"
            print "[5] ax + by + cz + dw + et = f"
            print "[0] return to the previous menu"
            menu88 = input ("Choose one: ")
            menu88_opts = {}

                       
            def xy():
                print "\nGiven:"
                print "[ a1x + b1y = c1"
                print "[ a2x + b2y = c2"

                a1 = input ("\na1? ")
                b1 = input ("b1? ")
                c1 = input ("c1? ")
                
                a2 = input ("\na2? ")
                b2 = input ("b2? ")
                c2 = input ("c2? ")

                
                detA = det22 (a1, b1, a2, b2)

                detx = det22 (c1, b1, c2, b2)
                dety = det22 (a1, c1, a2, c2)

                x = detx / detA
                y = dety / detA

                print "\nResult:"
                print "x = " + str (x)
                print "y = " + str (y)
            
                inp = raw_input ("\nPress [Enter] to go back")

                if inp == "":
                    tripack()

            def xyz():
                print "\nGiven:"
                print "[ a1x + b1y + c1z = d1"
                print "| a2x + b2y + c2z = d2"
                print "[ a3x + b3y + c3z = d3"

                a1 = input ("\na1? ")
                b1 = input ("b1? ")
                c1 = input ("c1? ")
                d1 = input ("d1? ")
                
                a2 = input ("\na2? ")
                b2 = input ("b2? ")
                c2 = input ("c2? ")
                d2 = input ("d2? ")
                
                a3 = input ("\na3? ")
                b3 = input ("b3? ")
                c3 = input ("c3? ")
                d3 = input ("d3? ")
                
                detA = det33 (a1, b1, c1, a2, b2, c2, a3, b3, c3)

                detx = det33 (d1, b1, c1, d2, b2, c2, d3, b3, c3)
                dety = det33 (a1, d1, c1, a2, d2, c2, a3, d3, c3)
                detz = det33 (a1, b1, d1, a2, b2, d2, a3, b3, d3)

                x = detx / detA
                y = dety / detA
                z = detz / detA

                print "\nResult:"
                print "x = " + str (x)
                print "y = " + str (y)
                print "z = " + str (z)
            
                inp = raw_input ("\nPress [Enter] to go back")

                if inp == "":
                    tripack()

            def xyzw():
                print "\nGiven:"
                print "[ a1x + b1y + c1z + d1w = e1"
                print "| a2x + b2y + c2z + d2w = e2"
                print "| a3x + b3y + c3z + d3w = e3"
                print "[ a4x + b4y + c4z + d4w = e4"

                a1 = input ("\na1? ")
                b1 = input ("b1? ")
                c1 = input ("c1? ")
                d1 = input ("d1? ")
                e1 = input ("e1? ")
                
                a2 = input ("\na2? ")
                b2 = input ("b2? ")
                c2 = input ("c2? ")
                d2 = input ("d2? ")
                e2 = input ("e2? ")
                
                a3 = input ("\na3? ")
                b3 = input ("b3? ")
                c3 = input ("c3? ")
                d3 = input ("d3? ")
                e3 = input ("e3? ")

                a4 = input ("\na4? ")
                b4 = input ("b4? ")
                c4 = input ("c4? ")
                d4 = input ("d4? ")
                e4 = input ("e4? ")
                
                detA = det44 (a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3, a4, b4, c4, d4)

                detx = det44 (e1, b1, c1, d1, e2, b2, c2, d2, e3, b3, c3, d3, e4, b4, c4, d4)
                dety = det44 (a1, e1, c1, d1, a2, e2, c2, d2, a3, e3, c3, d3, a4, e4, c4, d4)
                detz = det44 (a1, b1, e1, d1, a2, b2, e2, d2, a3, b3, e3, d3, a4, b4, e4, d4)
                detw = det44 (a1, b1, c1, e1, a2, b2, c2, e2, a3, b3, c3, e3, a4, b4, c4, e4)

                x = detx / detA
                y = dety / detA
                z = detz / detA
                w = detw / detA

                print "\nResult:"
                print "x = " + str (x)
                print "y = " + str (y)
                print "z = " + str (z)
                print "w = " + str (w)
            
                inp = raw_input ("\nPress [Enter] to go back")

                if inp == "":
                    tripack()


            def xyzwt():
                print "\nGiven:"
                print "[ a1x + b1y + c1z + d1w + e1t = f1"
                print "| a2x + b2y + c2z + d2w + e2t = f2"
                print "| a3x + b3y + c3z + d3w + e3t = f3"
                print "| a4x + b4y + c4z + d4w + e4t = f4"
                print "[ a5x + b5y + c5z + d5w + e5t = f5"
                
                a1 = input ("\na1? ")
                b1 = input ("b1? ")
                c1 = input ("c1? ")
                d1 = input ("d1? ")
                e1 = input ("e1? ")
                f1 = input ("f1? ")
                
                a2 = input ("\na2? ")
                b2 = input ("b2? ")
                c2 = input ("c2? ")
                d2 = input ("d2? ")
                e2 = input ("e2? ")
                f2 = input ("f2? ")
                
                a3 = input ("\na3? ")
                b3 = input ("b3? ")
                c3 = input ("c3? ")
                d3 = input ("d3? ")
                e3 = input ("e3? ")
                f3 = input ("f3? ")

                a4 = input ("\na4? ")
                b4 = input ("b4? ")
                c4 = input ("c4? ")
                d4 = input ("d4? ")
                e4 = input ("e4? ")
                f4 = input ("f4? ")

                a5 = input ("\na5? ")
                b5 = input ("b5? ")
                c5 = input ("c5? ")
                d5 = input ("d5? ")
                e5 = input ("e5? ")
                f5 = input ("f5? ")
                
                detA = det55 (a1, b1, c1, d1, e1, a2, b2, c2, d2, e2, a3, b3, c3, d3, e3, a4, b4, c4, d4, e4, a5, b5, c5, d5, e5)

                detx = det55 (f1, b1, c1, d1, e1, f2, b2, c2, d2, e2, f3, b3, c3, d3, e3, f4, b4, c4, d4, e4, f5, b5, c5, d5, e5)
                dety = det55 (a1, f1, c1, d1, e1, a2, f2, c2, d2, e2, a3, f3, c3, d3, e3, a4, f4, c4, d4, e4, a5, f5, c5, d5, e5)
                detz = det55 (a1, b1, f1, d1, e1, a2, b2, f2, d2, e2, a3, b3, f3, d3, e3, a4, b4, f4, d4, e4, a5, b5, f5, d5, e5)
                detw = det55 (a1, b1, c1, f1, e1, a2, b2, c2, f2, e2, a3, b3, c3, f3, e3, a4, b4, c4, f4, e4, a5, b5, c5, f5, e5)
                dett = det55 (a1, b1, c1, d1, f1, a2, b2, c2, d2, f2, a3, b3, c3, d3, f3, a4, b4, c4, d4, f4, a5, b5, c5, d5, f5)

                x = detx / detA
                y = dety / detA
                z = detz / detA
                w = detw / detA
                t = dett / detA

                print "\nResult:"
                print "x = " + str (x)
                print "y = " + str (y)
                print "z = " + str (z)
                print "w = " + str (w)
                print "t = " + str (t)
            
                inp = raw_input ("\nPress [Enter] to go back")

                if inp == "":
                    tripack()

                

            menu88_opts = {2 : xy, 3 : xyz, 4 : xyzw, 5 : xyzwt, 0 : spectools}

            menu88_opts[menu88]()


        menu8_opts = {1 : ldesolve, 2 : primecheck, 3 : fpairs, 4 : lcsolve, 5 : quad, 6: integrate, 7 : derive, 8 : syseq, 0 : tripack}

        menu8_opts[menu8]()
        
                       
    def about():
        print "\nABOUT THIS SCRIPT"
        print "Triangle Utility Pack v0.7b (Jan03)"
        print "Written by Brian Guadalupe"
        print "Started in December 18, 2013"
        print "\nisPrime algorithm uses the Lucas-Lehmer primality test"
        print "Numerical integration uses the Simpson method"
        print "Systems of equation solver uses Cramer's rule"
        print "Linear congruence solver and Diophantine equation solver uses the extended Euclidean algorithm"
        print "\nAlso available in GitHub:"
        print "http://github.com/alltootechnical/PythonScripts/blob/master/triangle_utility_pack_0.7b.py"
        inp = raw_input ("\nPress [Enter] to go back")

        if inp == "":
            tripack()

    def exitscript():
        print ""
        
    menuopts = {1 : trisolve, 2 : rtsolvr, 3 : tsnsf, 4 : ffnsf, 5 : area, 6 : pythtriples, 7 : menu7, 8 : spectools, 9 : about, 0 : exitscript}
        
    menuopts[menu0]()
    
tripack()    # runs the script
