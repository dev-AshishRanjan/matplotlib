import matplotlib.pyplot as plt
import numpy as np


x=np.arange(400,800,2)
yt=np.sin(np.arange(0,3,0.015))
xt=np.sqrt(np.arange(0,3,0.015))
tt= np.add(yt, -xt)
y= abs(tt)*50

l=[i**2-500*i+10 for i in x]
t=tt*50
#for i in range

plt.plot(x,y ,linestyle='none', marker='s', label='90' , mfc='w', markersize=8    )
plt.plot(x,y+np.linspace(-15 , 15,200)+7 , linestyle='none', marker='o', label='60' ,mfc='w', markersize=10, alpha=0.7)
plt.plot(x,t+40 , linestyle='none',  marker='^',  label='30', mfc='w', markersize=12)
#plt.ylim([5,60])
plt.xlim([410,750])
plt.minorticks_on()
plt.legend( fontsize=14)
plt.show()
