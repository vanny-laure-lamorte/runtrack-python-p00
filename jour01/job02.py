class Operation ():
    def __init__(self, nombre1, nombre2):
        self.op_nombre1 = nombre1
        self.op_nombre2 = nombre2

    def afficher_nombre (self):
        print (f"Le nombre1 est {self.op_nombre1} ")
        print (f"Le nombre2 est {self.op_nombre2}")

afficher = Operation(12 , 3)
afficher.afficher_nombre()