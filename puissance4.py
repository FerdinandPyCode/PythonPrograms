import random
import os
from time import sleep

os.system("cls")
class puissance4:

  def __init__(self):
    self.tab=[[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]

  def afficher(self):

    print("""
                0                 1                    2                     3                  4                    5                  6
    +-------------------------------------------------------------------------------------------------------------------------------------------
    |                |                   |                     |                   |                  |                    |                   |
    |        {}       |        {}          |         {}           |         {}         |        {}         |        {}           |        {}          |
    |                |                   |                     |                   |                  |                    |                   |
    |________________|___________________|_____________________|___________________|__________________|____________________|___________________|
    |                |                   |                     |                   |                  |                    |                   |
    |        {}       |        {}          |         {}           |         {}         |        {}         |        {}           |        {}          |
    |                |                   |                     |                   |                  |                    |                   |
    |________________|___________________|_____________________|___________________|__________________|____________________|___________________|
    |                |                   |                     |                   |                  |                    |                   |
    |        {}       |        {}          |         {}           |         {}         |        {}         |        {}           |        {}          |
    |                |                   |                     |                   |                  |                    |                   |
    |________________|___________________|_____________________|___________________|__________________|____________________|___________________|
    |                |                   |                     |                   |                  |                    |                   |
    |        {}       |        {}          |         {}           |         {}         |        {}         |        {}           |        {}          |
    |                |                   |                     |                   |                  |                    |                   |
    |________________|___________________|_____________________|___________________|__________________|____________________|___________________|
    |                |                   |                     |                   |                  |                    |                   |
    |        {}       |        {}          |         {}           |         {}         |        {}         |        {}           |        {}          |
    |                |                   |                     |                   |                  |                    |                   |
    |________________|___________________|_____________________|___________________|__________________|____________________|___________________|
    |                |                   |                     |                   |                  |                    |                   |
    |        {}       |        {}          |         {}           |         {}         |        {}         |        {}           |        {}          |
    |                |                   |                     |                   |                  |                    |                   |
    |________________|___________________|_____________________|___________________|__________________|____________________|___________________|

    """.format(self.tab[0][0],self.tab[0][1],self.tab[0][2],self.tab[0][3],self.tab[0][4],self.tab[0][5],self.tab[0][6],self.tab[1][0],self.tab[1][1],self.tab[1][2],self.tab[1][3],self.tab[1][4],self.tab[1][5],self.tab[1][6],self.tab[2][0],self.tab[2][1],self.tab[2][2],self.tab[2][3],self.tab[2][4],self.tab[2][5],self.tab[2][6],self.tab[3][0],self.tab[3][1],self.tab[3][2],self.tab[3][3],self.tab[3][4],self.tab[3][5],self.tab[3][6],self.tab[4][0],self.tab[4][1],self.tab[4][2],self.tab[4][3],self.tab[4][4],self.tab[4][5],self.tab[4][6],self.tab[5][0],self.tab[5][1],self.tab[5][2],self.tab[5][3],self.tab[5][4],self.tab[5][5],self.tab[5][6]))


  def remplir(self,y,numj):
    if y<0 or y>6:
      print("Entrez une colonne valide !!!")
      return False
    elif self.tab[0][y]!=" ":
      print("Case totalement occupée!!! \n Veuillez reesayer :")
      return False
    elif(numj==1):
      x=5
      while self.tab[x][y]!=" " and x>=0:
        x-=1
      self.tab[x][y]='O'
      return True
    else:
      x=5
      while self.tab[x][y]!=" " and x>=0:
        x-=1
      self.tab[x][y]='X'
      return True

  def ordinateur(self,n):
    #if n==1 or n==2:
    y=random.randint(0,6)
    #y=5
    self.remplir(y,2)
    #elif n==3:
  

  def Verifier_gagner(self):
    result=False
    k=0
    for i in range(6):
      for j in range(7):
        if self.tab[i][j]==" ":
          k+=1
        else:
          if i in range(3): 
            if self.tab[i][j]==self.tab[i+1][j]==self.tab[i+2][j]==self.tab[i+3][j]:
              self.tab[i][j]=self.tab[i+1][j]=self.tab[i+2][j]=self.tab[i+3][j]='A'
              result=True
          
          if j in range(4) and result==False:
            if self.tab[i][j]==self.tab[i][j+1]==self.tab[i][j+2]==self.tab[i][j+3]:
              self.tab[i][j]=self.tab[i][j+1]=self.tab[i][j+2]=self.tab[i][j+3]='A'
              result=True

          if i in range(3) and j in range(4) and result==False:
            if self.tab[i][j]==self.tab[i+1][j+1]==self.tab[i+2][j+2]==self.tab[i+3][j+3]:
              self.tab[i][j]=self.tab[i+1][j+1]=self.tab[i+2][j+2]=self.tab[i+3][j+3]='A'
              result=True
          
          if i in range(3) and j in range(3,7) and result==False:
            if self.tab[i][j]==self.tab[i+1][j-1]==self.tab[i+2][j-2]==self.tab[i+3][j-3]:
              self.tab[i][j]=self.tab[i+1][j-1]=self.tab[i+2][j-2]=self.tab[i+3][j-3]='A'
              result=True

    return result
           

j1=puissance4()
print("********************************** BIENVENUE AU JEU PUISSANCE 4 **************************************")
sleep(1)
nom=input("Entrez votre nom :")
t=True
score=0

while t==True:
  verifie=False
  n=1
  sleep(1)
  j1.tab=[[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]
  os.system("cls")
  print("Veuillez patienter pendant le chargement du jeu ...................")
  sleep(3)
  while verifie ==False and n<=21:
    os.system("cls")
    j1.afficher()
    print(nom,'\nVotre Score: ',score)
    remp=False

    while remp !=True:
      try:
        y=int(input("Entrez la colonne de jeu: "))
        remp=True
      except:
        remp=False

      remp=j1.remplir(y,1)

    gagne=False
    if n>=4:
      gagne=j1.Verifier_gagner()

    if gagne==True:
      j1.afficher()
      print("Bravo vous avez reussi !!!!!!!!!!!! <(^-^)> ")
      score+=1
      break

    verifie=gagne
    j1.ordinateur(n)

    if n>=4:
      gagne=j1.Verifier_gagner()

    if gagne==True:
      j1.afficher()
      print("Humm!!!! vous avez Perdu :) ")
      score-=1
      break

    j1.afficher()

    n+=1

    choix=5
  while choix==5:
    try:
      choix=int(input("Voulez vous recommencer le jeu !!!\n Si OUI tapez 1 SINON tapez 0 : "))
    except:
      print("Veuillez entrer une valeur convenable 0 ou 1 !!!")
      choix=5

  if choix==1:
    t=True
  else:
    os.system("cls")
    t=False
    print(" Merci")
    sleep(1)
    print(nom)
    sleep(1)
    print("d'avoir visité mon jeu \n\n")
    sleep(1)
    print("Votre score total est de ",score)
    
    if score>=10:
      print("Mention: Excellent")
    elif 5<score<10:
      print("Mention: Moyenne")
    elif 3<score<6:
      print("Mention: Pas mal")
    else:
      print("Veuillez revoir votre niveau de jeux")