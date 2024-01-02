class Personnage: 

    def __init__(self, x, y): 
        self.attribut_x = x
        self.attribut_y= y 

    def gauche (self): 
        self.attribut_x -=1
        print (f"La position de x pour aller à gauche est: {self.attribut_x}")

    def droite(self): 
        self.attribut_x +=1
        print (f"La position de x pour aller à droite est: {self.attribut_x}")

    def bas (self): 
        self.attribut_y -=1
        print (f"La position de y pour aller à en bas est: {self.attribut_y}")
    
    def haut (self): 
        self.attribut_y +=1
        print (f"La position de y pour aller en haut est: {self.attribut_y}")

    def position (self): 
        position_tuple = (self.attribut_x, self.attribut_y)        
        print (position_tuple)

afficher_gauche= Personnage(-10, 20)
afficher_gauche.gauche()

afficher_droite= Personnage(10, 20)
afficher_droite.droite()

afficher_bas= Personnage(30, -40)
afficher_bas.bas()

afficher_haut= Personnage(30, 40)
afficher_haut.haut()

afficher_position = Personnage(10, 20)
afficher_position.position()

