import numpy as np
import matplotlib.pyplot as plt
import colorsys
import seaborn as sns

x = np.arange(0, 2*np.pi+0.1 , np.pi/6)

y= np.sin(x)
y_error=np.random.rand(13)
x_error=np.random.rand(13)
l=np.linspace(0.1,1,20)
colors=[colorsys.rgb_to_hsv(i,0.1,i) for i in l]
#folors=np.arange(5,50,2)
#xolors=sns.color_palette('rocket', 20)
p=["s","o","^" ]

#for i in range(20):
#	plt.errorbar(x+2*i,y+i, yerr=y_error, xerr=x_error, marker= p[i%3] , linestyle="--" , mfc= "w" , capsize=4 , markersize= 10, alpha=0.6,color=colors[i])



y2= np.sin(y)
for i in range(20)  :
	plt.errorbar(x+i,y2**i, yerr=x_error, xerr=y_error,marker=p[i%3], linestyle='-.', mfc='w', capsize=3, markersize= 10, alpha= 0.8, color=colors[i])
plt.minorticks_on()
plt.tick_params(direction='in' , which='major', length=20, right=True, top=True)
plt.tick_params(direction='in', which='minor', length = 10, right=True, top= True)

plt.xlabel("x value", fontsize=15)
plt.ylabel("y value", fontsize=15)

plt.legend()


plt.show()
