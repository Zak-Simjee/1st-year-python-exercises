from matplotlib import pyplot as plt

length = float(input())
if length<0:
    print('too low')
    exit(1)
if length>500:
    print('too high')
    exit(1)
plt.axis('square')
plt.axis([0,500,0,500])
plt.title('A2.2')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(250,250, 'k+')
plt.show()