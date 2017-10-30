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
for a in range(n+1):

   x1 = 250
   y1 = 250+(math.sqrt(200**2-100**2)/2)
   x2 = 250-100
   y2 = 250-(math.sqrt(200**2-100**2)/2)
   x3 = 250+100
   y3 = 250-(math.sqrt(200**2-100**2)/2)
   x4 = 250
   y4 = 250+(math.sqrt(200**2-100**2)/2)

points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
plt.axis('square')
plt.axis([0,500,0,500])
plt.title('A2.4: Points')
plt.xlabel('x')
plt.ylabel('y')
draw(points)
plt.show()
