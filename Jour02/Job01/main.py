class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("L'âge de la personne est", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print(f"jai {self.age} ans")

class Professeur:
    def __init__(self, matiere_enseignee):
        self.__matiere_enseignee = matiere_enseignee

    def enseigner(self):
        print("Le cours vas commencer")

personne1 = Personne()
eleve1 = Eleve()

eleve1.affichageAge()