#Labels
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,9]
y=[0,2,1,4,5,3,2,0]
plt.plot(x,y,marker='o',mfc='k',color='b')
plt.xlabel("Price")
plt.ylabel("Increase")
plt.show()