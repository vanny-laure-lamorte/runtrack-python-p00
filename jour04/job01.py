class Personne: 
    def __init__(self, age=14): 
        self.personne_age = age

    def afficherAge(self):
        print (f"Vous avez {self.personne_age} ans")

    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, nouvel_age):
        if type(nouvel_age) == int: 
            self.personne_age = nouvel_age
            print(f"Le nouvel age de la personne {nouvel_age}ans")
        else: 
            print("L'age doit être un nombre entier.")

class Eleve(Personne):

    def alleEnCours(self): 
        print("Je vais cours")

    def afficherAge(self): 
        print(f"J'ai {self.personne_age} ans")

class Professeur:

    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee
    
    def get_matiereEnseignee(self): 
        return self.__matiereEnseignee
    
    def set_matiereEnseignee(self, matiereEnseignee): 
        self.__matiereEnseignee = matiereEnseignee
    
    def enseigner(self): 
        print("Le cours va commencer")


info_personne1 = Personne()
info_personne1.afficherAge()
        
info_eleve1 = Eleve()
info_eleve1.afficherAge()

