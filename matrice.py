# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module matrice
   ~~~~~~~~~~~~~~~
   
   Ce module gère une matrice. 
"""

#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant 
    valeurParDefaut dans chacune des cases
    paramètres: 
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    l1=[]
    l2=[]
    for i in range(nbColonnes):
        l1.append(valeurParDefaut)
    for i in range(nbLignes):
        l2.append(l1)
    return l2
#matrice = Matrice(7,7,0)
matrice =[[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21],[22,23,24,25,26,27,28]]

def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    return len(matrice)

def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    return len(matrice[0])
   
def getVal(matrice,ligne,colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return matrice[ligne][colonne]

def setVal(matrice,ligne,colonne,valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """
    matrice[ligne][colonne]=valeur 

#------------------------------------------        
# decalages
#------------------------------------------
def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    l1 = matrice[numLig]
    l1.append(nouvelleValeur)
    valeur_a_ejecter=l1[0]
    l1.remove(matrice[numLig][0])
    return valeur_a_ejecter


def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    l1=matrice[numLig]
    l1.insert(0,nouvelleValeur)
    valeur_a_ejecter=l1[-1]
    l1.pop(-1)
    return valeur_a_ejecter
    
def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
<<<<<<< HEAD
<<<<<<< HEAD

=======
=======
>>>>>>> origin/master
    valeur_a_ejecter=matrice[0][numCol]
    for i in range(len(matrice)-1):
      matrice[i][numCol]=matrice[i+1][numCol]
    matrice[-1][numCol]=nouvelleValeur
    return valeur_a_ejecter
<<<<<<< HEAD
>>>>>>> origin/master
=======
>>>>>>> origin/master
def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
<<<<<<< HEAD
<<<<<<< HEAD
    a=matrice[-1][numCol]
    Matrice1=matrice
    for i in matrice:
      matrice[i+1][numCol]=Matrice1[i][numCol]
    matrice[0][numCol]=nouvelleValeur
    return a

if __name__=='__main__':
  Matrice=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[14,15,16,17]]
  print(Matrice)
  print(decalageColonneEnBas(Matrice, 1,12))
  print(Matrice)
=======
=======
>>>>>>> origin/master
    valeur_a_ejecter=matrice[-1][numCol]
    valeur_stocke=[]
    for i in range(len(matrice)-1):
      valeur_stocke.extend(matrice[i+1])
      matrice[i].insert(numCol,valeur_stocke[i])
    #matrice[0][numCol]=nouvelleValeur
    return valeur_a_ejecter
if __name__=="__main__" :
  x=matrice
  print(x)
  print(decalageColonneEnBas(x, numCol=3, nouvelleValeur=9))
<<<<<<< HEAD
  print(x)
>>>>>>> origin/master
=======
  print(x)
>>>>>>> origin/master
