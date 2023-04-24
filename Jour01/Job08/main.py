class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur: le nombre de pages doit être un nombre entier positif.")

    def vérification(self):
        return self.__disponible

    def emprunter(self):
        if self.vérification():
            self.__disponible = False
        else:
            print("Le livre n'est pas disponible.")

    def rendre(self):
        if not self.vérification():
            self.__disponible = True
        else:
            print("Le livre n'a pas été emprunté.")


livre = Livre("Naruto", "Masashi Kishimoto", 120)

print(f"Disponible: {livre.vérification()}")

livre.emprunter()

print(f"Disponible: {livre.vérification()}")

livre.emprunter()

livre.rendre()

print(f"Disponible: {livre.vérification()}")

livre.rendre()