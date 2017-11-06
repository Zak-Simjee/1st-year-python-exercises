from matplotlib import pyplot as plt
import math
def main():
    a = input('Enter filename: ')
    plt.axis('square')
    plt.axis([-500,500,-500,500])
    x = 0
    y = 0
    angle = 0
    state = False
    pen = (x, y, angle, state)
    fr = open(a, 'r')
    for l in fr:
        b = l.split(' ')
        string = b[0]
        distance = b[1]
        if string == "PEN":
            distance = distance.rstrip()
            pen = Pen(pen, distance)
        elif string == 'FOWARD':
            pen = foward(pen, float(distance))
        elif string =='ROTATE':
            distance = float(distance)
            distance = math.radians(distance)
            pen = rotate(pen, distance)
        else:
            print('Error in Code')
            exit(2)

def foward(penstate, distance):
    x = penstate[0]
    y = penstate[1]
    angle = penstate[2]
    state = penstate[3]
    xi = x + distance*math.cos(angle)
    yi = y + distance*math.sin(angle)
    if state == False:
        return xi, yi, angle, state
    if state == True:
        plt.plot([x, xi], [y,yi])
        return xi, yi, angle, distance


def rotate(penstate, distance):
    x = penstate[0]
    y = penstate[1]
    angle = penstate[2]
    state = penstate[3]
    anglenew = angle + distance
    return x, y, anglenew, state

def Pen(penstate, distance):
    x = penstate[0]
    y = penstate[1]
    angle = penstate[2]
    state = penstate[3]
    if distance == 'UP':
        state = False
        return x, y, angle, state
    else:
        state = True
        return x, y, angle, state

def test(x, y, angle, state):
    pen = (x, y, angle, state)
    fowardtest = foward(pen, 100)
    if fowardtest == (100, 0, 0, False):
        x = None
    else:
        exit("Error in foward function")
    rotatetest = rotate(pen, 1)
    if rotatetest == (0, 0, 1, False):
        x = None
    else:
        exit("Error in rotate function")
    penuptest = Pen(pen, 'UP')
    if penuptest == (0, 0, 0, False):
        x = None
    else:
        exit('Error in pen up function')
    pendowntest = Pen(pen, 'DOWN')
    if pendowntest == (0, 0, 0, True):
        x = None
    else:
        exit('Error in pen down function')

test(0, 0, 0, False)
main()
plt.show()





