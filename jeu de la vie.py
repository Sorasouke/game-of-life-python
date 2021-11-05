import pygame
from pygame.locals import *
from random import randint
pygame.init()

class Grille :
    def __init__(self,hauteur,largeur):
        self.tableau = []
        for i in range (hauteur//10):
            ligne=[]
            for j in range (largeur//10):
                ligne.append(randint(0,1))
            self.tableau.append(ligne)

    def clear(self):
        '''
        on remplace toute les valeurs de la grille par des 0
        '''
        for x in range (hauteur//10):# on parcourt la grille est on remplace tout par 0
            for y in range (largeur//10):
                self.tableau[x][y]=0

    def gun(self):
        '''
        cette méthode sert à faire apparaître une figure qui envoie des planeurs
        à l'infini.
        '''
        for i in range(hauteur//10):
            for j in range(largeur//10):
                self.tableau[i][j] = 0
        figure=['........................#...........',
                '......................#.#...........',
                '............##......##............##',
                '...........#...#....##............##',
                '##........#.....#...##..............',
                '##........#...#.##....#.#...........',
                '..........#.....#.......#...........',
                '...........#...#....................',
                '............##......................']
        depart=largeur//64
        for i in range(len(figure)):
            for j in range(len(figure[i])):
                if figure[i][j]=='#':
                    self.tableau[depart+i][depart+j]=1

    def nb_voisins(self,x,y):
        '''
        on compte le nombre de voisins des cellules
        paramètre d'entrée :
            x -> est un entier compris entre 0 et la hauteur//10
            y -> est un entier compris entre 0 et la largeur//10
        '''
        nb_voisin = 0# création d'une variable qui servira à compter le nombre de voisin
        if x == (hauteur//10)-1:# on vérifie si x est égale à la dernière valeur du tableau
            if y==(largeur//10)-1:
                if self.tableau[x-1][y] ==1:
                    nb_voisin+=1
                if self.tableau[x-1][0] ==1:
                    nb_voisin+=1
                if self.tableau[x][0] ==1:
                    nb_voisin+=1
                if self.tableau[0][y] ==1:
                    nb_voisin+=1
                if self.tableau[0][0] ==1:
                    nb_voisin+=1
                if self.tableau[0][y-1] ==1:
                    nb_voisin+=1
                if self.tableau[x-1][y-1] ==1:
                    nb_voisin+=1
                if self.tableau[x][y-1] ==1:
                    nb_voisin+=1
            else :
                if self.tableau[x-1][y] ==1:# si le voisin du dessus est vivant on ajoute 1 à nb_voisin
                    nb_voisin+=1
                if self.tableau[x-1][y+1] ==1:# si le voisin à la diagonale haut droite est vivant on ajoute 1 à nb_voisin
                    nb_voisin+=1
                if self.tableau[x][y+1] ==1:# si le voisin à droite est vivant on ajoute 1 à nb_voisin
                    nb_voisin+=1
                if self.tableau[0][y] ==1:# si le voisin en bas est vivant on ajoute 1 à nb_voisin
                    nb_voisin+=1
                if self.tableau[0][y+1] ==1:# si le voisin à la diagonale bas droite est vivant on ajoute 1 à nb_voisin
                    nb_voisin+=1
                if self.tableau[0][y-1] ==1:# si le voisin à la diagonale bas gauche est vivant on ajoute 1 à nb_voisin
                    nb_voisin+=1
                if self.tableau[x-1][y-1] ==1:# si le voisin à la diagonale haut gauche est vivant on ajoute 1 à nb_voisin
                    nb_voisin+=1
                if self.tableau[x][y-1] ==1:# si le voisin à gauche est vivant on ajoute 1 à nb_voisin
                    nb_voisin+=1
        else :#sinon on refait la même chose mais différamment
            if y==(largeur//10)-1:
                if self.tableau[x+1][y-1] ==1:
                    nb_voisin+=1
                if self.tableau[x][y-1] ==1:
                    nb_voisin+=1
                if self.tableau[x-1][y-1] ==1:
                    nb_voisin+=1
                if self.tableau[x+1][y]==1:
                    nb_voisin+=1
                if self.tableau[x-1][y] ==1:
                    nb_voisin+=1
                if self.tableau[x+1][0]==1:
                    nb_voisin+=1
                if self.tableau[x-1][0] ==1:
                    nb_voisin+=1
            else :
                if self.tableau[x+1][y]==1:
                    nb_voisin+=1
                if self.tableau[x-1][y] ==1:
                    nb_voisin+=1
                if self.tableau[x+1][y+1] ==1:
                    nb_voisin+=1
                if self.tableau[x][y+1] ==1:
                    nb_voisin+=1
                if self.tableau[x-1][y+1] ==1:
                    nb_voisin+=1
                if self.tableau[x+1][y-1] ==1:
                    nb_voisin+=1
                if self.tableau[x][y-1] ==1:
                    nb_voisin+=1
                if self.tableau[x-1][y-1] ==1:
                    nb_voisin+=1
        return nb_voisin

    def update(self):
        '''
        on vérifie les voisins de tout le tableau qu'on stocke dans un tableau intermédiaire
        puis on écrase l'ancien tableau avec le tableau intermédiaire
        paramètre de sortie :
            self.tableau -> list de list
        '''
        tableau_futur= []#on crée une liste vide
        for i in range (hauteur//10):#on remplit des listes de 0 et on les ajoute à la liste vide
            ligne=[]
            for j in range (largeur//10):# qui est de la même taille que la grille qu'on utilise
                ligne.append(0)
            tableau_futur.append(ligne)
        for x in range (hauteur//10):#on parcoure tout les éléments de la grille
            for y in range (largeur//10):
                if self.tableau [x][y]==1:#si l'élement de la grille est 1
                    if self.nb_voisins(x,y) < 2 or self.nb_voisins(x,y) >3:# on vérifie si il a moins de 2 voisins ou plus de 2 voisins
                        #si oui l'élement devient 0
                        tableau_futur[x][y] = 0
                    else :#sinon il reste 1
                        tableau_futur[x][y] = 1
                else :#sinon
                    if self.nb_voisins(x,y) == 3:#si il a 3 voisins l'élement devient 1
                        tableau_futur[x][y] = 1
        self.tableau = tableau_futur#on remplace l'ancienne grille par la grille intermédiaire
        return self.tableau# et on la renvoie








horloge=pygame.time.Clock()
tempo=1 #vitesse de l'animation de pygame
largeur=1000#largeur en pixel de la fenêtre
hauteur=680#hauteur en pixel de la fenêtre
grille = Grille(hauteur,largeur)#création de la grille
couleur_noire = (0,0,0)
resolution=(largeur,hauteur)
fenetre=pygame.display.set_mode(resolution)
pygame.display.set_caption('Le jeu de la vie')# titre de la fenêtre pygame
carre_blanc =pygame.image.load("carre_blanc.gif").convert()






continuer=True
while continuer==True:#tant que continuer est égale à True
    for event in pygame.event.get():
        if event.type == QUIT:#si on clique sur la croix de la fenêtre on quitte la boucle
            continuer = False
        elif event.type == pygame.KEYDOWN:#si on appuie sur une touches du clavier
            if event.key == pygame.K_DOWN:#si on appuie sur la flèche du bas
                if tempo <= 1:#si le tempo est à 1 ou plus bas on empêche que le tempo passe en dessous de 1
                    tempo = 1
                else:#sinon on enlève 10 au tempo
                    tempo=tempo-10
                    if tempo == 0:#si après ça le tempo est égale à 0 il passe à 1
                        tempo =1
                    print("le tempo est de :",str(tempo))
            elif event.key == pygame.K_g:#si on appuie sur la touche g on fait apparaître un gun
                grille.clear()
                grille.gun()
            elif event.key == pygame.K_UP:#si on appuie sur la flèche du haut
                if tempo == 1:# si le tempo est égale à 1 on ajoute 9 (parce que c'est pas beau de faire +10)
                    tempo=tempo+9
                    print("le tempo est de :",str(tempo))
                else :#sinon on ajoute 10
                    tempo=tempo+10
                    print("le tempo est de :",str(tempo))
    grille.update()# on actualise la grille
    fenetre.fill(couleur_noire)
    for i in range (hauteur//10):#on parcourt la grille
        for j in range (largeur//10):
            if grille.tableau[i][j]==1:#si l'élement de la grille est 1 on affiche un carré blanc
                fenetre.blit(carre_blanc,(j*10,i*10))

    pygame.display.update()
    horloge.tick(tempo)
pygame.quit()
