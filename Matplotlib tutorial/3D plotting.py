import matplotlib.pyplot as plt
import numpy as np
#from mpl_toolkits.mplot3d import Axes3D


ax=plt.axes(projection="3d")#creating a variable for the 3d axes

# Generate random data
x = np.random.random(50)
y = np.random.random(50)
z = np.random.rand(50)

''' Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
'''

ax.scatter(x, y, z)

ax.set_xlabel("test")
ax.set_title("3D Plot")

plt.show()

#all the 2d features can b applied here


#PLOTTING A SURFACE CURVE
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

ax.plot_surface(X, Y, Z, cmap="Spectral")
ax.set_title("3D Plot")
ax.set_xlabel("test")
ax.view_init(azim=0, elev=90)
plt.show()
