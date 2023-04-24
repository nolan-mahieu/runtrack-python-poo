class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

# Instanciation d'un objet Animal
animal = Animal()

# Affichage de l'attribut âge
print(f"L'âge de l'animal {animal.age} ans")

# Appel de la méthode "vieillir"
animal.vieillir()

# Affichage de la phrase demandée
print("#L'âge de l'animal après appel la fonction vieillir")

# Affichage de l'attribut âge après avoir fait vieillir l'animal
print(f"L'âge de l'animal {animal.age} ans")

# Nommer l'animal
animal.nommer("Luna")

# Affichage du nom de l'animal en console
print(f"L'animal se nomme {animal.prenom}")