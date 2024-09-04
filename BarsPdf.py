#Bars
import matplotlib.pyplot as plt
x=["A","B","C","D","E"]
y=[1,2,3,4,2]
mycolors=["magenta","yellow","green","red","cyan"]
plt.bar(x,y,color=mycolors,width=0.5)
plt.title=["Bar"]
plt.xlabel=["Letters"]
plt.ylabel=["Numbers"]

plt.show()