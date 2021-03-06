#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Gameboard():
	""" Plateau du jeu
			Gestion du plateau de jeu (Affichage et traitements du contenu des cases)
			Contient le plateau de tir et le plateau des bateaux du joueur
	"""

	
	def __init__(self, pPlayerShip_init, pPlayerFiring_init):
		self.tableMatchesLinePosY = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		self.pPlayerShip = pPlayerShip_init
		self.pPlayerFiring = pPlayerFiring_init

	def DrawFiringBoard(self):
		print("			   1   2   3   4   5   6   7   8   9   10")
		print("			 ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐")
		for line in range(0, 9):
			lineToFill = "			" + str(self.tableMatchesLinePosY[line]) + "│"
			lineSeparator = "			 ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤"
			for col in range(0, 10):
				lineToFill += self.pPlayerFiring[col][line]
				lineToFill += "│"
			print(lineToFill)
			print(lineSeparator)
		lineToFill = "			J│"
		for col in range(0, 10):
			lineToFill += self.pPlayerFiring[col][9]
			lineToFill += "│"
		print(lineToFill)
		print("			 └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘\n")
		
	def DrawPlayerBoard(self):
		print("			   1   2   3   4   5   6   7   8   9   10")
		print("			 ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗")
		for line in range(0, 9):
			lineToFill = "			" + str(self.tableMatchesLinePosY[line]) + "║"
			lineSeparator = "			 ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣"
			for col in range(0, 10):
				lineToFill += self.pPlayerShip[col][line]
				lineToFill += "║"
			print(lineToFill)
			print(lineSeparator)

		lineToFill = "			J║"
		for col in range(0, 10):
			lineToFill += self.pPlayerShip[col][9]
			lineToFill += "║"
		print(lineToFill)
		print("			 ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝\n")

		