from matplotlib import pyplot as plt
def draw(points):
    print('processing ',len(points), 'points')
    x = []
    y = []
    for i in range (len(points)):
        x.append(points[i][0])
        y.append(points[i][1])

    plt.plot(x,y, 'b')
    plt.plot(x,y, 'ro')
plt.axis([0,500,0,500])
plt.title('A2.4:Points')
plt.xlabel('x')
plt.ylabel('y')
points = [(100,100), (100,200), (200,200), (200, 100), (100,100)]
draw(points)
plt.show()