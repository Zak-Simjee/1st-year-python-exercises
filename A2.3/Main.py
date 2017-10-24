from matplotlib import pyplot as plt
import math
def drawPolygon(n, length, xc, yc):
    if n<3 or length<0:
        exit(1)
    xp = []
    yp = []
    for i in range(n+1):
        xp.append(xc+r*math.sin(2*math.pi*i/n))
        yp.append(yc + r * math.cos(2 * math.pi * i / n))
    plt.plot(xp,yp,'k' )
n = 3
length = 125
r = length/(2*math.sin(math.pi/n))
xc = 150
yc = 150
plt.axis('square')
plt.axis([0,500,0,500])
plt.xlabel('x')
plt.ylabel('y')
plt.title('A2.3 Polygon')
drawPolygon(n, length, xc, yc)
n = 4
length = 100
r = length/(2*math.sin(math.pi/n))
xc = 250
yc = 250
drawPolygon(n, length, xc, yc)
n = 6
length = 75
r = length/(2*math.sin(math.pi/n))
xc = 350
yc = 350
drawPolygon(n, length, xc, yc)
plt.show()