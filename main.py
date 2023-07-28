from poule import Poule
from poulailler import Poulailler

# Création du poulailler
mon_poulailler = Poulailler()

# Boucle principale du jeu
while True:
    # Affichage de l'état du poulailler
    print(f"Budget restant : {mon_poulailler.budget}€")
    print(f"Nombre de poules : {mon_poulailler.nb_poules}")
    print(f"Nombre de coqs : {mon_poulailler.nb_coqs}")
    print(f"Quantité de nourriture : {mon_poulailler.nourriture} kg")
    print(f"Quantité d'eau : {mon_poulailler.eau} litres")
    print(f"Nombre d'oeufs : {mon_poulailler.oeufs}")

    # Demande au joueur ce qu'il veut faire
    choix = input("\nQue voulez-vous faire ?\n1 - Acheter de la nourriture\n2 - Acheter de l'eau\n3 - Ajouter une poule\n4 - Ajouter un coq\n5 - Vendre des oeufs\n6 - Vendre des poussins\n7 - Terminer la journée\n> ")

    # Traitement du choix du joueur
    if choix == "1":
        mon_poulailler.acheter_nourriture()
    elif choix == "2":
        mon_poulailler.acheter_eau()
    elif choix == "3":
        mon_poulailler.acheter_poule()
    elif choix == "4":
        mon_poulailler.ajouter_coq()
    elif choix == "5":
        mon_poulailler.vendre_oeufs()
    elif choix == "6":
        mon_poulailler.vendre_poussins()
    elif choix == "7":
        # Simulation d'une journée dans le poulailler
        for poule in mon_poulailler.poules:
            oeufs_pondus = poule.pondre_oeufs()
            mon_poulailler.oeufs += oeufs_pondus

            if oeufs_pondus > 0:
                poule.moral += 1

            if poule.est_malade:
                poule.guerir()

            if poule.etat_physique <= 20:
                mon_poulailler.poules.remove(poule)
                print("Une poule est morte !")

            poule.manger()
            poule.tomber_malade()

        # Fin de la journée
        print("La journée est terminée.\n")
        break
    else:
        print("Choix invalide, veuillez réessayer.\n")
