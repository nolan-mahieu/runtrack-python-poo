class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}, Année: {self.annee}, Prix: {self.prix}")

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")

    def demarrer(self):
        print("Attention, la voiture roule")

class Moto(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roue}")

    def demarrer(self):
        print("Attention, la moto roule")

ma_voiture = Voiture("Mercedes classe A", 2020, 18500)
ma_moto = Moto("Yamaha Vmax", 1987, 4500)

ma_voiture.informationsVehicule()
ma_moto.informationsVehicule()

ma_voiture.demarrer()
ma_moto.demarrer()
