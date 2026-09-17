import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi,500)  #linspace函数生成0到2π之间的500个点
y=np.sin(x)

plt.plot(x,y,label='sin(x)')

plt.xlabel('x')
plt.ylabel('y')

plt.title('Sine Function')

plt.legend()

plt.grid(True)

plt.show()