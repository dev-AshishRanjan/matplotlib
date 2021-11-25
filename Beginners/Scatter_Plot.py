import random
import colorsys
import matplotlib.pyplot as plt
import numpy as np

l=[random.random() for i in range(22)]
print(l)

colors=[colorsys.rgb_to_hsv(i, 0.1, 0.1) for i in l]

print(colors)

x=np.random.rand(22)
y=np.random.rand(22)
a=np.random.rand(22)**2*1000
folors =np.random.rand(22)


plt.scatter(x,y, c=folors , s=a ,alpha=0.8 )

plt.show()
