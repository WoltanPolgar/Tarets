import os
import random as rd
import shutil
from PIL import Image
import imageio
import moviepy.editor as mp
import numpy as np
import pylab as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as pl


from cercleclass import Cercle



if os.path.exists('frames2'):
    shutil.rmtree('frames2') #on efface le dossier temporaire
os.mkdir('frames2')#on crée le fichier temporaire où on stocke les images
if os.path.exists('bmp'):
    shutil.rmtree('bmp') #on efface le dossier temporaire
os.mkdir('bmp')#on crée le fichier temporaire où on stocke les images


# ici c'est la config tu peux jouer sur le nombre de tarets et le nombre de slides (profondeur du bois)
#nbslides = 600
#nbindividus = 10
#precision = 200

def drill(nbslides, nbindividus, precision):
    lslides =[]
    lcentres = []
    #je sais pas si c'est nécessaire mais sinon ça renvoie une erreur
    firstcercle = Cercle(600*rd.random(), 600*rd.random(), 0, 0)
    lcentres.append(firstcercle)
    lslides.append(lcentres)
    # on fait grandir le premier individu sur tous les slides
    for k in range(nbslides):
        L = []
        tmp = lslides[k][0]
        # on est obligé de créer un nouvel objet cercle sur chaque slide
        groscercle = Cercle(tmp.coordX, tmp.coordX, tmp.rayon+(1/np.sqrt(k+1))*tmp.croissance, tmp.order)
        L.append(groscercle)
        lslides.append(L)
    # on ajoute les individus les uns après les autres
    for i in range(1, nbindividus):
        # nouvel individu ajouté sur la première slide
        newcercle = Cercle(rd.uniform(-1000,1000), rd.uniform(-1000,1000), 0, i)
        lslides[0].append(newcercle)
        for j in range(1,nbslides+1):
            gg = lslides[j-1][i]
            # Ce if permet de remplir la liste avec les tarets morts, sinon on a des problemes d'index
            if not gg.alive:
                cercle_mort = Cercle(gg.coordX, gg.coordY, 0, gg.order)
                cercle_mort.alive = False
                cercle_mort.croissance = 0
                lslides[j].append(cercle_mort)
                continue
            tmp = Cercle(gg.coordX, gg.coordY, gg.rayon + (1/np.sqrt(j))*gg.croissance, gg.order)
            vX = 0
            vY = 0
            # on vérifie sur chaque slides si les individus déjà présents sont touchés ou pas
            for elt in lslides[j]: 
                if elt.alive: # La collision ne concerne que les tarets vivants
                    if gg.touch(elt, j):
                        # si il y a contact on calcule le décalage
                        vX += (gg.coordX - elt.coordX)*1.2
                        vY += (gg.coordY - elt.coordY)*1.2  
            vL = np.sqrt(vX ** 2 + vY ** 2)
            #on applique le décalage
            saveX, saveY = tmp.coordX, tmp.coordY
            if vL != 0 :
                tmp.coordX = (vX/vL)*(2/np.sqrt(j+1))*tmp.croissance + tmp.coordX
                tmp.coordY = (vY/vL)*(2/np.sqrt(j+1))*tmp.croissance + tmp.coordY
                # Cette boucle permet de gerer les collisions, on recalcule la position du trou 
                # On compte le nombre de calcul avec repositionning
                repositionning = 0
                while tmp.cut(lslides[j],j):
                    vXb, vYb = 0, 0
                    for elt in lslides[j]:
                        if tmp.touch(elt, j):
                            vXb += (gg.coordX - elt.coordX)*1.2

                            vYb += (gg.coordY - elt.coordY)*1.2 
                    vLb = np.sqrt(vXb ** 2 + vYb ** 2)
                    tmp.coordX = (vXb/vLb)*(2/np.sqrt(j+1))*tmp.croissance + tmp.coordX
                    tmp.coordY = (vYb/vLb)*(2/np.sqrt(j+1))*tmp.croissance + tmp.coordY
                    repositionning +=1
                    if repositionning > precision: # Si on a fait trop de calcul c'est qui est pris au piege
                        print("Un taret s'arrete ! ") # En lisant la console tu peux savoir combien se sont arretes
                        tmp.alive = False # on le stoppe
                        break
            lslides[j].append(tmp)
    return(lslides)





'''
# on affiche pour l'animation
j=0
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
 
    plt.savefig('frames2/'+str(j)+'.png', transparent=True) # on sauvegarde les images
    file_in ='frames2/'+str(j)+'.png'
    img = Image.open(file_in)
    newimg = img.convert('L')
    file_out = "bmp/"+str(j)+".bmp"
    newimg.save(file_out)


# tu peux décommenter cette partie pour lancer automatiquement la création vidéo

frames = []

for i in range(1,nbslides+1):
    new_frame = imageio.imread('frames2/images'+str(i)+'.png')
    frames.append(new_frame)
imageio.mimsave('animation2.gif', frames) #on les change en gif     

clip = mp.VideoFileClip("animation2.gif")
clip.write_videofile("myvideo2.mp4")

animation_3d()
'''
