from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as pl
import numpy as np


from main import drill


lslides = drill(600, 20, 200)


np.random.seed(19680801)


fig = pl.figure()
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y']
yticks = [3, 2, 1, 0]
for k, slide in enumerate(lslides):
    if k%10==0:
        for elt in slide:
            # Generate the random data for the y=k 'layer'.
            c, s = elt.dessin()

            # You can provide either a single color or an array with the same length as
            # xs and ys. To demonstrate this, we color the first bar of each set cyan.
            

            # Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.
            ax.plot(c, s, zs=k, zdir='y', alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# On the y axis let's only label the discrete values that we have data for.
#ax.set_yticks(yticks)

pl.show()