import matplotlib.pyplot as plt
#Next we need an array of numbers to plot. Various array functions are defined in the NumPy library which is imported with the np alias.
import numpy as np
#We now obtain the ndarray object of angles between 0 and 2π using the arange() function from the NumPy library.
x=np.arange(0, math.pi*2, 0.05)
#The ndarray object serves as values on x axis of the graph. The corresponding sine values of angles in x to be displayed on y axis are obtained by the following statement:
y=np.sin(x)
#The values from two arrays are plotted using the plot() function.
plt.plot(x,y)
#You can set the plot title, and labels for x and y axes.
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')
#The Plot viewer window is invoked by the show() function:
plt.show()
