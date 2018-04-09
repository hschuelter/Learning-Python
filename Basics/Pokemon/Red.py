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

def initializeBattle(you, red):

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
	
	#Pikachu
	pika.setLevel(50)

	pika.learnMove( Move('Quick Attack', '-', 40 , 100, 30, 0,  0, 1, 1) )
	pika.learnMove( Move('Thunderbolt ', '-', 90,  100, 15, 1, 12, 1, 0) )
	pika.learnMove( Move('Volt Tackle ', '-', 120, 100, 15, 0, 12, 1, 0) )
	pika.learnMove( Move('Iron Tail   ', '-', 100,  75, 15, 0,  8, 1, 0) )



	red.PokemonList.append( pika )
	pika.addOT(red)

	red.PokemonList.append( snor )
	snor.addOT(red)

	red.PokemonList.append( lapr )
	lapr.addOT(red)

	red.PokemonList.append( venu )
	venu.addOT(red)

	red.PokemonList.append( char )
	char.addOT(red)

	red.PokemonList.append( blas )
	blas.addOT(red)


def createPlayer(player):
	you = Player(player.name, player.gender)
	return you

def RedMenu(player):
	os.system('clear')
	you = createPlayer(player)
	red = Player()

	initializeBattle(you, red)


	Mechanics.listTeamPokemon(red)
	time.sleep(3)

def main():
	print('')

if __name__ == "__main__": main()