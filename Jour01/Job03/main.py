class Opreation:
    def __init__(self, nombre, nombre2):
        self.nombre1 = 12
        self.nombre2 = 3 

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("Résultat de l'addition :", resultat)

operation = Opreation(12, 3)

operation.addition()