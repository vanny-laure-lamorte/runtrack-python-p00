
from math import pi

class Forme: 

    def aire(self): 
        return 0
    
class Rectangle (Forme): 

    def __init__(self, largeur, hauteur): 
        self.rect_largeur = largeur
        self.rect_hauteur = hauteur

    def aire(self): 
        return self.rect_hauteur * self.rect_largeur
    
class Cercle (Forme): 

    def __init__(self, radius): 
        self.cercle_radius = radius

    def aire(self): 
        return pi * self.cercle_radius *  self.cercle_radius


rect1 = Rectangle(10, 20)
print (f"Voici l'air du rectangle: {rect1.aire()}")

cercle1 = Cercle(10)
print (f"Voici l'air du rectangle: {cercle1.aire()}")


    