import random

class Carte:

    # Initialisation d'une carte avec une valeur et une couleur
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def afficher(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        self.paquet = self.creerPaquet()

    # Création d'un paquet de cartes
    def creerPaquet(self):        
        couleurs = ["pique", "coeur", "carreau", "trèfle"]
        valeurs = ["as", 2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi"]
        return [Carte(valeur, couleur) for couleur in couleurs for valeur in valeurs]
    
    # Retire et renvoie une carte du paquet
    def tirerUneCarte(self):        
        return self.paquet.pop()
    
    # Assignation de valeurs aux cartes en fonction des règles du Blackjack
    def valeurCarte(self, carte):
        return 10 if carte.valeur in ["valet", "dame", "roi"] else 11 if carte.valeur == "as" else carte.valeur
    
    # Calcul de la valeur totale d'une main en ajustant la valeur des As si nécessaire
    def valeurMain(self, main):  
        total = sum(self.valeurCarte(carte) for carte in main)
        as_values = [carte for carte in main if carte.valeur == "as"]
        for as_carte in as_values:
            if total > 21:
                total -= 10
        return total

    # Affiche les cartes d'une main pour un joueur donné
    def afficherMain(self, main, joueur=""):
        main_str = ", ".join(carte.afficher() for carte in main)
        print(f"Main de {joueur}: {main_str}")

    # Réalise un tour pour un joueur en lui permettant de tirer des cartes
    def tour(self, joueur):
        main = [self.tirerUneCarte() for _ in range(2)]
        self.afficherMain(main, joueur)

        while self.valeurMain(main) < 21 and input(f"Tirer une carte, {joueur} ? (O/N)").lower() == "o":
            carte = self.tirerUneCarte()
            main.append(carte)
            self.afficherMain(main, joueur)
        return main

    def jouer(self):
        joueur = "Joueur"
        croupier = "Croupier"

        # Tours du joueur et du croupier
        main_joueur = self.tour(joueur)
        if self.valeurMain(main_joueur) <= 21:
            main_croupier = self.tour(croupier)
            while self.valeurMain(main_croupier) < 17:
                carte = self.tirerUneCarte()
                main_croupier.append(carte)
                self.afficherMain(main_croupier, croupier)

            # Affichage des mains du joueur et du croupier
            self.afficherMain(main_joueur, joueur)
            self.afficherMain(main_croupier, croupier)

            # Détermination du gagnant
            if self.valeurMain(main_joueur) > 21 or (self.valeurMain(main_croupier) <= 21 and self.valeurMain(main_croupier) > self.valeurMain(main_joueur)):
                print("La banque gagne !")
            else:
                print("Vous avez gagné !")
        else:
            print("Vous avez perdu")

# Initialisation du jeu de Blackjack et lancement du jeu
blackJack = Jeu()
blackJack.jouer()
