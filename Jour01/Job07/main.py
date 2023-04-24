class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_page = nombre_de_pages

    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nombre_de_page(self):
        return self.__nombre_de_page
    
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_page = nombre_de_pages
        else:
            print("Erreur: le nombre de pages doit être un nombre entier positif.")

livre = Livre("Naruto", "Masashi Kishimoto", 120)

print(f"Titre: {livre.get_titre()}, Auteur: {livre.get_auteur()}, Nombre de pages: {livre.get_nombre_de_page()}")

livre.set_titre("Naruto - Akatsuki")
livre.set_auteur("Masashi Kishimoto")
livre.set_nombre_de_pages(190)

print(f"Titre: {livre.get_titre()}, Auteur: {livre.get_auteur()}, Nombre de pages: {livre.get_nombre_de_page()}")

livre.set_nombre_de_pages(-5)