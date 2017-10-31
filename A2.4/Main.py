from matplotlib import pyplot as plt
import math
def draw(points):
    print('processing ',len(points), 'points')
    x = []
    y = []
    for i in range (len(points)):
        x.append(points[i][0])
        y.append(points[i][1])

    plt.plot(x,y, 'b')
    plt.plot(x,y, 'ro')


n = 3
length = 200
r = length / (2 * math.sin(math.pi / n))
xc = 250
yc = 250

x1 = (xc+r*math.sin(2*math.pi*4/n))
y1 = (yc + r * math.cos(2 * math.pi * 4 / n))
x2 = (xc+r*math.sin(2*math.pi*5/n))
y2 = (yc + r * math.cos(2 * math.pi * 5 / n))
x3 = (xc+r*math.sin(2*math.pi*6/n))
y3 = (yc + r * math.cos(2 * math.pi * 6 / n))
x4 = (xc+r*math.sin(2*math.pi*7/n))
y4 = (yc + r * math.cos(2 * math.pi * 7 / n))
points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
plt.axis('square')
plt.axis([0,500,0,500])
plt.title('A2.4: Points')
plt.xlabel('x')
plt.ylabel('y')
draw(points)
plt.show()
