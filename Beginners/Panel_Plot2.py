import matplotlib.pyplot as plt
import numpy as np


x=np.arange(400,800,1)
yt=np.sin(np.arange(0,3,0.0075))
xt=np.sqrt(np.arange(0,3,0.0075))
tt= np.add(-yt, xt)
y= abs(tt)*50

u=np.sin(np.linspace(0,7 ,400))*50

l=[i**2-500*i+10 for i in x]
t=tt*50
#for i in range

plt.plot(x,t ,linestyle='none', marker='^', label='90' , mfc='w', markersize=8  ,color="green"  )
plt.plot(x,u+np.linspace(-15 , 15,400)+7 , linestyle='none', marker='o', label='60' ,mfc='w', markersize=10, alpha=0.7,color="blue")
plt.plot(x,u , linestyle='none',  marker='s',  label='30', mfc='w', markersize=8, color="red")
#plt.ylim([5,60])
plt.xlim([410,750])
plt.minorticks_on()
plt.legend( fontsize=14)
plt.show()
