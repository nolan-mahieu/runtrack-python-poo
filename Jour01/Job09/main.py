class Student:
    def __init__(self, nom, prenom, num_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = credits
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Trés bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
        
    def studentInfo(self):
        print(f"Nom: {self.__nom}")
        print(f"Prenom: {self.__prenom}")
        print(f"Id: {self.__num_etudiant}")
        print(f"Niveau: {self.__level}")

jhon_doe = Student("Doe","Jhon",145)

jhon_doe.add_credits(30)
jhon_doe.add_credits(25)
jhon_doe.add_credits(15)

print(f"Le nombre de crédits de jhon Doe est de {jhon_doe._Student__credits} points ")

jhon_doe.studentInfo()