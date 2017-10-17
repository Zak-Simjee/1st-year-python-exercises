from matplotlib import pyplot as plt
plt.axis('square')
plt.axis([0,500,0,500])
plt.xlabel('x')
plt.ylabel('y')
plt.title('A2.1 Square')
a= [250]
b= [250]
c= [100,400,400,100,100]
d= [100,100,400,400,100]
x= [50,450,450,50,50]
y= [50,50,450,450,50]
plt.plot(a,b,'+k')
plt.plot(c,d, 'r')
plt.plot(x,y, 'b')
plt.show()