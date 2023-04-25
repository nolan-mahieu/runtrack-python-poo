class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur

rect = Rectangle(5, 3)

print("Périmètre du rectangle :", rect.perimetre())
print("Surface du rectangle :", rect.surface())

rect.set_longueur(6)
rect.set_largeur(4)
print("Nouvelle longueur :", rect.get_longueur())
print("Nouvelle largeur :", rect.get_largeur())
print("Nouveau périmètre :", rect.perimetre())
print("Nouvelle surface :", rect.surface())

para = Parallelepipede(5, 3, 2)

print("Périmètre du parallélépipède :", para.perimetre())
print("Surface du parallélépipède :", para.surface())
print("Volume du parallélépipède :", para.volume())