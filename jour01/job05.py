class Point: 
    def __init__(self, x, y): 
        self.coordinate_x = x
        self.coordinate_y = y

    def afficherLesPoints(self): 
        print (f"Les coordonnée x : {self.coordinate_x} et les coordonnées x : {self.coordinate_y}")

    def afficher_x(self): 
        print ("Les coordonnées de x : ", self.coordinate_x)

    def afficher_y (self):
        print ("Les coordonnées de x : ", self.coordinate_y)

afficher_coordinates_x_y = Point(10, 20)
afficher_coordinates_x_y.afficherLesPoints()

afficher_point_x= Point (10, 10)
afficher_point_x.afficher_x()

afficher_point_y= Point (20, 40)
afficher_point_y.afficher_y()

afficher_coordinates_x_y = Point(30, 40)
afficher_coordinates_x_y.afficherLesPoints()

