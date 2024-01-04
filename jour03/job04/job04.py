class Joueur: 

    def __init__(self, nom, numero, position, nb_but, passe_decisive, carton_jaune, carton_rouge): 
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nb_but = nb_but
        self.passe_decisive = passe_decisive
        self.carton_jaune = carton_jaune
        self.carton_rouge = carton_rouge
    
    def marquerUnBut(self):
        self.nb_but = self.nb_but +1

    def effectuerUnePasseDecisive(self): 
        self.passe_decisive = self.passe_decisive +1

    def recevoirUnCartonJaune(self): 
        self.carton_jaune = self.carton_jaune +1
    
    def recevoirUnCartonRouge(self): 
        self.carton_rouge =  self.carton_rouge +1

    def afficherStatistiques(self): 
        print(f"\n Nom du joueur: {self.nom} \n Numéro du joueur: {self.numero} \n Position du joueur: {self.position} \n Nombre de but: {self.nb_but} \n Passe décisive: {self.passe_decisive} \n Carton jaune: {self.carton_jaune} \n Carton rouge: {self.carton_rouge}")


class Equipe: 

    def __init__(self, nom): 
        self.equipe_nom = nom
        self.liste_joueur = []

    def ajouterJoueur(self, nouveau_joueur):
        self.liste_joueur.append(nouveau_joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Voici les statistiques des joueurs de l'équipe {self.equipe_nom}:")
        for joueur in self.liste_joueur:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, buts=0, passes=0, cartons_jaunes=0, cartons_rouges=0 ): 
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                joueur.nb_but += buts
                joueur.passe_decisive += passes
                joueur.carton_jaune += cartons_jaunes
                joueur.carton_rouge += cartons_rouges

info_joueur1 = Joueur("Kevin", 21, "Attaquant", 1, 10, 2, 3 )
info_joueur1.afficherStatistiques()
info_joueur2 = Joueur("Lucas", 24, "Défense", 3, 10, 5, 1)
info_joueur2.afficherStatistiques()
info_joueur3 = Joueur("Lucy", 24, "Buteur", 1, 4, 2, 2 )
info_joueur3.afficherStatistiques()
info_joueur4 = Joueur("Ines", 6, "Milieu", 2, 5, 3, 4 )
info_joueur4.afficherStatistiques()  

# info_joueur1.marquerUnBut()
# info_joueur1.effectuerUnePasseDecisive()
# info_joueur1.recevoirUnCartonJaune()
# info_joueur1.recevoirUnCartonRouge()

info_equipe1 = Equipe("Bayern Munich")
info_equipe1.ajouterJoueur(info_joueur1)
info_equipe1.ajouterJoueur(info_joueur2)

info_equipe2 = Equipe("Real Madrid")
info_equipe2.afficherStatistiquesJoueurs()
info_equipe2.ajouterJoueur(info_joueur3)

info_equipe2.ajouterJoueur(info_joueur4)
info_equipe2.mettreAJourStatistiquesJoueur()

