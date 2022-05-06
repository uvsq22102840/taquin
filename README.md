# projet_taquin

#####################################################
# groupe BITD2_1
# Eva AVARRE
# Marwa FIDAH MOURO
# Erwann KERVOELEN
#https://github.com/uvsq22102840/taquin
######################################################

Dans ce projet, on veut programmer le jeu solitaire du taquin. Il s’agit d’un puzzle constitué de 15 carrés
numérotés de 1 à 15 qui peuvent coulisser horizontalement et verticalement à l’intérieur d’un cadre carré
qui contient un emplacement vide. Un carré ne peut coulisser que si l’emplacement voisin dans la direction choisie est vide. L’objectif est de déplacer les carrés de manière à ce que les cases soient rangées dans l'ordre croissant.
Le jeu démare à partir d'une configuration aléatoire.


Pour débuter le projet, nous avons crée l'interface graphique. Pour cela, nous avons crée un canvas de 700 de largeur et de longueur.Nous y avons ajouté des cases de 100 sur 100 numérotées de 1 à 15. Nous avons ensuite formaté un bouton retour qui permet à l'ordinateur de d'annuler un coup et de revenir à la configuration précédante, pour cela nous avons utiliser les fonctions étudier lors du premier semestre : 

def retour():
    (il faudra mettre la fonction retour que l'on aura programmer)
    
bouton_retour=tk.Button(racine,text="retour", command=retour,bg="grey")

Afin de coder notre Taquin, nous nous somes inspiré de l'algorithme A* trouvé dans le livre "L'intelligence artificielle en pratique avec Python" écrit par Hugues Bersini et Ken Hasselmann . Cet algorithme se base sur une formule simple: f=g+h , g représente le numéro de l'étape (zéro pour le première étape, 1 pour la deuxième etc); h représente l'entropy c'est-à-dire le nombre de cases qui ne sont pas à la bonne place. ![image](https://user-images.githubusercontent.com/91220165/167218581-af0ab6a9-c5b7-4d3b-86ae-576208bcbcab.png)
Comme on peut le voir sur cette image, cet algorithme nous permet de trouver la solution la plus rapide et la plus simple.
