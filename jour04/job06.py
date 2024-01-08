class Vehicle: 

    def __init__(self, marque, modele, annee, prix): 
        self.vehicle_marque = marque
        self.vehicle_modele = modele
        self.vehicle_annee = annee
        self.vehicle_prix = prix
    
    def informationsVehicule(self): 
        print (f"\nMarque = {self.vehicle_marque}\nModèle ={self.vehicle_modele}\nAnnée = {self.vehicle_annee}\nPrix = {self.vehicle_prix}")

    def demarrer(self): 
        print ("Attention, je roule")

vehicle1 = Vehicle("Mercedes", "Classe A", 2020, 18500)
vehicle1.informationsVehicule()

class Voiture(Vehicle): 
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.voiture_porte = 4

    def informationsVehicule(self):
        print (f"\nMarque = {self.vehicle_marque}\nModèle ={self.vehicle_modele}\nAnnée = {self.vehicle_annee}\nPrix = {self.vehicle_prix}\nNombre de porte = {self.voiture_porte}")

    def demarrer(self): 
        print ("La voiture roule")
        

voiture1 = Voiture("Mercedes", "Classe A", 2020, 18500)
voiture1.informationsVehicule()
voiture1.demarrer()

class Moto(Vehicle): 

    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.moto_roue = 2
    
    def informationsVehicule(self):
        print (f"\nMarque = {self.vehicle_marque}\nModèle ={self.vehicle_modele}\nAnnée = {self.vehicle_annee}\nPrix = {self.vehicle_prix}\nNombre de porte = {self.moto_roue}")

    def demarrer(self): 
        print ("La moto roule")

moto1 = Moto("Yamaha", "1200 Vmax", 1987, 4500)
moto1.informationsVehicule()
moto1.demarrer()


    

    



    

