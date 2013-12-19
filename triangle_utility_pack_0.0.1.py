#!/usr/bin/python
#"Not yet final!" -Brian
from __future__ import division
import math

def tripack():
    print "\nTRIANGLE UTILITY PACK"
    print "====================="
    print "Choices:"
    print "[1] right triangle solver"
    print "[2] 30-60-90 side finder"
    print "[3] 45-45-90 side finder"
    print "[4] area of a triangle"
    print "[5] ----------"
    print "[6] ----------"
    print "[7] ----------"
    print "[8] ----------"
    print "[9] ----------"
    print "[0] about"
    menu0 = input ("Choose one: ")
    
    menu1_opts = {}
    
    def sin(x):
        return math.sin(x)
        
    def cos(x):
        return math.cos(x)
        
    def tan(x):
        return math.tan(x)
    
    def asin(x):
        return math.asin(x)
    
    def atan(x):
        return math.atan(x)
        
    def rad(x):
        return math.radians(x)
        
    def deg(x):
        return math.degrees(x)
    
    def sqrt(x):
        return math.sqrt(x)
        
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
            aA = input ("angle A?")
            sa = input ("side a?")
            
            aB = 90 - aA
            sb = sa / tan (rad (aA))
            sc = sa / sin (rad (aA))
            
            print "\nResults:"
            print ("angle B = " + str (aB))
            print ("side b = " + str (sb))
            print ("side c = " + str (sc))
            
        def aasb():
            aB = 0
            sa = 0
            sc = 0
            
            print "\nGiven:"
            aA = input ("angle A?")
            sb = input ("side b?")
            
            aB = 90 - aA
            sa = sb * tan (rad (aA))
            sc = sb / cos (rad (aA))
        	
            print "\nResults:"
            print ("angle B = " + str (aB))
            print ("side a = " + str (sa))
            print ("side c = " + str (sc))
            
        def aasc():
            aB = 0
            sa = 0
            sb = 0
            
            print "\nGiven:"
            aA = input ("angle A?")
            sc = input ("side c?")
            
            aB = 90 - aA
            sa = sc * sin (rad (aA))
            sb = sc * cos (rad (aA))
            
            print "\nResults:"
            print ("angle B = " + str (aB))
            print ("side a = " + str (sa))
            print ("side b = " + str (sb))
            
        def sasc():
            aA = 0
            aB = 0
            sb = 0
    
            print "\nGiven:"
            sa = input ("side a?")
            sc = input ("side c?")
            
            
            aA = deg (asin (sa / sc))
            aB = 90 - aA
            sb = sqrt (sc**2 - sa**2)
            
            print "\nResults:"
            print ("angle A = " + str (aA))
            print ("angle B = " + str (aB))
            print ("side b = " + str (sb))
            
        def sasb():
            aA = 0
            aB = 0
            sc = 0
            
            print "\nGiven:"
            sa = input ("side a?")
            sb = input ("side b?")
            
            
            aA = deg (atan (sa / sb))
            aB = 90 - aA
            sc = sqrt (sa**2 + sb**2)
            
            print "\nResults:"
            print ("angle A = " + str (aA))
            print ("angle B = " + str (aB))
            print ("side c = " + str (sc))
    
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
                sa = input ("\nside a?")
                
                sb = 0
                sc = 0
                
                sb = sa * sqrt (3)
                sc = 2 * sa
                
                print "\nResults:"
                print ("side b = " + str (sb))
                print ("side c = " + str (sc))
                
            def thirty_b():
                sb = input ("\nside b?")
                
                sa = 0
                sc = 0
                
                sa = sb * (sqrt (3) / 3)
                sc = sb * (2 * sqrt (3) / 3)
                
                print "\nResults:"
                print ("side a = " + str (sa))
                print ("side c = " + str (sc))
                
            def thirty_c():
                sc = input ("\nside c?")
                
                sa = 0
                sb = 0
                
                sa = sc / 2
                sb = sc * (sqrt (3) / 2)
                
                print "\nResults:"
                print ("side a = " + str (sa))
                print ("side b = " + str (sb))    
            
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
                sa = input ("\nside a?")
                
                sb = 0
                sc = 0
                
                sb = sa * (sqrt (3) / 3)
                sc = sa * (2 * sqrt (3) / 3)
                                
                print "\nResults:"
                print ("side b = " + str (sb))
                print ("side c = " + str (sc))
                
            def sixty_b():
                sb = input ("\nside b?")
                
                sa = 0
                sc = 0
                
                sa = sb * sqrt (3)
                sc = 2 * sb
                
                print "\nResults:"
                print ("side a = " + str (sa))
                print ("side c = " + str (sc))
                
            def sixty_c():
                sc = input ("\nside c?")
                
                sa = 0
                sb = 0
                
                sa = sc * (sqrt (3) / 2)
                sb = sc / 2
                                
                print "\nResults:"
                print ("side a = " + str (sa))
                print ("side b = " + str (sb))    
            
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
            sa = input ("\nside a?")
            
            sb = 0
            sc = 0
            
            sb = sa 
            sc = sa * (sqrt (2))
                            
            print "\nResults:"
            print ("side b = " + str (sb))
            print ("side c = " + str (sc))
            
        def fortyfive_b():
            sb = input ("\nside b?")
            
            sa = 0
            sc = 0
            
            sa = sb
            sc = sb * (sqrt (2))
            
            print "\nResults:"
            print ("side a = " + str (sa))
            print ("side c = " + str (sc))
            
        def fortyfive_c():
            sc = input ("\nside c?")
            
            sa = 0
            sb = 0
            
            sa = sc / (sqrt (2))
            sb = sa
                            
            print "\nResults:"
            print ("side a = " + str (sa))
            print ("side b = " + str (sb))    
        
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
        print "[7] three angles and circumradius"
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
            
        def withtrig():
            print "\nGiven:"
            side1 = input ("first side?")
            side2 = input ("second side?")
            angle = input ("included angle?")
            
            area = 0
            
            area = (1 / 2) * side1 * side2 * sin (rad (angle))
            
            print "\nResult:"
            print ("area = " + str (area))
        
        def herons():
            print "\nGiven:"
            side1 = input ("first side?")
            side2 = input ("second side?")
            side3 = input ("third side?")
            
            s = 0
            area = 0
            
            s = (side1 + side2 + side3) / 2
            area = sqrt (s * (s - side1) * (s - side2) * (s - side3))
            
            print "\nResult:"
            print ("area = " + str (area))
        
        def evenmoretrig():
            print "\nGiven:"
            angle1 = input ("first angle?")
            angle2 = input ("second angle?")
            side = input ("a side?")
            
            area = 0
            angle3 = 0
            
            angle3 = 180 - (angle1 + angle2)
            area = (side**2 * sin (rad (angle2)) * sin (rad (angle3))) / (2 * sin (rad (angle1)))
            
            print "\nResult:"
            print ("area = " + str (area))
            
        def oneside():
            print "\nGiven"
            side = input ("side?")
            
            area = 0
            
            area = (sqrt (3) / 4) * side ** 2
            
            print "\nResult:"
            print ("area = " + str (area))
        
        def spandir():
            print "\nGiven"
            sper = input ("semiperimeter?")
            inrad = input ("inradius?")
            
            area = 0
            
            area = sper * inrad
            
            print "\nResult:"
            print ("area = " + str (area))
            
        def threeangles():
            print "\nGiven:"
            angle1 = input ("first angle?")
            angle2 = input ("second angle?")
            angle3 = input ("third angle?")
            circrad = input ("circumradius?")
        
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
        elif menu4 == 7:
            threeangles()
        elif menu4 == 0:
            tripack()
    
    def about():
        print "\nABOUT THIS APP"
        print "Triangle Utility Pack"
        print "Written by me!"
        print "December 18, 2013"
        
    menuopts = {1 : rtsolvr, 2 : tsnsf, 3 : ffnsf, 4 : area, 5 : rtsolvr, 6 : rtsolvr, 7 : rtsolvr, 8 : rtsolvr, 9 : rtsolvr, 0 : about}
        
    menuopts[menu0]()
    
tripack()