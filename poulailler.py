from poule import Poule
import random

class Poulailler:
    def __init__(self):
        self.budget = 50
        self.nb_poules = 4
        self.nb_coqs = 1
        self.nourriture = 0
        self.eau = 0
        self.poules = []
        self.oeufs =0

        for i in range(self.nb_poules):
            self.poules.append(Poule())
    
    def vendre_oeufs(self):
        prix_oeuf = 1
        quantite = int(input("Combien d'oeufs voulez-vous vendre ? "))

        if quantite <= self.oeufs:
            prix_total = prix_oeuf * quantite
            self.budget += prix_total
            self.oeufs -= quantite
            print(f"Vente de {quantite} oeufs effectuée.")
        else:
            print("Vous n'avez pas assez d'oeufs.")
    def acheter_poule(self):
        prix_poule = 10

        if self.budget >= prix_poule:
            self.budget -= prix_poule
            self.nb_poules += 1
            self.poules.append(Poule())
            print("Vous avez acheté une nouvelle poule.")
        else:
            print("Vous n'avez pas assez d'argent.")
    
    def vendre_poussins(self):
        prix_poussin = 10
        quantite = int(input("Combien de poussins voulez-vous vendre ? "))

        if quantite <= self.nb_poussins:
            prix_total = prix_poussin * quantite
            self.budget += prix_total
            self.nb_poussins -= quantite
            print(f"Vente de {quantite} poussins effectuée.")
        else:
            print("Vous n'avez pas assez de poussins.")
    def ajouter_coq(self):
        prix_coq = 20

        if self.budget >= prix_coq:
            self.budget -= prix_coq
            self.nb_coqs += 1
            print("Vous avez acheté un nouveau coq.")
        else:
            print("Vous n'avez pas assez d'argent.")
    def acheter_nourriture(self):
        prix_nourriture = 5
        kg_nourriture = 20
        quantite = int(input("Combien de kilogrammes de nourriture voulez-vous acheter ? "))
        prix_total = prix_nourriture * quantite

        if prix_total <= self.budget:
            self.budget -= prix_total
            self.nourriture += kg_nourriture * quantite
            print(f"Achat de {quantite} kg de nourriture effectué.")
        else:
            print("Vous n'avez pas assez d'argent.")

    def acheter_eau(self):
        prix_eau = 10
        litre_eau = 100
        quantite = int(input("Combien de litres d'eau voulez-vous acheter ? "))
        prix_total = prix_eau * quantite

        if prix_total <= self.budget:
            self.budget -= prix_total
    
