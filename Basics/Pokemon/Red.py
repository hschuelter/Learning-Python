import random as ran
import os
import sys
import time
##
from Pokemon import Pokemon
from Player import Player
from Battle import Battle
from Move import Move
import Mechanics

def makeRedTeam(red):

	pika = Pokemon("PIKACHU"  , "Pikachu" , 12)
	snor = Pokemon("SNORLAX"  , "Snorlax" ,  0)
	lapr = Pokemon( "LAPRAS"  ,  "Lapras" , 10, 14)
	venu = Pokemon("VENUSAUR" , "Venusaur", 11, 3)
	char = Pokemon("CHARIZARD", "Charizard", 9, 2)
	blas = Pokemon("BLASTOISE", "Blastoise", 10)
	
	pika.setStats(110, 150,  60, 140,  70, 110) 	#Pikachu @Light Orb
	snor.setStats(235, 130,  85,  85, 130,  50) 	#Snorlax
	lapr.setStats(205, 105, 100, 105, 115,  80) 	#Lapras
	venu.setStats(155, 102, 103, 120, 120, 100) 	#Venusaur
	char.setStats(153, 104,  98, 129, 105, 120) 	#Charizard
	blas.setStats(154, 103, 120, 105, 125,  98) 	#Blastoise

	#NAME, DESC, POWER, ACCURACCY, TOTAL PP, CATEGORY, TYPING, MODIFIER, PRIORITY
	
	#Pikachu====
	pika.setLevel(50)

	pika.learnMove( Move('Quick Attack', '-', 40 , 100, 30, 0,  0, 1, 1) )
	pika.learnMove( Move('Thunderbolt ', '-', 90,  100, 15, 1, 12, 1, 0) )
	pika.learnMove( Move('Volt Tackle ', '-', 120, 100, 15, 0, 12, 1, 0) )
	pika.learnMove( Move('Iron Tail   ', '-', 100,  75, 15, 0,  8, 1, 0) )
	red.catchPokemon(pika)
	
	#Snorlax====
	snor.setLevel(50)

	snor.learnMove( Move('Shadow Ball', '-', 80 , 100, 15, 1,  7, 1, 0) )
	snor.learnMove( Move('Crunch     ', '-', 80 , 100, 15, 0, 16, 1, 0) )
	snor.learnMove( Move('Blizzard   ', '-', 110, 100,  5, 1, 14, 1, 0) )
	snor.learnMove( Move('Giga Impact', '-', 150,  90,  5, 0,  0, 1, 0) )
	red.catchPokemon( snor )

	#Charizard====
	char.setLevel(50)

	char.learnMove( Move('Blast Burn  ', '-', 150,  90,  5, 1,  9, 1, 0) )
	char.learnMove( Move('Flare Blitz ', '-', 120, 100, 15, 0,  9, 1, 0) )
	char.learnMove( Move('Air Slash   ', '-',  75,  95, 15, 1,  2, 1, 0) )
	char.learnMove( Move('Dragon Pulse', '-',  85, 100, 10, 1, 15, 1, 0) )
	red.catchPokemon( char )

	#Venusar====
	venu.setLevel(50)

	venu.learnMove( Move('Frenzy Plant', '-', 150,  90,  5, 1, 11, 1, 0) )
	venu.learnMove( Move('Giga Drain  ', '-',  75, 100, 10, 1, 11, 1, 0) )
	venu.learnMove( Move('Sludge Bomb ', '-',  90, 100, 10, 1,  3, 1, 0) )
	venu.learnMove( Move('Sleep Powder', '-',   0,  75, 15, 2, 11, 1, 0) )
	red.catchPokemon( venu )

	#Lapras====
	lapr.setLevel(50)

	lapr.learnMove( Move('Body Slam', '-', 85 , 100, 15, 0,  0, 1, 0) )
	lapr.learnMove( Move('Brine    ', '-', 65 , 100, 10, 1, 10, 1, 0) )
	lapr.learnMove( Move('Blizzard ', '-', 110, 100,  5, 1, 14, 1, 0) )
	lapr.learnMove( Move('Psychic  ', '-',  90, 100, 10, 1, 13, 1, 0) )
	red.catchPokemon( lapr )

	#Blastoise====
	blas.setLevel(50)

	blas.learnMove( Move('Hidro Cannon', '-', 150,  90,  5, 1, 10, 1, 0) )
	blas.learnMove( Move('Flash Cannon', '-',  80, 100, 10, 1,  8, 1, 0) )
	blas.learnMove( Move('Blizzard    ', '-', 110, 100,  5, 1, 14, 1, 0) )
	blas.learnMove( Move('Focus Blast' , '-', 120,  70,  5, 1,  1, 1, 0) )
	red.catchPokemon( blas )


