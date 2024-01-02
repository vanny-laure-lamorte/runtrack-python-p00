class Animal: 
    def __init__(self, age, prenom):
        self.data_age = age
        self.data_prenom = prenom

    def vieillir(self): 
        self.data_age = self.data_age + 1
        print(f"L'age de l'animal {self.data_age}")
    
    def nommer(self, prenom): 
        print (f"L'animal se nomme {prenom}")    

age_animal = Animal(0 , " ")
age_animal.vieillir()

prenom_animal = Animal(0, "")
prenom_animal.nommer("Luna")