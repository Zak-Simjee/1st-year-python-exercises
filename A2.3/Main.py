from matplotlib import pyplot as plt
import math
def drawPolygon(n, length, xc, yc):
    if n<3 or length<0:
        exit(1)
    xp = []
    yp = []
    for i in range(n+1):
        xp.append(xc)

length =
r = length/(2*math.sin(3.141/n))
plt.axis('square')
plt.axis([0,500,0,500])
plt.xlabel('x')
plt.ylabel('y')
plt.title('A2.3 Polygon')
