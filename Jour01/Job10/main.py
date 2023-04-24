class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, reservoir=50, en_marche=False):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__reservoir = reservoir
        self.__en_marche = en_marche

    def get_marque(self):
        return self.__marque

    def set_marque(self, marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, modele):
        self.__modele = modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, annee):
        self.__annee = annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def __verifier_plein(self):
        return self.__reservoir

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
        else:
            print("Le réservoir est trop faible pour démarrer la voiture.")

    def arreter(self):
        self.__en_marche = False

# Exemple d'utilisation de la classe Voiture
ma_voiture = Voiture("Bmw", "Series 3", 2020, 15000)

ma_voiture.set_marque("Bmw")
ma_voiture.set_modele("Series 3")
ma_voiture.set_annee(2021)
ma_voiture.set_kilometrage(20000)

ma_voiture.demarrer()
print(ma_voiture.get_en_marche())

ma_voiture.arreter()
print(ma_voiture.get_en_marche())