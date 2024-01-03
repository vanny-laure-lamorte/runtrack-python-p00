class Livre: 

    def __init__(self, titre, auteur,nb_page): 
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_page = nb_page

    def get_titre (self): 
        return self.__titre     

    def get_auteur (self): 
        return self.__auteur

    def get_nb_page (self):
        return self.__nb_page

    def set_titre (self, titre): 
        self.__titre = titre     

    def set_auteur (self, auteur):
        self.__auteur = auteur
      
    def set_nb_page (self, nb_page): 
        if type(nb_page) == int and nb_page >= 0:
            self.__nb_page = nb_page
        else: 
            print("Erreur: Veuillez corriger le nombre de pages. Il doit être un entier positif")
    
info_livre = Livre("Jude l'Obscur", "Thomas Hardy", 480 )
print (f"Le titre du livre : {info_livre.get_titre()}\n L'auteur du livre : {info_livre.get_auteur()}\n Le nombre de page : {info_livre.get_nb_page()}\n ")

# Exemple pour afficher un message erreur si le nombre de page est en chiffre décimale.
info_livre.set_titre("Thérèse Raquin")
info_livre.set_auteur("Émile Zola")
info_livre.set_nb_page(288.5)
print (f"\n Le titre du livre:{info_livre.get_titre()}\n L'auteur du livre: {info_livre.get_auteur()}\n Le nombre de page: {info_livre.get_nb_page()}")

# Exemple pour afficher un message erreur si le nombre de page en négatif
info_livre.set_titre("L'Odyssée")
info_livre.set_auteur("Homère")
info_livre.set_nb_page(-162)
print (f"\n Le titre du livre:{info_livre.get_titre()}\n L'auteur du livre: {info_livre.get_auteur()}\n Le nombre de page: {info_livre.get_nb_page()}")

