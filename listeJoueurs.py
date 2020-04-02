# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module listeJoueurs
   ~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la liste des joueurs. 
"""
import random
from joueur import *

def ListeJoueurs(nomsJoueurs):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    listejoueurs=[]
    for elem in nomsJoueurs:
      listejoueurs.append(Joueur(elem))
    return listejoueurs

joueurs=ListeJoueurs(['jason','emerick','toto'])
def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs.append(joueur)

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs un liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
<<<<<<< HEAD
<<<<<<< HEAD
    pass


def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
    random.shuffle(joueurs)

=======
    random.shuffle(joueurs)
>>>>>>> origin/master
=======
    random.shuffle(joueurs)
    
>>>>>>> origin/master
def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=2):
    """
    distribue de manière aléatoire des trésors entre les joueurs.
    paramètres: joueurs la liste des joueurs
                nbTresors le nombre total de trésors à distribuer (on rappelle 
                        que les trésors sont des entiers de 1 à nbTresors)
                nbTresorsMax un entier fixant le nombre maximum de trésor 
                             qu'un joueur aura après la distribution
                             si ce paramètre vaut 0 on distribue le maximum
                             de trésor possible  
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    if nbTresorMax == 0:
<<<<<<< HEAD
        pass
=======
      nbTresorMax = nbTresors
>>>>>>> origin/master
    for i in range(nbTresors):
      if i<nbTresorMax:
        nb_aleatoire=random.randint(0,len(joueurs))
        joueurs[nb_aleatoire]["tresor"].append(i)
    #pas claire

def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """   
    d=joueurs[1]
    joueurs[1]=joueurs[0]
    joueurs[0]=d

def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    return len(joueurs)

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le joueur courant
    """
    return joueurs[0]

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
<<<<<<< HEAD
    del(joueurs[0]["tresor"][0])
=======
    tresorTrouve(joueurs[0])
>>>>>>> origin/master

def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésors restant pour le joueur dont le numéro 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
<<<<<<< HEAD
    return len(joueurs[numJoueur]["tresor"])
=======
    return getNbTresorsRestants(joueurs[numJoueur])
>>>>>>> origin/master

def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    #demander au prof
    pass

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
<<<<<<< HEAD
    return joueurs[0]["nom"]
=======
    return getNom(joueurs[0])
>>>>>>> origin/master

def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
<<<<<<< HEAD
    return joueurs[numJoueur]["nom"]
=======
    return getNom(joueurs[numJoueur])
>>>>>>> origin/master

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    return prochainTresor(joueurs[numJoueur])

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    return prochainTresor(joueurs[0])

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
<<<<<<< HEAD
    pass
<<<<<<< HEAD


=======
>>>>>>> origin/master
=======
    if getNbTresorsRestants(joueurs[0]) == []:
      return True
    else : 
      return False
    
>>>>>>> origin/master
if __name__=='__main__':
  j=joueurs
  print(j)
  ajouterJoueur(j, 'momo')
  print(j)
  initAleatoireJoueurCourant(j)
  print(j)
  print(distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0))
  print(j)
  print(changerJoueurCourant(joueurs))
  print(getNbJoueurs(joueurs))
  print(j)
  print(getJoueurCourant(joueurs))
  print(nbTresorsRestantsJoueur(joueurs,numJoueur=0))
  print(numJoueurCourant(joueurs))
<<<<<<< HEAD
<<<<<<< HEAD
  print(nomJoueurCourant(joueurs))
=======
  print(nomJoueurCourant(joueurs))
>>>>>>> origin/master
=======
  print(nomJoueurCourant(joueurs))


>>>>>>> origin/master
