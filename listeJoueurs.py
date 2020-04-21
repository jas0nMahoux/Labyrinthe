import random
from joueur import *

def ListeJoueurs(nomsJoueurs):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    joueurs={}
    Liste_Joueurs=[]
    for joueur in nomsJoueurs:
      Liste_Joueurs.append(Joueur(joueur))
    joueurs["liste_joueurs"]=Liste_Joueurs
    joueurs["joueur_Courant"]=0
    return joueurs


def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs["liste_joueurs"].append(joueur)
    

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs une liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs["joueur_Courant"]=random.choice(list(range(0,len(joueurs["liste_joueurs"]))))
    

def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
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
    tresor= list(range(1,nbTresors+1))
    random.shuffle(tresor)
    if nbTresorMax==0:
      i=0
      stop=False
      while i<len(tresor):
        cpt=0
        while cpt<len(joueurs["liste_joueurs"]) and i<len(tresor):
          ajouterTresor(joueurs["liste_joueurs"][cpt],tresor[i])
          cpt+=1
          i+=1
      nombre_Joueurs=getNbJoueurs(joueurs)
      if nbTresors%nombre_Joueurs!=0:
        if (nbTresors-1)%nombre_Joueurs==0:
          tresorTrouve(joueurs["liste_joueurs"][0])
        elif (nbTresors-2)%nombre_Joueurs==0:
          tresorTrouve(joueurs["liste_joueurs"][0])
          tresorTrouve(joueurs["liste_joueurs"][1])
        elif (nbTresors-3)%nombre_Joueurs==0:
          tresorTrouve(joueurs["liste_joueurs"][0])
          tresorTrouve(joueurs["liste_joueurs"][1])
          tresorTrouve(joueurs["liste_joueurs"][2])          
    if nbTresorMax!=0:
      i=0
      stop=False
      while i<(len(joueurs)*nbTresorMax) and stop==False:
        cpt=0
        if len(tresor)==0:
            stop=True
        while cpt<len(joueurs) and stop==False:
          if i<len(tresor):
            stop=True
          ajouterTresor(joueurs["liste_joueurs"][cpt],tresor[i])
          cpt+=1
          i+=1



def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    if (joueurs["joueur_Courant"]+1)==len(joueurs["liste_joueurs"]):
      joueurs["joueur_Courant"]=0
    else:
      joueurs["joueur_Courant"]+=1

def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    return len(joueurs["liste_joueurs"])

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le joueur courant
    """
    return joueurs["liste_joueurs"][joueurs["joueur_Courant"]]

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    tresorTrouve(joueurs["liste_joueurs"][joueurs["joueur_Courant"]])

def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésors restant pour le joueur dont le numéro 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    return getNbTresorsRestants(joueurs["liste_joueurs"][numJoueur-1])

def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    return joueurs["joueur_Courant"]

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    return getNom(joueurs["liste_joueurs"][joueurs["joueur_Courant"]])

def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    return getNom(joueurs["liste_joueurs"][numJoueur-1])

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    return prochainTresor(joueurs["liste_joueurs"][numJoueur-1])

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    return prochainTresor(joueurs["liste_joueurs"][joueurs["joueur_Courant"]])

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
    if prochainTresor(joueurs["liste_joueurs"][joueurs["joueur_Courant"]])==None:
      return True
    else:
      return False

if __name__=="__main__":
  Li=(ListeJoueurs(["jason","emerick"]))
  print(Li)
  print(initAleatoireJoueurCourant(Li))
  print(Li)
  print(ajouterJoueur(Li,Joueur("Damien")))
  print(Li)
  print(distribuerTresors(Li,nbTresors=30, nbTresorMax=11))
  print(Li)
  print(changerJoueurCourant(Li))
  print(Li)
  print(getNbJoueurs(Li))
  print(getJoueurCourant(Li))
  print(joueurCourantTrouveTresor(Li))
  print(nbTresorsRestantsJoueur(Li,1))
  print(numJoueurCourant(Li))
  print(nomJoueurCourant(Li))
  print(nomJoueur(Li,2))
  print(prochainTresorJoueur(Li,2))
  print(Li)
  print(tresorCourant(Li))
  print(joueurCourantAFini(Li))