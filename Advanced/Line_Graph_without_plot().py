import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


x=np.random.rand(10)
y=np.random.rand(10)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
l=Line2D(x,y)
ax.add_artist(l)
plt.show()
