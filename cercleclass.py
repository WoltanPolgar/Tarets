import numpy as np


# On crée la classe Cercle pour que ce soit plus facile de les utiliser
class Cercle :
    def __init__(self, coordX, coordY, rayon, order):
        self.coordX = coordX
        self.coordY = coordY
        self.rayon = rayon
        self.grow = True
        self.order = order
        self.croissance = 5 
        self.alive = True

    # on peut afficher les attributs d'un cercle (self)
    def affiche(self):
        print('CoordX :'+str(self.coordX)+ ', CoordY : '+str(self.coordY) + ', Rayon :' + str(self.rayon) +
              ', Order :' +str(self.order)+', Alive : '+str(self.alive)+'\n')

    # on dessine le cercle (self)
    def dessin(self):
          # définit la fonction cercle abcisse, ordonnée, rayon
        tab = np.arange(0, 2 * np.pi, 0.01)  # matrice, définit l'étendu du domaine et la précision
        c = self.coordX + self.rayon * np.cos(tab)  # calcule les coordonnées x du cercle à dessiner
        s = self.coordY + self.rayon * np.sin(tab)  # calcule les coordonnées y du cercle à dessiner
        return c, s

    # calcule la distance entre deux cercles
    def distance(self, pt):
        return(np.sqrt((self.coordX-pt.coordX)**2 + (self.coordY - pt.coordY)**2))

    # détermine si deux cercles se touchent
    def touch(self, autre, t):
        d = np.sqrt((self.coordX-autre.coordX)**2 + (self.coordY - autre.coordY)**2)
        return(d <= (self.rayon + autre.rayon+(2/np.sqrt(t))*self.croissance))
    
    
    
    # cut permet de detecter les collisions parmi une liste de cercle
    def cut(self, list_autre, t):
        
        for elt in list_autre:
            if self.touch(elt, t):
                return True
        return False
            

