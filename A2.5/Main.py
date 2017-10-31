from matplotlib import pyplot as plt
import math
def polygon(nsides, length, xc, yc, angle):
    coordinates = []
    math.radians(angle)
    r = length / (2 * math.sin(math.pi / nsides))
    for i in range(nsides+1):
        x = xc + r*math.sin((2*math.pi*i/nsides)+ angle)
        y = yc + r*math.cos((2*math.pi*i/nsides)+ angle)
    coordinate = (x, y)
    coordinates.append(coordinate)
    return coordinates

nsides = int(input('Enter number of side'))
if nsides<2:
    print('Number of sides is too low')
    exit(1)

length = float(input('Enter length'))
if length<0:
    print('Length is too small')
    exit(1)

xc = float(input('Enter centre x point'))
yc = float(input('Enter centre y point'))
angle = float(input('Enter angle'))
calculatedcoordinates = polygon(nsides, length, xc, yc, angle)
fr = open('points.txt', 'w')
fr.write(len(calculatedcoordinates))
fr.write(calculatedcoordinates)
