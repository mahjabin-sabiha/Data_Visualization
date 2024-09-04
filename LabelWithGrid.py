#Label with Grid Lines
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,9]
y=[0,2,1,4,5,3,2,0]
plt.plot(x,y,marker='o',mfc='k',color='b')
plt.title("Laptop Price",fontsize=20,loc='right')
plt.xlabel("Price")
plt.ylabel("Increase")
plt.grid(axis='y',color='m',ls='--',lw=0.9)
plt.show()