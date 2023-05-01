import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()

    def creer_paquet(self):
        valeurs = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
        couleurs = ['Coeur', 'Carreau', 'Trefle', 'Pique']
        paquet = [Carte(v, c) for v in valeurs for c in couleurs]
        random.shuffle(paquet)
        return paquet

    def piocher(self):
        return self.paquet.pop()

    def calculer_score(self, main):
        score = 0
        as_count = 0
        for carte in main:
            if carte.valeur in ['J', 'Q', 'K']:
                score += 10
            elif carte.valeur == 'A':
                score += 11
                as_count += 1
            else:
                score += int(carte.valeur)

            while score > 21 and as_count > 0:
                score -= 10
                as_count -= 1

        return score

    def jouer(self):
        main_joueur = [self.piocher(), self.piocher()]
        main_croupier = [self.piocher(), self.piocher()]

        while True:
            print(f"Votre main: {', '.join(str(c) for c in main_joueur)} - Score: {self.calculer_score(main_joueur)}")
            print(f"Main du croupier: {main_croupier[0]}")

            action = input("Souhaitez-vous piocher (P) ou passer (S) ? ").lower()
            if action == 'p':
                main_joueur.append(self.piocher())
                if self.calculer_score(main_joueur) > 21:
                    print("Vous avez dépassé 21. Vous avez perdu.")
                    return
            elif action == 's':
                break

        while self.calculer_score(main_croupier) < 17:
            main_croupier.append(self.piocher())

        print(f"Main du croupier: {', '.join(str(c) for c in main_croupier)} - Score: {self.calculer_score(main_croupier)}")

        if self.calculer_score(main_croupier) > 21 or self.calculer_score(main_joueur) > self.calculer_score(main_croupier):
            print("Félicitations! Vous avez gagné.")
        else:
            print("Le croupier a gagné.")

if __name__ == '__main__':
    jeu = Jeu()
    jeu.jouer()