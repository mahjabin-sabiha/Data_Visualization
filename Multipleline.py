import matplotlib.pyplot as plt
x1=[1,2,3,4,5]
y1=[1,3,6,8,1]
x2=[1,1,2,4,5]
y2=[7,4,0,1,0]
x3=[1,2,3,4]
y3=[7,2,0,1]
plt.plot(x1,y1,x2,y2,x3,y3,ls=':',lw=2,marker="o",mec="k",mfc="c",ms=10)
plt.show()