class Commande: 

    def __init__(self, num_commande, statut_commande): 
        self.__num_commande = num_commande
        self.__liste_plat = { }
        self.__statut_commande = statut_commande
    
    def get_num_commande(self):
        return self.__num_commande
    def get_liste_plat(self):
        return self.__liste_plat
    def get_statut_commande(self): 
        return self.__statut_commande
    
    def set_num_commande(self, num_commande):
        self.__num_commande = num_commande
    def set_plat_commande(self, liste_plat):
        self.__liste_plat = liste_plat
    def set_statut_commande(self, statut_commande): 
        self.__statut_commande = statut_commande
    
    def ajouter_plat(self, nom_plat, prix_plat):
        self.__liste_plat[nom_plat] = prix_plat
    
    def annuler_plat(self):
        self.__statut_commande = "Annulée"        

    def __calculer_total_commande(self):
        total = 0
        prix = list(self.__liste_plat.values())
        for i in range(len(self.__liste_plat)):
            total += prix[i]
        total += self.TVA()
        return total
    
    def TVA(self):
        total_TVA = 0
        prix = list(self.__liste_plat.values())
        for i in range(len(self.__liste_plat)):
            total_TVA += (prix[i] * 20/100)
        return total_TVA

    def afficher_commande(self):
        print (f""" 
        Le numero de la commande : {self.get_num_commande()} 
        La liste des plats : {self.get_liste_plat()}
        Le total à payer : {self.__calculer_total_commande()}€ 
        Le statut de la commande : {self.get_statut_commande()}""")    

commander1 = Commande(1, "En Cours")
commander1.ajouter_plat("Gambas plancha", 15)
commander1.ajouter_plat("Paella", 20)
commander1.ajouter_plat("Churros", 9 )

commander1.annuler_plat()
commander1.afficher_commande()