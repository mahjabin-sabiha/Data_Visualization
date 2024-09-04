import matplotlib.pyplot as plt
y=[15,30,30,20,5]
mycolors=["black","blue","cyan","magenta","green"]
mylabels=["Apple","Banana","Grapes","Weed","Tobacco"]
myexplode=[0,0.2,0.3,0,0]
plt.pie(y,colors=mycolors,explode=myexplode,labels=mylabels)
plt.legend(title="Fruits")
plt.show()
