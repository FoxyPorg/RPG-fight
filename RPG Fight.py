from random import randint
import Pickle #

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

###########################################
#                Fonctions                #
###########################################

def Initialisation():
    Combat=int(input("Entrez le nombre de combats"))
    NbDeJoueur=int(input("Entrez le nombre de joueur:"))


def affichage_etat_partie(tour):
    print("--- Etat de la partie ---")
    print(">>> Etat des joueurs :")
    print(">>>Statistiques de l'ennemie:")
    print(">>> Statistiques de la partie:")


def attaque():
    print("a")


def DeroulementDuJeu():
    Initialisation()
    for A in range (Combat):

        for I in range(tour):
            print("le Joueur {}".format(NumDuJoueur))
            affichage_etat_partie(1)
            attaque(Foxy)


##################################################
#                    Classes                     #
##################################################

class Joueur: # Classe definissant chaque Joueurs
    def __init__(self, PV_joueur, Chance_joueur):
        self.Capacite=input("Capacitées possibles: \n Coup de Poing \n Coup de Pied \n ")
        self.PV = PV_joueur
        self.Chance = Chance_joueur
        self.Force = 10
        self.Vitesse = 10
        self.Endurance = 10
        self.avancement = 0


class Ennemie: # Classe definissant chaque Ennemie
    def __init__(self):
        self.PV = 100
        self.Chance = 10
        self.Force = 10
        self.Vitesse = 20
        self.Endurance = 10


class Competences: # Classe definissant chaque Competences
    def __init__(self):
        self.PV = 25
        self.Physique = 1
        self.Distance = 0
        self.flashbang = 0

###########################################
# Definition des valeurs pour les classes #
###########################################

Foxy = joueur(250, 0, 100, 10, 5, 0)
