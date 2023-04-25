class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("L'âge de la personne est :", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, matiere_enseignee, age):
        super().__init__(age)
        self.__matiere_enseignee = matiere_enseignee

    def enseigner(self):
        print("Le cours va commencer")

personne1 = Personne()
eleve1 = Eleve()

eleve1.affichageAge()

eleve1.bonjour()
eleve1.allerEnCours()

# Modification de l'âge de l'élève
eleve1.modifierAge(15)
eleve1.affichageAge()

professeur2 = Professeur("Mathématiques", 40)

professeur2.bonjour()
professeur2.enseigner()