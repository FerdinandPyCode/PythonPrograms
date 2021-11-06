import os
os.system("cls")
class morpion:

    def __init__(self):
        self.tab=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
         
    def afficher(self):
        print("""
               0                 1                2
         _________________________________________________
        |               |               |                 |
       0|               |               |                 |
        |               |               |                 |     
        |       {}       |        {}      |        {}        |
        |               |               |                 |
        |_______________|_______________|_________________|
        |               |               |                 |
       1|               |               |                 |
        |               |               |                 |     
        |        {}      |        {}      |        {}        |
        |               |               |                 |
        |_______________|_______________|_________________|
        |               |               |                 |
       2|               |               |                 |
        |               |               |                 |     
        |        {}      |       {}       |        {}        |
        |               |               |                 |
        |_______________|_______________|_________________|
        """.format(self.tab[0][0],self.tab[0][1],self.tab[0][2],self.tab[1][0],self.tab[1][1],self.tab[1][2],self.tab[2][0],self.tab[2][1],self.tab[2][2]))
    
    
    def controler(self,x,y,numjou):
        if (x<0 or x>=3 or y<0 or y>=3):
            print("Case indisponible , Veuillez recommencer !!!")
            return False
        elif self.tab[x][y] !=" ":
            print("Case occupée ,Veuillez recommencer !!!!")
            return False
        else :
            if numjou==1:
                self.tab[x][y] ='X'
            else:
                self.tab[x][y] ='O'
            return True
    
    def verifier(self):
        if ((self.tab[0][0]==self.tab[0][1]==self.tab[0][2]=='X') or
             (self.tab[1][0]==self.tab[1][1]==self.tab[1][2]=='X')or
             (self.tab[2][0]==self.tab[2][1]==self.tab[2][2]=='X')or
             (self.tab[0][0]==self.tab[1][0]==self.tab[2][0]=='X')or
             (self.tab[0][1]==self.tab[1][1]==self.tab[2][1]=='X')or
             (self.tab[0][2]==self.tab[1][2]==self.tab[2][2]=='X')or
             (self.tab[0][0]==self.tab[1][1]==self.tab[2][2]=='X')or
             (self.tab[0][2]==self.tab[1][1]==self.tab[2][0]=='X')):
             return True
        elif ((self.tab[0][0]==self.tab[0][1]==self.tab[0][2]=='O') or
             (self.tab[1][0]==self.tab[1][1]==self.tab[1][2]=='O')or
             (self.tab[2][0]==self.tab[2][1]==self.tab[2][2]=='O')or
             (self.tab[0][0]==self.tab[1][0]==self.tab[2][0]=='O')or
             (self.tab[0][1]==self.tab[1][1]==self.tab[2][1]=='O')or
             (self.tab[0][2]==self.tab[1][2]==self.tab[2][2]=='O')or
             (self.tab[0][0]==self.tab[1][1]==self.tab[2][2]=='O')or
             (self.tab[0][2]==self.tab[1][1]==self.tab[2][0]=='O')):
             return True
        else:
            return False


j1=morpion()
print("******************************************************************__BIENVENUE DANS LE JEU MORPION__ *******************************************************************************\n\n")
print("Veuillez choisir une valeur dans le menu\n\n1-Jouer à deux \n2-Jouer contre l'ordinateur\n3-Aide\n4-Quitter")
t=False
while t==False:
    choix=input("Faites votre choix :")
    try :
        choix=int(choix)
        if choix>0 or choix<5:
            t=True
    except ValueError:
        print("La valeur entrée est incorrecte")
    except:
        print("Veuillez entrer une valeur correcte")

if choix==1:
    joueur_1=input("\nNom du Joueur n°1 :")
    joueur_2=input("\nNom du Joueur n°2 :")
    retry=1
    while retry==1:
        j1.tab=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        os.system("cls")
        n_tour=1
        Gagne=False
        while (n_tour<=4 and Gagne==False):


            os.system("cls")
            print("Tour: {}\n".format(n_tour))
            j1.afficher()
            print(joueur_1)
            controle=False
            while controle !=True:
                x=int(input("\nPosition horizontale de la case: ")) #Controle à faire sur les entrées de l'auteur 
                y=int(input("\nPosition verticale de la case: "))   #Controle à faire sur les entrées de l'auteur
                controle=j1.controler(x,y,1)
            os.system("cls")
            print("Tour: {}\n".format(n_tour))
            j1.afficher()
            Gagne=j1.verifier()

            if n_tour>=3 and Gagne:
                print("Le joueur ",joueur_1," à gagner !!!!!!!!!!!!!!!!")
                break

            os.system("cls")
            print("Tour: {}\n".format(n_tour))
            j1.afficher()
            print(joueur_2)
            controle=False
            while controle !=True:
                x=int(input("\nPosition horizontale de la case: ")) #Controle à faire sur les entrées de l'auteur 
                y=int(input("\nPosition verticale de la case: "))   #Controle à faire sur les entrées de l'auteur
                controle=j1.controler(x,y,2)
            os.system("cls")
            print("Tour: {}\n".format(n_tour))
            j1.afficher()
            Gagne=j1.verifier()

            if n_tour>=3 and Gagne:
                print("Le joueur ",joueur_2," à gagner !!!!!!!!!!!!!!!!")
                break
            
            if n_tour==4 and Gagne==False:
                print("***********************************GAME_____OVER******************************")
            n_tour+=1
        retry=int(input("Voulez-vous recommencer ? Si oui tapez Un 1 sinon tapez Zero 0 :"))

if choix==2:
    joueur=input("\nNom du Joueur :")
    retry=1
    while retry==1:
        j1.tab=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        os.system("cls")
        n_tour=1
        Gagne=False
        while (n_tour<=4 and Gagne==False):
            os.system("cls")
            print("Tour: {}\n".format(n_tour))
            j1.afficher()
            print(joueur)
            controle=False
            while controle !=True:
                x=int(input("\nPosition horizontale de la case: ")) #Controle à faire sur les entrées de l'auteur 
                y=int(input("\nPosition verticale de la case: "))   #Controle à faire sur les entrées de l'auteur
                controle=j1.controler(x,y,1)
            os.system("cls")
            print("Tour: {}\n".format(n_tour))
            j1.afficher()
            Gagne=j1.verifier()

            if n_tour>=3 and Gagne:
                print("Le joueur ",joueur," à gagner !!!!!!!!!!!!!!!!")
                break

            #print("Tour: {}\n".format(n_tour))
            import random
            f=False
            while f==False:
                i=random.randint(0,2)
                j=random.randint(0,2)
                if j1.tab[i][j] !=" ":
                    f=False
                else:
                    f=True
            j1.tab[i][j]='O'

            Gagne=j1.verifier()

            if n_tour>=3 and Gagne:
                print("***********************************GAME_____OVER******************************")
                break
            
            if n_tour==4 and Gagne==False:
                os.system("clear")
                j1.afficher()
                print("***********************************GAME_____OVER******************************")
            n_tour+=1
        retry=int(input("Voulez-vous recommencer ? Si oui tapez Un 1 sinon tapez Zero 0 :"))