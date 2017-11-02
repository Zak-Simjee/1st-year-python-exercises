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

nsides = int(input('Enter number of sides: '))
if nsides<2:
    print('Error: Number of sides cannot be less than 2')
    exit(1)

length = float(input('Enter length: '))
if length<0:
    print('Error: Length cannot be less than 0')
    exit(1)

xc = float(input('Enter centre x point: '))
yc = float(input('Enter centre y point: '))
angle = float(input('Enter angle: '))
calculatedcoordinates = polygon(nsides, length, xc, yc, angle)
fr = open('points.txt', 'w')
fr.write(str(len(calculatedcoordinates)))
fr.write('\n')
for a in range(len(calculatedcoordinates)):
    xcoord = calculatedcoordinates[a][0]
    ycoord = calculatedcoordinates[a][1]
    coords = '{0:.2f},{1:.2f}'
    finalcoords = coords.format(xcoord, ycoord)
    fr.write(finalcoords)
    fr.write('\n')
fr.close()