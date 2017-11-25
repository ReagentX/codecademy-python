"""This is an area calculator
for CodeCademy"""

from math import pi
from time import sleep
from datetime import datetime


now = datetime.now()

print "Starting calculator. It is %s/%s/%s at %s:%s" % \
    (now.month, now.day, now.year, now.hour, now.minute)
sleep(0.1)

hint = "Don't forget to include the correct units! \nExiting..."

option = raw_input("Enter C for Circle or T for Triangle: ").upper()

if option == 'C':
    print 'Circle selected.'
    radius = float(raw_input("Radius: "))
    area = pi * (radius ** 2)
    print "The pie is baking..."
    sleep(0.1)
    print "%.2f" % (area)

elif option == 'T':
    print 'Triangle selected'
    base = float(raw_input("Base: "))
    height = float(raw_input("Height: "))
    area = 0.5 * base * height
    print "Uni Bi Tri..."
    sleep(0.1)
    print "%.2f" % (area)

else:
    print "Really dude? Fuck off."
    pass
