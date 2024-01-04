class Ville: 

    def __init__(self, nom, nb_habitant):
        self.__ville_nom = nom
        self.__ville_nb_habitant = nb_habitant
        
    def get_nom(self): 
        return self.__ville_nom
    def get_nb_habitant(self):
        return self.__ville_nb_habitant 

    def set_nom (self, nom):
        self.__ville_nom = nom
    def set_nb_habitant (self, nb_habitant):
        self.__ville_nb_habitant = nb_habitant

class Personne: 

    def __init__(self, nom, age, obj_ville): 
        self.__personne_nom = nom 
        self.__personne_age = age
        self.__personne_obj_ville = obj_ville
    
    def get_personne_nom(self): 
        return self.__personne_nom    
    def get_personne_age(self): 
        return self.__personne_age 
    def get_personne_objet(self):
        return self.__personne_objet
    
    def set_personne_nom(self, nom ): 
        self.__personne_nom = nom         
    def set_personne_age(self,age ): 
        self.__personne_age = age      
    def set_personne_objet(self, objet):
        self.__personne_objet = objet
    
    def ajouterPopulation(self):
        population = self.obj_ville.get_nb_habitant() 
        self.obj_ville.set_nb_habitant(population +1)

obj_paris = Ville("Paris", 1000000)
print(f"Population de la ville de Paris : {obj_paris.get_nb_habitant()} habitants")

obj_marseille = Ville("Marseille", 861635)
print(f"Population de la ville de Marseille : {obj_marseille.get_nb_habitant()} habitants")

John = Personne ("John", 45, obj_paris)
Myrtille = Personne("Myrtille", 4, obj_paris)
Chloé = Personne("Chloé", 18, obj_marseille )

print(f"Mis à jour de la popullation de la ville {obj_paris.get_nom} {obj_paris.get_nb_habitant}")

print(f"Mis à jour de la popullation de la ville {obj_marseille.get_nom} {obj_marseille.get_nb_habitant}")

     




