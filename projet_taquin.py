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
from tkinter import *
import random 

############################
# dimensions canvas et grille
font_size = 16
width_size = 700
height_size = 700
lenght = width_size/4
widht = lenght/2
############################

boardShuffled =[i for i in range (1,16)]
random.shuffle(boardShuffled)
boardShuffled.append(0)

def puzzle_display():

    boardShuffled = [i for i in range(1,16)]
    random.shuffle(boardShuffled)
    boardShuffled.append(0)

    tileIndice = 0
    for i in range(4):
        for j in range(4):

            current_button = Button(cnv,
                width=4,
                height=3,
                text=boardShuffled[tileIndice],
                bg='royal blue')

            current_button.grid(row=i,column=j)
            current_button.bind('<Button-1>',move_tile)

            tileIndice += 1

    current_button.configure(bg="gray70")
    current_button.configure(text="")
    current_button.unbind('<Button-1>')

def shuffle(event):
    puzzle_display()

def move_tile(event):
    clickedButton = event.widget
    buttonGridInfo = clickedButton.grid_info()
    clickedButtonRow = buttonGridInfo["row"]
    clickedButtonColumn = buttonGridInfo["column"]

    if(clickedButtonColumn < 3):
        buttonOnRight = cnv.grid_slaves(row=clickedButtonRow, column=clickedButtonColumn+1)[0]
        if (buttonOnRight.cget['bg'] == 'gray70'):
            event.widget.grid(
                row=clickedButtonRow,
                column=clickedButtonColumn+1)
            buttonOnRight.grid(
                row=clickedButtonRow,
                column=clickedButtonColumn)

    if(clickedButtonColumn > 0):
        buttonOnRight = cnv.grid_slaves(row=clickedButtonRow,column=clikedButtonColumn-1)[0]
        if (buttonOnRight.cget('bg') == 'gray70'):
            event.widget.grid(
                row=clickedButtonRow,
                column=clickedButtonColumn-1)
            buttonOnRight.grid(
                row=clickedButtonRow,
                column=clickedButtonColumn)

    if(clickedButtonRow > 0):
        buttonOnRight = cnv.grid_slaves(row=clickedButtonRow-1, column=clickedButtonColumn)[0]
        if (buttonOnRight.cget('bg') == 'gray70'):
            event.widget.grid(
                row=clickedButtonRow-1,
                column=clickedButtonColumn)
            buttonOnRight.grid(
                row=clickedButtonRow,
                column=clickedButtonColumn)

    if(clickedButtonRow < 3):
        buttonOnRight = cnv.grid_slaves(row=clickedButtonRow+1,column=clickedButtonColumn)[0]
        if (buttonOnRight.cget('bg') == 'gray70'):
            event.widget.grid(
                row=clickedButtonRow+1,
                column=clickedButtonColumn)
            buttonOnRight.grid(
                row=clickedButtonRow,
                column=clickedButtonColumn)

Font=('Ubuntu', font_size, 'bold')
windows=Tk()
windows.title('Jeu du Taquin')
windows.resizable(0,0)
windows.bind('<KeyPress-s>', shuffle)
cnv=Canvas(windows,width=width_size, height=height_size, bg='gray70')
cnv.pack()

puzzle_display()
windows.mainloop()





