# -*- coding: utf-8 -*-

from random import randint

######################
#  Principes de base #
######################
# - Combat tout/tour > combat entre plusieurs joueur et un ennemie (ou plusieurs)
# - 1er tour: choix capacité de chaque combattant
# - Chaque tour, chacun peut attaquer à son tour, perte de pv, choix de capacité nouvelle, immobilisation...
# - On passe ensuite a un autre ennemie

####################
#  Initialisation  #
####################
# - Choix d'une capacité et choix d'un ennemie à attaquer
# - Ennemie choisit une capacité aleatoire
# - La vitesse influe sur l'ordre d'apparition du texte
# - Réduction des Statistiques du joueur et de l'ennemie

#######
# Fin #
#######
# - The End

################################
#           Variables          #
################################

# Joueurs
PV_Joueur = 100
Chance_Joueur = 10
Force_Joueur = 50
Vitesse_Joueur = 10
Endurance_Joueur = 10

# Ennemies
PV_Ennemie = 100
Chance_Ennemie = 10
Force_Ennemie = 50
Vitesse_Ennemie = 10
Endurance_Ennemie = 10

# Compétences
PV_Competence = -25
Physique_Competence = 1
Distance_Competence = 0
Flashbang_Competence = 0

###########################################
#                Fonctions                #
###########################################

def Initialisation():
    NB_Combat=int(input("Entrez le nombre de combats"))
    Nb_Joueur=int(input("Entrez le nombre de joueur:"))
    for I in range (Nb_Joueur):
        Joueur = Joueurs(input("Nom du Joueur:"), int(input("PV du Joueur")), int(input("Chance du joueur")), int(input("Force du Joueur")), int(input("Vitesse du joueur")), int(input("Endurance du joueur")))


def affichage_etat_partie(tour):
    print("--- Etat de la partie ---")
    print(">>> Etat des joueurs :")
    print(">>>Statistiques de l'ennemie:")
    print(">>> Statistiques de la partie:")


def attaque():
    if Joueur.Capacite == "Coup de poing":
        Ennemies(PV_Ennemie) = Ennemies(PV_Ennemie - PV_Competence)
        print(monstre_1.PV_Ennemie)
    if Joueur.Capacite == "Coup de Pied":
        Ennemies(PV_Ennemie) = monstre_1(PV_Ennemie - PV_Competence)
        print(monstre_1.PV_Ennemie)


def apparition_monstre():
    monstre = randint(0, 1)
    if monstre == 1:
        Ennemie.monstre_1()
    elif monstre == 2:
        Ennemie.monstre_2()


def Deroulement_Du_Jeu():
    Initialisation()
    for A in range (NB_Combat):
            print("le Joueur {}".format(NumDuJoueur))
            affichage_etat_partie(A)
            attaque(Joueur)


##################################################
#                    Classes                     #
##################################################

class Joueurs: # Classe definissant chaque Joueurs
    def __init__(self, Nom_Joueur, PV_Joueur, Chance_Joueur, Force_Joueur, Vitesse_Joueur, Endurance_Joueur):
        self.nom = Nom_Joueur
        self.PV = PV_Joueur
        self.Chance = Chance_Joueur
        self.Force = Force_Joueur
        self.Vitesse = Vitesse_Joueur
        self.Endurance = Endurance_Joueur
        self.Capacite=input("Capacitées possibles: \n Coup de Poing \n Coup de Pied \n ")


class Ennemie: # Classe definissant chaque Ennemie
    def __init__(self, PV_Ennemie, Force_Ennemie, Vitesse_Ennemie, Endurance_Ennemie):
        self.PV = PV_Ennemie
        self.Chance = Chance_Ennemie
        self.Force = Force_Ennemie
        self.Vitesse = Vitesse_Ennemie
        self.Endurance = Endurance_Ennemie

    def monstre_1(): # Brute
        monstre_1 = Ennemie(250, 10, 14, 42, 69)

    def monstre_2(): # Voleur
        monstre_2 = Ennemie(10, 100, 5, 120, 200)


class Competences: # Classe definissant chaque Competences
    def __init__(self, PV_Competence, Physique_Competence, Distance_Competence, Flashbang_Competence):
        self.PV = PV_Competence
        self.Physique = Physique_Competence
        self.Distance = Distance_Competence
        self.Flashbang = Flashbang_Competence


#####################################
###    Lancement de la partie     ###
#####################################
Initialisation()
