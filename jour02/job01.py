class Rectangle: 

    def __init__(self, longeur, largeur): 
        self.__longeur = longeur
        self.__largeur = largeur

    # Assesseur: afficher
    def get_longeur(self):
        return self.__longeur
    
    def get_largeur(self): 
        return self.__largeur
    
    # Mutateur : modifier
    def set_longeur(self, longeur):
        self.__longeur = longeur
    
    def set_largeur(self, largeur): 
        self.__largeur = largeur
       
# Valeurs de départ
rect = Rectangle (10, 5)
print("La longeur est : ", rect.get_longeur())
print("La largeur est : ", rect.get_largeur())  

# Valeur modifié
rect.set_longeur(15)
print("La longeur modifiée est : ", rect.get_longeur())
rect.set_largeur(20)
print("La largeur modifiée est : ", rect.get_largeur()) 
