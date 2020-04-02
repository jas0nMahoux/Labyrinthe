# -*- coding: utf-8 -*-
"""
        Projet Labyrinthe 
        Projet Python 2020 - Licence Informatique UNC (S3 TREC7)
        
   Module carte
   ~~~~~~~~~~~~
   
   Ce module gère les cartes du labyrinthe. 
"""
import random

"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']


def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    c={}
    cardinal=[ouest, sud, est, nord]
    binaire=""
    for i in cardinal:
      if i==True:
        binaire+="1"
      else:
        binaire+="0"
    indice_carte=int(binaire, 2)
    c["carte"]=listeCartes[indice_carte]
    c["tresor"]=tresor
    c["pions"]=pions
    c["mur"]=[nord, est, sud, ouest]
    return c

def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """
    if c["carte"]=='Ø':
      return False
    else: 
      return True


def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    return c['mur'][0] 

    
def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    return c['mur'][2]
    


def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    return c['mur'][1]
    

def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    return c['mur'][3]
    

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c["pions"]

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c["pions"]=listePions

def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    return len(c["pions"])

def possedePion(c,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """
    return pion in c["pions"]

def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c["tresor"]

def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    tresor=c["tresor"]
    c["tresor"]=0
    return tresor


def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    c['tresor']=tresor

def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if len(c["pions"])>0:
      c["pions"].remove(pion)

def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion not in c["pions"]:
      c["pions"].append(pion)

def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    tourner_mur=[]
    for i in range(len(c['mur'])):
      tourner_mur.append(c['mur'][i-1])
    c['mur']=tourner_mur
    
    
def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    tourner_mur=[]
    a=c['mur'][0]
    for i in range(len(c['mur'])-1):
      tourner_mur.append(c['mur'][i+1])
    tourner_mur.append(a)
    c['mur']=tourner_mur

def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    a=random.randint(0,10)
    for i in range(a):
      tournerHoraire(c)

def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire 
    est de la forme bNbEbSbO où bN, bE, bS et bO valent 
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
    c['mur'].reverse()
    cardinal=c['mur']
    binaire=""
    for elem in cardinal:
      if elem==True:
        binaire+="1"
      else:
        binaire+="0"
    return int(binaire, 2)

def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """    
    c['carte']=listeCartes[code]

def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    return c['carte']

def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if carte1['mur'][0]==True:
      return False
    elif carte2['mur'][2]==True:
      return False
    else:
      return True

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if carte1['mur'][2]==True:
      return False
    elif carte2['mur'][0]==True:
      return False
    else:
      return True

def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if carte1['mur'][3]==True:
      return False
    elif carte2['mur'][1]==True:
      return False
    else:
      return True

def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen    
    """
    if carte1['mur'][1]==True:
      return False
    elif carte2['mur'][3]==True:
      return False
    else:
      return True



if __name__=='__main__':
  C=Carte( True, True, False, False, tresor=1, pions=[])
  C1=Carte( False, False, True, True, tresor=1, pions=[])
  print(C1)
  print(C)
  print(estValide(C))
  print(murNord(C))
  print(murSud(C))
  print(murOuest(C))
  print(murEst(C))
  print(getListePions(C))
  print(C)
  setListePions(C,[1,2])
  print(C)
  print(getNbPions(C))
  print(possedePion(C,2))
  print(getTresor(C))
  print(prendreTresor(C))
  print(getTresor(C))
  print(C)
  prendrePion(C, 2)
  print(C)
  poserPion(C, 3)
  print(C)
  print(C['mur'])
  tournerHoraire(C)
  print(C['mur'])
  print(C)
  tournerAntiHoraire(C)
  print(C['mur'])
  print(C)
  tournerHoraire(C)
  print(C)
  tournerHoraire(C)
  print(C)
  tournerAntiHoraire(C)
  print(C)
  tourneAleatoire(C)
  print(C)
  print(coderMurs(C))
  decoderMurs(C,coderMurs(C))
  print(C1)
  print(C)
  print(passageNord(C,C1))
  print(passageSud(C,C1))
  print(passageEst(C,C1))
  print(passageOuest(C,C1))