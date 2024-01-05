class Carte: 
    def __init__(self, couleur, valeur): 
        self.carte_valeur = valeur
        self.carte_couleur= couleur
    
    def valeur_chiffre(self, chiffre): 
        if 2 <= chiffre <= 10 and type(chiffre) == int:              
            self.carte_valeur = chiffre
            print (f"Carte Chiffre: {self.carte_valeur} points")
        else: 
            print("Erreur. Choisir une valeur entre 2 et 10")

    def valeur_figure(self):    
        self.carte_valeur = 10             
        print(f"Carte figure: {self.carte_valeur} points")

    def valeur_as(self, carteas):
        if carteas == 1: 
            self.carte_valeur = 1
            print(f"Carte As: {self.carte_valeur} points")
        elif carteas == 11:
            self.carte_valeur== 11
            print(f"Carte As: {self.carte_valeur} points")

set1 = Carte("Roi", "Rouge" )
set1.valeur_chiffre(3)
set1.valeur_as(11)
set1.valeur_figure()

class Jeu(Carte): 
    def __init__(self, valeur, couleur):
        super().__init__(valeur, couleur)
        self.liste_depart = []   

    def prendre(self, nouvelle_carte):
        self.liste_depart.append(nouvelle_carte)       

    def passer(self): 
        pass

    def croupier_objectif(): 
        pass

    def joueur_ojectif():
        pass

class Joueur: 

    def __init__(self, nom, statut, nb_points): 
        self.joueur_nom = nom
        self.statut = statut
        self.nb_points = nb_points
        self.carte_en_main = []

    def AfficherInfo(self): 
        print(f"\nNom du joeur : {self.joueur_nom}\nStatut du joueur :  {self.statut}\nNombre de points : {self.nb_points}\nCarte en main : {self.carte_en_main}\n")

joueur1 = Joueur("Kevin", "Croupier", 10)
joueur1. AfficherInfo()


        

    
