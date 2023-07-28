import random

class Poule:
    def __init__(self):
        self.etat_physique = 100
        self.moral = 100
        self.est_malade = False
        self.nb_oeufs_jour = 0
        self.est_couve = False

    def calcul_nb_oeufs_jour(self):
        if self.etat_physique >= 75:
            self.nb_oeufs_jour = 3
        elif self.etat_physique >= 50:
            self.nb_oeufs_jour = 2
        elif self.etat_physique >= 25:
            self.nb_oeufs_jour = 1
        else:
            self.nb_oeufs_jour = 0

    def pondre_oeufs(self):
        self.calcul_nb_oeufs_jour()
        oeufs_pondus = random.randint(0, self.nb_oeufs_jour)
        return oeufs_pondus

    def couver_oeufs(self):
        if self.moral >= 70:
            self.est_couve = True
            return True
        else:
            return False

    def manger(self):
        if self.est_malade:
            self.etat_physique -= self.nb_oeufs_jour * 5
        else:
            self.etat_physique += self.nb_oeufs_jour * 10
        self.moral += self.nb_oeufs_jour
        self.moral -= 5

    def tomber_malade(self):
        taux_maladie = random.randint(1, 100)
        if taux_maladie <= 5:
            self.est_malade = True

    def guerir(self):
        self.est_malade = False
        self.etat_physique += 20

    def prendre_vitamines(self):
        if self.etat_physique <= 80:
            self.etat_physique += 20