def makeYourTeam(you):
	
	aeroda = Pokemon("AERODACTYL", "Aerodactyl", 5, 2)
	amphar = Pokemon("AMPHAROS"  , "Ampharos"  , 12)
	nineta = Pokemon("NINETALES" , "Ninetales" , 9)
	

	aeroda.setStats(155, 125,  85,  80,  95, 150) 	#Aerodactyl
	amphar.setStats(165,  95, 105, 135, 110,  75) 	#Ampharos
	nineta.setStats(148,  96,  95, 101, 120, 120) 	#Ninetales
	

	#Tauros====
	tauros = Pokemon("TAUROS", "Tauros", 0)
	tauros.setStats(150, 120, 115,  60,  90, 130) 
	tauros.setLevel(50)

	tauros.learnMove( Move('Return    ', '-', 102, 100, 20, 0,  0, 1, 0) )
	tauros.learnMove( Move('Earthquake', '-', 100, 100, 10, 0,  4, 1, 0) )
	tauros.learnMove( Move('Rock Slide', '-', 100,  80, 10, 0,  5, 1, 0) )
	tauros.learnMove( Move('Rock Smash', '-',  40, 100, 15, 0,  1, 1, 0) )

	
	you.catchPokemon(tauros)

	#Heracross====
	heracr = Pokemon("HERACROSS", "Heracross", 6, 1)
	heracr.setStats(155, 145,  95,  60, 115, 105)
	heracr.setLevel(50)

	heracr.learnMove( Move('Brick Break' , '-',  75, 100, 15, 0,  1, 1, 0) )
	heracr.learnMove( Move('Close Combat', '-', 120, 100,  5, 0,  1, 1, 0) )
	heracr.learnMove( Move('Megahorn    ', '-', 120,  85,  5, 0,  6, 1, 0) )
	heracr.learnMove( Move('Rock Slide  ', '-', 100,  80, 10, 0,  5, 1, 0) )

	you.catchPokemon(heracr)

	#Feraligatr====
	ferali = Pokemon("FERALIGATR", "Feraligatr", 10)
	ferali.setStats(160, 125, 120,  99, 103,  98)
	ferali.setLevel(50)

	ferali.learnMove( Move('Waterfall ', '-',  80, 100, 15, 0, 10, 1, 0) )
	ferali.learnMove( Move('Superpower', '-', 120, 100,  5, 0,  1, 1, 0) )
	ferali.learnMove( Move('Ice Fang  ', '-',  65,  95, 15, 0, 14, 1, 0) )
	ferali.learnMove( Move('Earthquake', '-', 100, 100, 10, 0,  4, 1, 0) )
	you.catchPokemon(ferali)



def createPlayer(player):
	you = Player(player.name, player.gender)
	return you

def RedMenu(player):
	you = createPlayer(player)
	red = Player()

	makeRedTeam(red)
	makeYourTeam(you)

	choice = 0

	while (choice == 0):
		os.system('clear')
		print('===')
		print('Menu:')
		print('    1) See your team.')
		print('    2) See Red\'s team.')
		print('    3) Battle!!')
		print('    4) Exit.')
		print('===')
		print('Option: '),
		choice = input()

		if (choice == 1):
			loop = 1
			while (loop > 0):
				loop = Mechanics.listTeamPokemon(you)
				if (loop == 1):
					print('===\nOK? '), 
					a = raw_input()		
			choice = 0

		elif (choice == 2):
			loop = 1
			while (loop > 0):
				loop = Mechanics.listTeamPokemon(red)
				if (loop == 1):
					print('===\nOK? '), 
					a = raw_input()		
			choice = 0

		elif (choice == 3):
			choice = 0

		elif (choice == 4):
			choice = -1

		else:
			choice = 0

	os.system('clear')

def main():
	print('')

if __name__ == "__main__": main()