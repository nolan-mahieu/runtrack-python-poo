class Animal:
    def __init__(self):
        self.age = 0 
        self.prenom = ""

    def vieillir(self):
        self.age += 1

animal = Animal()

print(f"L'âge de l'animal {animal.age} ans")

animal.vieillir()

print("#L'âge de l'animal après appel la fonction vieillir")

print(f"L'âge de l'animal {animal.age} ans")