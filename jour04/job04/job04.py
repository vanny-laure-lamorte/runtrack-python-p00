class Forme: 

    def aire(self): 
        return 0
    
class Rectangle (Forme): 

    def __init__(self, largeur, hauteur): 
        self.rect_largeur = largeur
        self.rect_hauteur = hauteur

    def aire(self): 
        return self.rect_hauteur * self.rect_largeur
    
rect1 = Rectangle(10, 20)
print(f"L'aire du rectangle est: {rect1.aire()}")

