class Livre: 

    def __init__(self, disponible): 
        self.__disponible = disponible

    def get_disponible(self):
        return self.__disponible 

    def set_disponible(self, disponible): 
        self.__disponible = disponible

    def verification(self): 
        if self.get_disponible() == True: 
            return self.get_disponible() 
        else: 
            return self.get_disponible() 
    
    def emprunter(self): 
        if self.verification() ==  True:
            self.set_disponible(False)
    
    def rendre(self): 
        if self.emprunter() == False: 
            self.set_disponible(True)