class CompteBancaire: 

    def __init__(self, num_compte, nom, prenom, solde):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.decouvert = True 
    
    def get_num_compte(self): 
        return self.__num_compte
    def get_nom(self):
        return self.__nom
    def get_prenom(self):
        return self.__prenom
    def get_solde(self):
        return self.__solde
    
    def set_num_compte(self,num_compte ): 
        self.__num_compte = num_compte        
    def set_nom(self, nom):
        self.__nom = nom        
    def set_prenom(self, prenom):
        self.__prenom = prenom        
    def set_solde(self, solde):
        self.__solde = solde

    def afficher(self):
        print (f"\n Nom : {self.get_nom()}\n Prénom : {self.get_prenom()}\n Numéro de compte : {self.get_num_compte()}")

    def afficherSolde(self): 
        print(f"\n Votre solde est de {self.get_solde()}€")

    def versement(self, montant_versement): 
        self.__solde = self.__solde + montant_versement     
        
    def retrait(self, montant_retrait): 
        if self.__solde >= montant_retrait:
            self.__solde = self.__solde - montant_retrait
            return True
        else: 
            print("Solde insuffisant pour le retrait")
            self.agios()
            return False
        
    def agios(self): 
        if self.__solde <= 0:
            self.__solde = self.__solde - 5       

    def virement(self, destinataire_compte, montant):
        if self.retrait(montant): 
            destinataire_compte.versement(montant)
            print (f"\n Le virement à bien été effectué.")
        else:
            print (f"Erreur. Le virement n'a pas fonctionné")

  
compte1 = CompteBancaire("123456789", "Madec", "Lucy", 200)
compte1.afficher()
compte1.afficherSolde()

compte1.versement(50)
compte1.afficherSolde()

compte1.retrait(25)
compte1.afficherSolde()

compte2 = CompteBancaire("987654321", "Ines", "Lorquet", -50)
compte2.afficher()
compte2.afficherSolde()

compte1.virement(compte2, 50)
compte2.afficherSolde()

compte1.afficher()
compte1.afficherSolde()
