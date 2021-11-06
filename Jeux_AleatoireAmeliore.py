import random
import os
os.system("cls")
def afficher():
       print("********************************* BIENVENUE       MONSIEUR : ",nom,"********************************\n\n Je vous présente mon précieux jeux\n\nOn commence:Veuillez choisir un nombre entre 0 et 100 ")
nom=input("\nEntrez votre nom: ")
t=True
p=1
while t:
   l=random.randint(1,100)
   afficher()
   i=10
   m=10
   print("NOMBRE D'ASSISTANCE: ",p)  
   while i>0: 
         print("Tour restant:",m)
         n=int(input("Entrez un nombre :"))
         if n<=0 or n>100:
               print("\nVous n'êtes pas dans le jeu",nom)
         elif n<l:
               print("\nPlus grand !!!",nom)
               m=m-1
         elif n>l:
               print("\nPlus petit !!!",nom)
               m=m-1
         else :
               print("***************** Bravo ",nom," vous avez reussi avec ",10-i+1," coups")
               break
         i=i-1
   if n!=l:
          print("\n\n****************Vous avez perdu M. ",nom,"**************")
   print("\n\nVoulez vous recommencé !!!\nSi oui tapez 1 sinon tapez 0 :")
   choix=int(input("Faites votre choix :"))
   if choix==1:   
         t=True
         os.system("cls")
         p=p+1
   else :
      print("Merci d'avoir jouer !!! A bientôt ",nom)
      t=False
