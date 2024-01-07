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
        if nouveau_joueur not in self.liste_joueur:
            self.liste_joueur.append(nouveau_joueur)
        else: 
            print("Erreur: le joueur est déjà dans l'équipe")

    def afficherStatistiquesJoueurs(self):
        print(f"Voici les statistiques des joueurs de l'équipe {self.equipe_nom}:")
        for i in self.liste_joueur:
            i.afficherStatistiques()
        print(" ")

    def mettreAJourStatistiquesJoueur(self, nom, buts=0, passes=0, cartons_jaunes=0, cartons_rouges=0 ): 
        for joueur in self.liste_joueur:
            if joueur.nom == nom:
                joueur.nb_but += buts
                joueur.passe_decisive += passes
                joueur.carton_jaune += cartons_jaunes
                joueur.carton_rouge += cartons_rouges

# Création des joueurs
info_joueur1 = Joueur("Kevin", 21, "Gardien", 0, 0, 0, 0)
info_joueur2 = Joueur("Lucas", 24, "Défense", 3, 10, 5, 1)
info_joueur3 = Joueur("Lucy", 24, "Buteur", 1, 4, 2, 2 )
info_joueur4 = Joueur("Ines", 6, "Milieu", 2, 5, 3, 4 )

#Création des équipes
info_equipe1 = Equipe("Bayern Munich")
info_equipe1.ajouterJoueur(info_joueur1)
info_equipe1.ajouterJoueur(info_joueur2)

info_equipe2 = Equipe("Real Madrid")
info_equipe2.ajouterJoueur(info_joueur3)
info_equipe2.ajouterJoueur(info_joueur4)

# Afficher les statistiques des joueurs par equipes
info_equipe1.afficherStatistiquesJoueurs()
info_equipe2.afficherStatistiquesJoueurs()

# Mis à jour des statistiques du joueur
info_equipe1.mettreAJourStatistiquesJoueur("Lucy", 0, 1, 2, 1 )

# Simulation match
info_joueur1.marquerUnBut()
info_joueur2.marquerUnBut()
info_joueur3.recevoirUnCartonJaune()
info_joueur4.effectuerUnePasseDecisive()
info_joueur2.marquerUnBut()
info_joueur3.recevoirUnCartonRouge()

# Statistiques après le match
info_equipe1.afficherStatistiquesJoueurs()
info_equipe2.afficherStatistiquesJoueurs()

