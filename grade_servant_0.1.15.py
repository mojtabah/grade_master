#!/usr/bin/env python

print "I am your grade servant. I will obey you."

variable = int(raw_input("Enter your grade"))

if variable > 89:
  print "You get an A!"
elif variable > 79:
  print "You get a B!"
elif variable > 69:
  print "You get a C!"
elif variable > 59:
  print "You get a D!"
else:
  print "You fail!!!"
