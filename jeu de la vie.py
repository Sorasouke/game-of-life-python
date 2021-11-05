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
        for x in range (hauteur//10):
            for y in range (largeur//10):
                self.tableau[x][y]=0

    def gun(self):
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
        nb_voisin = 0
        if x == (hauteur//10)-1:
            if y ==0:
                if self.tableau[x-1][y] ==1:
                    nb_voisin+=1
                if self.tableau[x-1][y+1] ==1:
                    nb_voisin+=1
                if self.tableau[x][y+1] ==1:
                    nb_voisin+=1
                if self.tableau[0][y] ==1:
                    nb_voisin+=1
                if self.tableau[0][y+1] ==1:
                    nb_voisin+=1
                if self.tableau[0][y-1] ==1:
                    nb_voisin+=1
                if self.tableau[x-1][y-1] ==1:
                    nb_voisin+=1
                if self.tableau[x][y-1] ==1:
                    nb_voisin+=1
            elif y==(largeur//10)-1:
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
                if self.tableau[x-1][y] ==1:
                    nb_voisin+=1
                if self.tableau[x-1][y-1] ==1:
                    nb_voisin+=1
                if self.tableau[x][y-1] ==1:
                    nb_voisin+=1
                if self.tableau[x-1][y+1] ==1:
                    nb_voisin+=1
                if self.tableau[x][y+1] ==1:
                    nb_voisin+=1
                if self.tableau[0][y] ==1:
                    nb_voisin+=1
                if self.tableau[0][y+1] ==1:
                    nb_voisin+=1
                if self.tableau[0][y-1] ==1:
                    nb_voisin+=1
        else :
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
        tableau_futur= []
        for i in range (hauteur//10):
            ligne=[]
            for j in range (largeur//10):
                ligne.append(0)
            tableau_futur.append(ligne)
        for x in range (hauteur//10):
            for y in range (largeur//10):
                if self.tableau [x][y]==1:
                    if self.nb_voisins(x,y) < 2 or self.nb_voisins(x,y) >3:
                        tableau_futur[x][y] = 0
                    elif self.nb_voisins(x,y) == 3 or self.nb_voisins(x,y) == 2 :
                        tableau_futur[x][y] = 1
                else :
                    if self.nb_voisins(x,y) == 3:
                        tableau_futur[x][y] = 1
        self.tableau = tableau_futur
        return self.tableau








horloge=pygame.time.Clock()
tempo=11
largeur=1000
hauteur=680
grille = Grille(hauteur,largeur)
couleur_noire = (0,0,0)
resolution=(largeur,hauteur)
fenetre=pygame.display.set_mode(resolution)
pygame.display.set_caption('Le jeu de la vie')
carre_blanc =pygame.image.load("carre_blanc.gif").convert()






continuer=True
while continuer==True:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if tempo == 1:
                    pass
                else:
                    tempo=tempo-10
                    print("le tempo est de :",str(tempo))
            elif event.key == pygame.K_g:
                grille.clear()
                grille.gun()
            elif event.key == pygame.K_UP:
                tempo=tempo+10
                print("le tempo est de :",str(tempo))

    grille.update()
    fenetre.fill(couleur_noire)
    for i in range (hauteur//10):
        for j in range (largeur//10):
            if grille.tableau[i][j]==1:
                fenetre.blit(carre_blanc,(j*10,i*10))

    pygame.display.update()
    horloge.tick(tempo)
pygame.quit()
