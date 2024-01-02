class Cercle: 

    def __init__(self, rayon): 
        self.donnee_rayon = rayon
               
    def changerRayon(self, new_rayon):
        print("Le nouveau rayon est", new_rayon)
        self.donnee_rayon = new_rayon     
        self.circonference()
        self.aire()
        self.diametre()         

    def afficherInfos(self):
        print ("Le rayon du cercle est: ", self.donnee_rayon )

    def circonference(self):
        resultat_circonference = 2 * self.donnee_rayon * 3.14
        print ("La circonference du cercle est :  ", resultat_circonference)

    def aire(self):
        resultat_aire = 3.14 * self.donnee_rayon * self.donnee_rayon
        print ("L'aire du cercle est : ", resultat_aire)

    def diametre(self):
        resultat_diametre = self.donnee_rayon*2
        print ("Le diamètre du cercle est : ", resultat_diametre) 

cercle1 = Cercle(4)
cercle1.afficherInfos()
cercle1.circonference()
cercle1.aire()
cercle1.diametre()

cercle2 = Cercle(7)
cercle2.changerRayon(7)

