import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*np.pi+0.1 , np.pi/6)

y= np.sin(x)
y_error=np.random.randint(0,3,13)
x_error=np.random.randint(0,2,13)

plt.errorbar(x,y, yerr=y_error, xerr=x_error, marker= '^', linestyle="--" , mfc= "w" , capsize=5 , markersize= 10)
plt.show()
