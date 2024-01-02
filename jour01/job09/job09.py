class Produit: 

    def __init__(self, nom, prixHT, TVA ):
        self.produit_nom = nom
        self.produit_prixHT = prixHT
        self.produit_TVA = TVA
        
    def CalculerPrixTTC (self):         
        prix_TTC = self.produit_prixHT + self.produit_prixHT*self.produit_TVA
        return prix_TTC

    def afficher(self): 
        self.CalculerPrixTTC()
        return f"""
        Le nom du produit: {self.produit_nom} 
        Le prix HT: {self.produit_prixHT}€ 
        La TVA: {self.produit_TVA}
        Le prix TTC: {self.CalculerPrixTTC()}€ 
        """
 
prix_final = Produit("Saucisson", 4.5, 0.28)
print (prix_final.afficher())

prix_final = Produit("Jambon Cru", 5, 0.28)
print (prix_final.afficher())

prix_final = Produit("Coppa", 3, 0.28)
print (prix_final.afficher())





    