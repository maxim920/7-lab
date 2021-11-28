from numpy import *
import matplotlib.pyplot as plt

x = linspace(1, 7, 51) 
y = 5*sin(10*x)*sin(3*x)/(x^(1/2))

plt.plot(x, y)
plt.show()