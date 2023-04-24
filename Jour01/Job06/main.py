class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Accesseurs (getters)
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs (setters)
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur


# Création d'un rectangle avec longueur 10 et largeur 5
rect = Rectangle(10, 5)

# Affichage des valeurs initiales
print(f"Longueur: {rect.get_longueur()}, Largeur: {rect.get_largeur()}")

# Modification des valeurs de longueur et largeur
rect.set_longueur(15)
rect.set_largeur(8)

# Vérification que les modifications sont bien prises en compte
print(f"Longueur: {rect.get_longueur()}, Largeur: {rect.get_largeur()}")