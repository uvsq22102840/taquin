# projet_taquin

#####################################################
# groupe BITD2_1
# Eva AVARRE
# Marwa FIDAH MOURO
# Erwann KERVOELEN
#https://github.com/uvsq22102840/taquin
######################################################
#Etat projet
#1 créer grille pour tout les nums
#2 créer système case vide ou non (= 0)
#3 créer clic de souris = déplacement chiffre si case vide à côté
#4 créer verif de fin, soit arrangement  chiffre correct (dans la fonction qui tourne perma)
#####################################################
from tkinter import Tk
from random import randint
import tkinter as tk


############################
# constantes

# taille des cases de la grille
N = 100
# dimensions canvas et grille
LARGEUR = 700
HAUTEUR = 700
LARGEUR_CASE = LARGEUR // N
HAUTEUR_CASE = HAUTEUR // N
############################
#Création canvas

root = tk.Tk( )
canvas = tk.Canvas(root, width=LARGEUR, height=HAUTEUR)


def taquin():
    return [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]


for r in range(4):
    for c in range(4):
        num = taquin()
        tk.Label(root, text=num[r][c],
         borderwidth=50 ).grid(row=r,column=c)




root.mainloop()

