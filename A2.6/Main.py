from matplotlib import pyplot as plt
import math
def drawPoints(points, style):
    print('processing ', len(points), 'points')
    style = 'r-'
    x = []
    y = []
    for i in range(len(points)):
        x.append(points[i][0])
        y.append(points[i][1])

    plt.plot(x, y, style)

def main():
    plt.axis([0,500,0,500])
    plt.title('A2.6: Reading Points')
    plt.xlabel('x')
    plt.ylabel('y')
    a = str(input('Enter filename: '))
    fr = open(a, 'r')
    n = int(fr.readline())
    points = []







