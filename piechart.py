import matplotlib.pyplot as plt
y=[35,25,25,15]
mylabels=["Apples","Banannas","Cherries","Dates"]
myexplode=[0.2,0,0,0]
plt.pie(y,labels=mylabels,startangle=90,explode=myexplode)
plt.legend(title="Four Fruits")
plt.show()