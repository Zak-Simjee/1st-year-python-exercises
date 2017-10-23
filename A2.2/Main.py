from matplotlib import pyplot as plt

length = float(input())
if length<0:
    print('Error: Value too low')
    exit(1)
if length>500:
    print('Error: Value too high')
    exit(1)
plt.axis('square')
plt.axis([0,500,0,500])
plt.title('A2.2')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(250,250, 'k+')
x = [250-(length/2),250+(length/2),250+(length/2),250-(length/2),250-(length/2)]
y = [250-(length/2),250-(length/2),250+(length/2),250+(length/2),250-(length/2)]
plt.plot(x,y, 'b')
plt.show()
