import random
import os
print("********************************* BIENVENUE       MONSIEUR ********************************\n\n Je vous présente mon précieux jeux\n\nOn commence: \nEntrez votre nom: ")
nom=input()

t=True
while t:
   n=10
   i=10
   l=random.randint(1,100)
   os.system("cls")
   while i>0:
      os.system("cls")
      print("Tour restant:",n)

      lentre=int(input("Entrez un nombre :"))

      if lentre<=0 or lentre>100:
         print("Vous n'êtes pas dans le jeu",nom)
      elif lentre<l:
         print("Plus grand !!!",nom)
         n=n-1
      elif lentre>l:
         print("Plus petit !!!",nom)
         n=n-1 
      else :
         print("Bravo vous avez reussi avec ",10-i+1," coups")
         break
      i=i-1
   print("Voulez vous recommencé !!!\nSi oui tapez 1 sinon tapez 0 :")
   choix=int(input("Faites votre choix :"))
   if choix==1 :
      t=True
   else :
      print("Merci d'avoir jouer !!! A bientôt ",nom)
      t=False