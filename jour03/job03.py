class Tache:
    def __init__(self, titre, description, statut='à faire'):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.liste_taches = []

    def ajouterTache(self, tache):
        self.liste_taches.append(tache)

    def supprimerTache(self, titre):
        for tache in self.liste_taches:
            if tache.titre == titre:
                self.liste_taches.remove(tache)
                break

    def marquerCommeFinie(self, titre):
        for tache in self.liste_taches:
            if tache.titre == titre:
                tache.statut = 'terminée'
                break

    def afficherListe(self):
        for tache in self.liste_taches:
            print(f"Titre : {tache.titre}, Description : {tache.description}, Statut : {tache.statut}")

    def filterListe(self, statut):
        filtered_tasks = [tache for tache in self.liste_taches if tache.statut == statut]
        return filtered_tasks

corvee1 = Tache("Ranger", "plier vêtements")
corvee2 = Tache("Nettoyer", "faire la vaiselle")
corvee3 = Tache("Cuisiner", "preparer diner")

liste_de_taches = ListeDeTaches()
liste_de_taches.ajouterTache(corvee1)
liste_de_taches.ajouterTache(corvee2)
liste_de_taches.ajouterTache(corvee3)

print("Liste initiale des tâches :")
liste_de_taches.afficherListe()

liste_de_taches.marquerCommeFinie("Faire les courses")

liste_de_taches.supprimerTache("Faire du sport")

print("\nListe mise à jour des tâches :")
liste_de_taches.afficherListe()

taches_a_faire = liste_de_taches.filterListe('à faire')
print("\nTâches à faire :")
for tache in taches_a_faire:
    print(f"Titre : {tache.titre}, Description : {tache.description}, Statut : {tache.statut}")
