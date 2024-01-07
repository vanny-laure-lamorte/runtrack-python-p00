class Cercle: 

    def __init__(self, rayon): 
        self.donnee_rayon = rayon
               
    def changerRayon(self, new_rayon):
        self.donnee_rayon = new_rayon  
        return new_rayon   

    def afficherInfos(self):
        print("Le rayon du cercle est: ", self.donnee_rayon)
        print ("La circonference du cercle est : ", self.circonference())
        print ("L'aire du cercle est : ", self.aire())
        print ("Le diamètre du cercle est : ", self.diametre() ) 

    def circonference(self):
        resultat_circonference = 2 * self.donnee_rayon * 3.14
        return resultat_circonference
        
    def aire(self):
        resultat_aire = 3.14 * self.donnee_rayon * self.donnee_rayon
        return resultat_aire        

    def diametre(self):
        resultat_diametre = self.donnee_rayon*2
        return resultat_diametre        

cercle1 = Cercle(4)
cercle1.afficherInfos()

cercle2 = Cercle(7)
cercle2.changerRayon(7)
cercle2.afficherInfos()

