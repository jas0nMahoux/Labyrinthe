# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module plateau
   ~~~~~~~~~~~~~~
   
   Ce module gère le plateau de jeu. 
"""

from matrice import *
from carte import *

def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """
    liste_tresor=[]
    for i in range(nbTresors):
      liste_tresor.append(i+1)
    for i in range(len(matrice)):
      for j in range(len(matrice)):
        nord=random.choice([True,False])
        est=random.choice([True,False])
        sud=random.choice([True,False])
        ouest=random.choice([True,False])
        a=Carte( nord, est, sud, ouest, tresor=0, pions=[])
        if not estValide(a):
          while not estValide(a):
            nord=random.choice([True,False])
            est=random.choice([True,False])
            sud=random.choice([True,False])
            ouest=random.choice([True,False])
            a=Carte( nord, est, sud, ouest, tresor=0, pions=[])
        if len(liste_tresor)==0:
          pass
        elif random.choice([True,False]):
          T=random.choice(liste_tresor)
          a['tresor']=T
          liste_tresor.remove(T)
        setVal(matrice,i,j,a)
    nord=random.choice([True,False])
    est=random.choice([True,False])
    sud=random.choice([True,False])
    ouest=random.choice([True,False])
    b=Carte( nord, est, sud, ouest, tresor=0, pions=[])
    if not estValide(b):
          while not estValide(b):
            nord=random.choice([True,False])
            est=random.choice([True,False])
            sud=random.choice([True,False])
            ouest=random.choice([True,False])
            b=Carte( nord, est, sud, ouest, tresor=0, pions=[])
    setVal(matrice,0,0,Carte(True,False,False,True,0,[1]))
    setVal(matrice,0,2,Carte(True,False,False,False,0,[]))
    setVal(matrice,0,4,Carte(True,False,False,False,0,[]))
    if nbJoueurs>1:
      setVal(matrice,0,6,Carte(True,True,False,False,0,[2]))
    else:
      setVal(matrice,0,6,Carte(True,True,False,False,0,[]))
    setVal(matrice,2,0,Carte(False,False,False,True,0,[]))
    setVal(matrice,2,2,Carte(False,False,False,True,0,[]))
    setVal(matrice,2,4,Carte(True,False,False,False,0,[]))
    setVal(matrice,2,6,Carte(False,True,False,False,0,[]))
    setVal(matrice,4,0,Carte(False,False,False,True,0,[]))
    setVal(matrice,4,2,Carte(False,False,True,False,0,[]))
    setVal(matrice,4,4,Carte(False,True,False,False,0,[]))
    setVal(matrice,4,6,Carte(False,True,False,False,0,[]))
    if nbJoueurs>2:
      setVal(matrice,6,0,Carte(False,False,True,True,0,[3]))
    else:
      setVal(matrice,6,0,Carte(False,False,True,True,0,[]))
    setVal(matrice,6,2,Carte(False,False,True,False,0,[]))
    setVal(matrice,6,4,Carte(False,False,True,False,0,[]))
    if nbJoueurs>3:
      setVal(matrice,6,6,Carte(False,True,True,False,0,[4]))
    else:
      setVal(matrice,6,6,Carte(False,True,True,False,0,[]))
    return (matrice, b)




def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """
    cartesAmovibles=[]
    i=0
    while i<=33:
      if i<=15:
        cartesAmovibles.append(Carte(True,False,False,True,0,[]))
      elif 15<=i<=21:
        cartesAmovibles.append(Carte(True,False,False,False,0,[]))
      else:
        cartesAmovibles.append(Carte(False,True,True,False,0,[]))
      i+=1
    tresors=list(range(tresorDebut,nbTresors+1))
    cpt=0
    for a in cartesAmovibles:
      if cpt>=len(tresors):
        break
      mettreTresor(a,tresors[cpt])
      cpt+=1
    random.shuffle(cartesAmovibles)
    return cartesAmovibles



def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """
    if numTresor==prendreTresor(getVal(plateau[0],lig,col)):
	    return True
    return False

def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """
    if numTresor==prendreTresor(getVal(plateau[0],lig,col)):
	    return True
    return False

def getCoordonneesTresor(plateau,numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    for ligne,l in enumerate(plateau[0]):
      for colone,c in enumerate(l):
        if numTresor==getTresor(c):
          return (ligne ,colone)
    return None

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    for ligne,l in enumerate(plateau[0]):
      for colone,c in enumerate(l):
        for pions in getListePions(c):
          if numJoueur==pions:
            return (ligne ,colone)
    return None

def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    prendrePion(getVal(plateau[0],lin,col),numJoueur)

def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    poserPion(getVal(plateau[0],lin,col), numJoueur)


def accessible(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    
    trouve=False
    STOP=False
    cartes_accessibles=[[ligD,colD]]
    passage=0
    while not trouve and not STOP:
        for carte in cartes_accessibles:
          if carte[0]-1>=0:
            if [carte[0]-1, carte[1]] not in cartes_accessibles:
              if passageNord(plateau[0][carte[0]][carte[1]], plateau[0][carte[0]-1][carte[1]])==True:
                      cartes_accessibles.append([carte[0]-1, carte[1]])
                      passage+=1
          if (carte[0]+1)<7:
              if [carte[0]+1, carte[1]] not in cartes_accessibles:
                  if passageSud(plateau[0][carte[0]][carte[1]], plateau[0][carte[0]+1][carte[1]])==True:
                      cartes_accessibles.append([carte[0]+1, carte[1]])
                      passage+=1
          if (carte[1]-1)>=0:
              if [carte[0], carte[1]-1] not in cartes_accessibles:
                  if passageOuest(plateau[0][carte[0]][carte[1]], plateau[0][carte[0]][carte[1]-1])==True:
                      cartes_accessibles.append([carte[0], carte[1]-1])
                      passage+=1
          if (carte[1]+1)<7:
              if [carte[0], carte[1]+1] not in cartes_accessibles:
                  if passageEst(plateau[0][carte[0]][carte[1]], plateau[0][carte[0]][carte[1]+1])==True:
                      cartes_accessibles.append([carte[0], carte[1]+1])
                      passage+=1
          if [ligA, colA] in cartes_accessibles:
            return True
        if passage==0:
          STOP=True
        passage=0
    return False

def accessibleDist(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin, 
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    pass





if __name__=='__main__':

  x=Plateau(2, 20)
  print(x)
  print(getCoordonneesJoueur(x,2))
  print(accessible(x,1,2,1,5))