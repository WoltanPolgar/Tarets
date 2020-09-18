from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from main import drill
import imageio
import os
import moviepy.editor as mp
from cercleclass import Environnement

diametre = int(input("Quel est le diamètre du bois ? "))
nbslides = int(input("Quelle est la profondeur du bois ? "))
nbind = int(input("Combien d'individus ? "))
precision = int(input("Quel degré de précision des collisions ? (>150) "))
anim = int(input("Est-ce  qu'on fait une animation 3d ? (0 = non, 1 = oui) "))
gif = int(input("On affiche l'animation et on sauvegarde un gif ? (0 = non, 1 = oui) "))

lslides = drill(nbslides, nbind, precision, diametre)

np.random.seed(19680801)

if gif != 0:
    j=0
    frames = []
    
    env = Environnement(diametre)
    c_env,s_env = env.dessin()
    surface_totale = np.pi * env.rayon**2
    
    for slide in lslides:
        surface_prise = 0
        plt.clf()
        plt.plot(c_env,s_env)
        j+=1
        for elt in slide:
            surface_prise += np.pi * elt.rayon ** 2
            c, s = elt.dessin()
            plt.plot(c,s)
            #fig.patch.set_visible(False)
            #plt.axis('off')
            plt.axis(xmin=-1500, xmax=1500, ymin=-1500, ymax=1500)
            
        plt.pause(10 ** -10)
        print("surface restante en pourcentage : ", (surface_totale - surface_prise) / surface_totale)   
        plt.savefig(str(j)+'.png', transparent=True) # on sauvegarde les images

        new_frame = imageio.imread(str(j)+'.png')
        frames.append(new_frame)
        os.remove(str(j)+'.png')
    imageio.mimsave('animation2.mp4', frames) #on les change en gif     

    #clip = mp.VideoFileClip("animation2.gif")
    #clip.write_videofile("myvideo2.mp4")
    

 
if anim != 0:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    colors = ['r', 'g', 'b', 'y']
    yticks = [3, 2, 1, 0]
    frames = []




    for k, slide in enumerate(lslides):
        
        if k>300 and k <400:
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

