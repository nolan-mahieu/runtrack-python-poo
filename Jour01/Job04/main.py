class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"je suis {self.nom} {self.prenom}"
    
personne1 = Personne("Jhon", "Doe")
personne2 = Personne("Jean", "Dupont")

print(personne1.SePresenter())
print(personne2.SePresenter())