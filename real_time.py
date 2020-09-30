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


from cercleclass import Cercle, Environnement



if os.path.exists('frames2'):
    shutil.rmtree('frames2') #on efface le dossier temporaire
os.mkdir('frames2')#on crée le fichier temporaire où on stocke les images
if os.path.exists('bmp'):
    shutil.rmtree('bmp') #on efface le dossier temporaire
os.mkdir('bmp')#on crée le fichier temporaire où on stocke les images

def coordonnees(environnement):
    r = environnement.rayon
    x = rd.uniform(-r, r)
    y = rd.uniform(-r, r)
    while x**2 + y**2 > r**2 :
        x = rd.uniform(-r, r)
        y = rd.uniform(-r, r) 
    return x, y   

def drill_real_time(nbslides, nbindividus, precision, diametre):
    environnement = Environnement(diametre)
    list_slides = []
    slide_initiale = []
    # Initialisation
    for i in range(nbindividus): # Création des tarets
        x_initial, y_initial = coordonnees(environnement)
        taret = Cercle(x_initial, y_initial, 0, i)
        taret.croissance = rd.uniform(5, 10) # Pour faire varier la croissance
        slide_initiale.append(taret)
    list_slides.append(slide_initiale)
    
    
    return list_slides