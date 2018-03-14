import random as ran
import os

typelist = 	['NORMAL', 'FIGHTING', 'FLYING', 'POISON',  	# [0  ~  3]
			 'GROUND', 'ROCK', 'BUG', 'GHOST', 'STEEL', 	# [4  ~  8]
			 'FIRE', 'WATER', 'GRASS', 'ELECTRIC',			# [9  ~ 12]
			 'PSYCHIC', 'ICE', 'DRAGON', 'DARK', 'FAIRY',	# [13 ~ 17]
			 'NULL']										# [   18  ]

nature= ['Quirky', 'Lonely', 'Brave', 'Adamant', 'Naughty',	# [0  ~  4]
		 'Bold', 'Docile', 'Relaxed', 'Impish', 'Lax',		# [5  ~  9]
		 'Timid', 'Hasty', 'Serious', 'Jolly', 'Naive', 	# [10 ~ 14]
		 'Modest', 'Mild', 'Quiet', 'Bashful', 'Rash', 		# [15 ~ 19]
		 'Calm', 'Gentle', 'Sassy', 'Careful', 'Quirky',	# [20 ~ 24]
		 'NATURELESS']										# [   25  ]

category= ['PHYSICAL', 'SPECIAL', 'OTHER']


class Move:

	def __init__(self, name = '-', effect = '-', base_power = 0, accuracy = 0, total_PP = 0, category = '-', typing = 18, modifier = '-'):
		self.name = name
		self.effect = effect
		self.base_power = base_power
		self.accuracy = accuracy

		self.total_PP = total_PP
		self.current_PP = total_PP

		self.category = category
		self.typing = typing

		self.modifier = modifier

	def getName(self):
		return self.name

	def getEffect(self):
		return self.effect

	def getBasePower(self):
		return self.base_power

	def getAccuracy(self):
		return self.accuracy

	def getTotal_PP(self):
		return self.total_PP

	def getCategory(self):
		return self.category

	def getTyping(self):
		return self.typing

	def moveInfo(self):

		os.system('clear')
		
		if(self.name == '-'):
			print 'Invalid choice'
			return -1

		
		print self.name
		print '+---------------+---------------+'
		print '|  TYPE:\t|     ' + typelist[self.typing] + '\t|'
		print '|  CATEGORY:\t|    ' + category[self.category] + '\t|'
		print '|  POWER:\t|\t' + str(self.base_power) + '\t|'
		print '|  ACCURACY:\t|      ' + str(self.accuracy) + '\t|' 
		print '|  PP:\t\t|     ' + str(self.current_PP) + '/' + str(self.total_PP) + '\t|' 
		print '+---------------+---------------+'
		print 'Description: '
		print self.effect
		print ''


class Pokemon:

	def __init__(self, nickname, species, typing1, typing2 = 18):
		self.nickname = nickname
		self.species = species
		self.level = 5

		self.typing = []
		self.typing.append(typing1)
		self.typing.append(typing2)

		self.nature = ran.randint(0,24)

		self.shiny = (ran.randint(1,8192) / 8192)

		self.moves = []

		'''
		self.moves.append( Move('Tackle', 'No effect', 40, 100, 35, 0, 0, 1) )
		self.moves.append( Move('Growl', 'Lowers opponent\'s Attack by one stage.', 0 , 100, 40, 1, 0, 0) )
		self.moves.append( Move() )
		self.moves.append( Move() )
		'''

	def printStats(self):
		if self.shiny == 0:
			print self.nickname  + ' (' + self.species + ')'
		else:
			print self.nickname  + ' (' + self.species + ') *'

		print 'Level:  ' + str(self.level)

		print 'Type:   ',
		for i in range (0, len(self.typing) ):
			print typelist[ self.typing[i] ] + '  ',

		print ''
		print 'Nature: ' + nature[self.nature]

		self.printMoves()

	def printGenericStats(self):

		print self.nickname  + ' (' + self.species + ')'
		print 'Level:  ' + str(self.level)

		print 'Type: ',
		for i in range (0, len(self.typing) ):
			if self.typing[i] != 18:
				print '| ' + typelist[ self.typing[i] ],

		print '|'
		self.printMoves()


	def printMoves(self):
		print 'Moves:'

		for move in range(0, len(self.moves) ):
			if self.moves[move].name != '-':
				print '  ' + str(move+1) + ') ' + self.moves[move].name + '\t' + str(self.moves[move].current_PP) + '/' + str(self.moves[move].total_PP) + '\t[' + typelist[self.moves[move].typing] +  ']  '
			else:
				print '  ' + str(move+1) + ') ' + '  -'

	def learnMove(self, move):
		if len(self.moves) < 4:
			self.moves.append(move)

		else:
			print 'Your Pokemon can\'t learn more than four moves...'
			print 'Choose one to forget:'

			self.printMoves()

			option = input()

			self.moves[option-1] = move


	def changeNickname(self, new_nickname):
		self.nickname = new_nickname

	def getMove(self, position):
		if position > 0 and position <= len(self.moves):
			return self.moves[position-1]
		else:
			print 'Invalid move!'
			return Move()

	def catchPokemon(self):
		poke = copy.deepcopy(self)
		return poke

def Status(Pokemon):
	os.system('clear')
	Pokemon.printStats()

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
		print '  ' + str(i+1) + ') ' + Moves[i].getName() + '\t[' + typelist[Moves[i].getTyping()] +  ']  '


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
			Status(p1)
		elif option == 2:
			MoveInfo(p1)
		elif option == 3:
			listAllMoves(moves)

	'''
	while(option != 0):
		print '===\nDeveloper Menu:'

		print '\t1) List all available Pokemon'
		print '\t2) List all available moves'	
		print '\t?) To exit'

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
		print '\t?) To exit'
		
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