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

# Classe définissant le morceau de bois
# C'est un cercle de centre (0,0) et dont le diametre est demandé au lancement
class Environnement:
    # Crée le bout de bois
    def __init__(self, diametre):
        self.rayon = diametre / 2
        self.x = 0
        self.y = 0
    
    # Dessine le bout de bois
    def dessin(self):
        tab = np.arange(0, 2 * np.pi, 0.01)  # matrice, définit l'étendu du domaine et la précision
        c = self.x + self.rayon * np.cos(tab)  # calcule les coordonnées x du cercle à dessiner
        s = self.y + self.rayon * np.sin(tab)  # calcule les coordonnées y du cercle à dessiner
        return c, s

    # Sert à voir si l'individu (cercle) touche le bord
    def collision(self, cercle):
        return cercle.rayon + np.sqrt((cercle.coordX - self.x)**2 +(cercle.coordY -self.y)**2) > self.rayon
    
    # Sert à calculer le vecteur de repositionnement pour échapper au mur
    # l'argument first sert à ne pas trop répéter de code (il ne sert que pour le premier individu)
    def vecteur_mur(self, cercle, first=True):
        d_centre = np.sqrt((cercle.coordX - self.x)**2 +(cercle.coordY -self.y)**2)
        bonne_norme = cercle.rayon - (self.rayon - d_centre)
        v_mur_X = self.x - cercle.coordX
        v_mur_Y = self.y - cercle.coordY
        vL = np.sqrt(v_mur_X**2 + v_mur_Y**2)
        if first:
            cercle.coordX += (bonne_norme/vL) * v_mur_X
            cercle.coordY += (bonne_norme/vL) * v_mur_Y
            return cercle
        else:
            return (bonne_norme/vL) *v_mur_X, (bonne_norme/vL) *v_mur_Y   

      

