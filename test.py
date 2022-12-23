import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return np.sin(x)

def f2(x):
    return np.cos(x)

x = np.linspace(0,2*np.pi,101)

plt.plot(x,f1(x),color='blue')
plt.plot(x,f2(x),color='red')
plt.title("$\\beta(\phi_{ij})$ as a function of $\phi_{ij}$",color="black",fontsize=25)
plt.xlabel('$\phi_{ij}$',color="black",fontsize=20,fontweight='bold')
plt.ylabel('$\\beta(\phi_{ij})$',fontsize=20,fontweight='bold')
plt.axhline(color='black')
plt.axvline(color='black')
plt.legend(["$\phi_{ij}^2$","$\phi_{ij}^3$"],bbox_to_anchor=[1, 1],title="Legend",fontsize=20)
plt.grid()
plt.show()