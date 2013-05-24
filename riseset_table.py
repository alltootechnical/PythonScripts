# -*- coding: utf-8 -*-
import sys
import ephem        # Needs PyEphem (rhodesmill.org/pyephem/‎)

lat = str(sys.argv[1])
lon = str(sys.argv[2])

place = ephem.Observer()
place.lat = lat
place.lon = lon

Su = ephem.Sun()
Me = ephem.Mercury()
Ve = ephem.Venus()
Mo = ephem.Moon()
Ma = ephem.Mars()
Ju = ephem.Jupiter()
Sa = ephem.Saturn()
Ur = ephem.Uranus()
Ne = ephem.Neptune()

print "Object           Rise            Transit               Set"
print "==================================================================="
print "Sun     | " + str(place.next_rising(Su)) + " | " + str(place.next_transit(Su)) + " | " + str(place.next_setting(Su))
print "Mercury | " + str(place.next_rising(Me)) + " | " + str(place.next_transit(Me)) + " | " + str(place.next_setting(Me))
print "Venus   | " + str(place.next_rising(Ve)) + " | " + str(place.next_transit(Ve)) + " | " + str(place.next_setting(Ve))
print "Moon    | " + str(place.next_rising(Mo)) + " | " + str(place.next_transit(Mo)) + " | " + str(place.next_setting(Mo))
print "Mars    | " + str(place.next_rising(Ma)) + " | " + str(place.next_transit(Ma)) + " | " + str(place.next_setting(Ma))
print "Jupiter | " + str(place.next_rising(Ju)) + " | " + str(place.next_transit(Ju)) + " | " + str(place.next_setting(Ju))
print "Saturn  | " + str(place.next_rising(Sa)) + " | " + str(place.next_transit(Sa)) + " | " + str(place.next_setting(Sa))
print "Uranus  | " + str(place.next_rising(Ur)) + " | " + str(place.next_transit(Ur)) + " | " + str(place.next_setting(Ur))
print "Neptune | " + str(place.next_rising(Ne)) + " | " + str(place.next_transit(Ne)) + " | " + str(place.next_setting(Ne))
print "==================================================================="
print ""
print "Note: All times are in UTC (GMT +0)"

