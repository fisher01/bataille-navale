import os
from class_player import Player

#Clear screen before the game
os.system('cls' if os.name == 'nt' else 'clear')

pseudo = str(input("Entrez le pseudo du premier joueur : "))
player1 = Player(pseudo)
pseudo = str(input("Entrez le pseudo du second joueur : "))
player2 = Player(pseudo)
