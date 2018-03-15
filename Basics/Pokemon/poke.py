import random as ran
import os
import db_pokemon as dpoke
from Pokemon import Pokemon
from Move import Move

def MoveInfo(Pokemon):
	os.system('clear')

	Pokemon.printMoves()
	print 'Select a move:', 
	opt = input()

	move =  Pokemon.getMove(opt)
	if move.getName != '-':
		move.moveInfo()
	else:
		print 'Errou!'


def initializeGame():
	moves = []
	pokemon = []

	moves.append( Move('Tackle', 'No additional effect.', 40, 100, 35, 0, 0, 1) )
	moves.append( Move('Scratch', 'No additional effect.', 40, 100, 35, 0, 0, 1) )
	moves.append( Move('Growl', 'Lowers opponent\'s Attack by one stage.', 0 , 100, 40, 2, 0, 0) )
	moves.append( Move('Tail Whip', 'Lowers opponent\'s Defense by one stage.', 0 , 100, 30, 2, 0, 0) )
	moves.append( Move('Ember', 'May induce burn.', 40, 100, 25, 1, 9, 1) )
	moves.append( Move('Water Gun', 'No additional effect.', 40, 100, 25, 1, 10, 1) )
	moves.append( Move('Vine Whip', 'No additional effect.', 45, 100, 25, 0, 11, 1) )

	pokemon.append( Pokemon("BULBASAUR", "Bulbasaur", 11) )
	pokemon[0].learnMove(moves[0]) # Tackle
	pokemon[0].learnMove(moves[2]) # Growl

	pokemon.append( Pokemon("SQUIRTLE", "Squirtle", 10) )
	pokemon[1].learnMove(moves[0]) # Tackle
	pokemon[1].learnMove(moves[3]) # Tail Whip

	pokemon.append( Pokemon("CHARMANDER", "Charmander", 9) )
	pokemon[2].learnMove(moves[1]) # Sratch
	pokemon[2].learnMove(moves[2]) # Growl


	return pokemon, moves
		
def listAllMoves(Moves):

	os.system('clear')

	print 'All moves:\n'

	for i in range(0, len(Moves) ):
		print '  ' + str(i+1) + ') ' + Moves[i].getName() + '\t[' + dpoke.typelist[Moves[i].getTyping()] +  ']  '


	print '\nSelect a move:'
	opt = input()

	if (opt > 0 and opt <= len(Moves) ):
		Moves[opt-1].moveInfo()
	else:
		return

def listAllPokemon(Pokemon):
	os.system('clear')

	print 'All currently available Pokemon:\n'

	for i in range(0,len(Pokemon)):
		Pokemon[i].printGenericStats()
		print '---\n'


def devMenu(Pokemon, Moves):
	option = 1
	os.system('clear')


	'''
	print '\t1) See the Pokemon\'s stats'
	print '\t2) See the Pokemon\'s moves'

	if option == 1:
		os.system('clear')
		Pokemon.printStats()
	elif option == 2:
		MoveInfo(p1)
	elif option == 3:
		listAllMoves(moves)

	'''
	while(option != 0):
		print '===\nDeveloper Menu:'

		print '\t1) List all available Pokemon'
		print '\t2) List all available moves'	
		print '\t0) To exit'

		print 'Choice:',
		option = input()

		if option == 1:
			listAllPokemon(Pokemon)
		elif option == 2:
			listAllMoves(Moves)
		else:
			option=0



def gameMenu(Pokemon, Moves):
	os.system('clear')

	print 'You can\'t play the game yet :/'
	print '(Insert a key to go back...)'

	sad = input()
	return

def main():
	pokemon, moves = initializeGame()
	p1 = Pokemon("Bulba", "Bulbasaur", 11)

	option = 1
	

	while(option != 0):
		os.system('clear')
		print "===\nMain Menu:"

		print '\t1) Go to dev menu'
		print '\t2) Play the game'		
		print '\t0) To exit'
		
		print 'Choice:',
		option = input()

		if option == 1:
			devMenu(pokemon, moves)
		elif option == 2:
			gameMenu(pokemon, moves)
		else:
			option = 0


	os.system('clear')
	print 'Go in the shadow'



if __name__ == "__main__": main()