from math import pi
from random import choice as ch
planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]
random_planet = ch(planets)
if random_planet == 'Mercury':
  r = 2440
  area = 4 * pi * r * r
elif random_planet == 'Venus':
  r = 6052
  area = 4 * pi * r * r
elif random_planet == 'Earth':
  r = 6371
  area = 4 * pi * r * r
elif random_planet == 'Mars':
  r = 3390
  area = 4 * pi * r * r
elif random_planet == 'Saturn':
  r = 58232
  area = 4 * pi * r * r
else:
  print("Oops! An error occurred.")
print("The Surface area of the sphere is: " + str(area) + "\n" + " Name of the planet is: " + random_planet)

