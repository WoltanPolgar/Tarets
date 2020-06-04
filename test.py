from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from main import drill
import imageio
import os
import moviepy.editor as mp


nbslides = int(input("quelle est la profondeur du bois ?"))
nbind = int(input("combien d'individus ?"))
precision = int(input("quel degré de précision des collisions ? (>150)"))
anim = int(input("est-ce  qu'on fait une animation 3d ? (0 = non, 1 = oui)"))
gif = int(input("on sauvegarde un gif ? (0 = non, 1 = oui)"))

lslides = drill(nbslides, nbind, precision)

np.random.seed(19680801)

if gif != 0:
    j=0
    frames = []
    for slide in lslides:
        plt.clf()
        j+=1
        for elt in slide:
            c, s = elt.dessin()
            plt.plot(c,s)
            #fig.patch.set_visible(False)
            plt.axis('off')
            #plt.axis(xmin=-1500, xmax=1500, ymin=-1500, ymax=1500)
        plt.pause(10 ** -10)
    
        plt.savefig(str(j)+'.png', transparent=True) # on sauvegarde les images

        new_frame = imageio.imread(str(j)+'.png')
        frames.append(new_frame)
        os.remove(str(j)+'.png')
    imageio.mimsave('animation2.gif', frames) #on les change en gif     

    clip = mp.VideoFileClip("animation2.gif")
    clip.write_videofile("myvideo2.mp4")
    

 
if anim != 0:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    colors = ['r', 'g', 'b', 'y']
    yticks = [3, 2, 1, 0]
    frames = []



    for k, slide in enumerate(lslides):
        
        if k%10==0:
            for elt in slide:
                # Generate the random data for the y=k 'layer'.
                c, s = elt.dessin()
                
                #plt.axis(xmin=-1500, xmax=1500, ymin=-1500, ymax=1500)
                # You can provide either a single color or an array with the same length as
                # xs and ys. To demonstrate this, we color the first bar of each set cyan.
                

                # Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.
                ax.plot(c, s, zs=k, zdir='y', alpha=0.8)
        
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')


    # On the y axis let's only label the discrete values that we have data for.
    #ax.set_yticks(yticks)
    plt.savefig('3d.png')
    plt.show()

