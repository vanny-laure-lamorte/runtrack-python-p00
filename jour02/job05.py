class Voiture: 
    def __init__(self, marque, modele, annee, kilometrage): 
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.en_marche = False
        self.__reservoir = 50

    def get_marque (self):
        return self.__marque
        
    def get_modele (self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def get_reservoir(self):
        return self.__reservoir    
    
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def demarrer(self): 
        if self.__verifier_plein()> 5:
            self.en_marche = True
            print ("La voiture peut démarrer \n")
        else: 
            print("Attention, vous n'avez pas assez d'essence \n")     
        
    def arreter(self): 
        self.en_marche = False
        print ("La voiture ne peut pas demarrer")

    def __verifier_plein(self): 
        return self.get_reservoir()

car = Voiture("BMV", "Scoop" , 2026, 300000)
print (f"\n La marque de la voiture : {car.get_marque()}\n Le modèle de la voiture : {car.get_modele()}\n L'année de production de la voiture : {car.get_annee()}\n Le kilometrage de la voiture : {car.get_kilometrage()}\n")

car.demarrer()   
car.arreter()
car.set_reservoir(5)
car.demarrer()