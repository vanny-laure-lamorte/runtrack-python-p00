class Rectangle: 

    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur       

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):   
        return (self.get_largeur() + self.get_largeur()) *2
    
    def surface(self): 
        return self.get_largeur() * self.get_longueur()
    
rect1 = Rectangle(10, 20)
print(f"Le perimètre est : {rect1.perimetre()}")
print(f"La surface est : {rect1.surface()}")
        
class Parallelepipede(Rectangle):

    def __init__(self, hauteur, longueur, largeur): 
        Rectangle.__init__(self, longueur, largeur)
        self.parallelepipede_hauteur = hauteur
         
    def volume(self): 
        return self.get_largeur() * self.get_longueur() * self.parallelepipede_hauteur
    
parallelepipede1 = Parallelepipede(10, 20, 30)
print(f"Le volume du parallelepipede: {parallelepipede1.volume()}")