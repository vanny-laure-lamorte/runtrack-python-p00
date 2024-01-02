class Personne: 
    def __init__(self, nom, prenom): 
        self.user_name = nom
        self.user_prenom = prenom

    def SePresenter (self):
        print (f"Je suis {self.user_name} {self.user_prenom}")

user_data = Personne("John", "Doe")
user_data.SePresenter()

user_data = Personne("Jean", "Dupond")
user_data.SePresenter()

    