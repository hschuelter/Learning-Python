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
		 'Calm', 'Gentle', 'Sassy', 'Careful', 'Quirky']	# [20 ~ 24]

category= ['PHYSICAL', 'SPECIAL']


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

	def moveInfo(self):

		os.system('clear')
		
		if(self.name == '-'):
			print 'Invalid choice'
			return -1

		
		print self.name
		print '+---------------+---------------+'
		print '|  TYPE:\t|    ' + typelist[self.typing] + '\t|'
		print '|  CATEGORY:\t|    ' + category[self.category] + '\t|'
		print '|  POWER:\t|\t' + str(self.base_power) + '\t|'
		print '|  ACCURACY:\t|      ' + str(self.accuracy) + '\t|' 
		print '|  PP:\t\t|     ' + str(self.current_PP) + '/' + str(self.total_PP) + '\t|' 
		print '+---------------+---------------+'
		print 'Description: '
		print self.effect
		print ''


class Pokemon:

	def __init__(self, nickname, species, typing):
		self.nickname = nickname
		self.species = species
		self.level = 5
		self.typing = typing
		self.nature = ran.randint(0,24)

		self.moves = []

		self.moves.append( Move('Tackle', 'No effect', 40, 100, 35, 0, 0, 1) )
		self.moves.append( Move('Growl', 'Lowers opponent\'s Attack by one stage.', 0 , 100, 40, 1, 0, 0) )
		self.moves.append( Move() )
		self.moves.append( Move() )

	def printStats(self):
		print self.nickname  + ' (' + self.species + ')'
		print 'Level:  ' + str(self.level)
		print 'Type:   ' + typelist[self.typing]
		print 'Nature: ' + nature[self.nature]

		self.printMoves()

	def printMoves(self):
		print 'Moves:'

		for move in range(0, len(self.moves) ):
			if self.moves[move].name != '-':
				print '  ' + str(move+1) + ') ' + self.moves[move].name + '\t' + str(self.moves[move].current_PP) + '/' + str(self.moves[move].total_PP) + '\t[' + typelist[self.moves[move].typing] +  ']  '
			else:
				print '  ' + str(move+1) + ') ' + '  -'

	def getMove(self, position):
		if position > 0 or position < 4 or self.moves[position-1].name != '-':
			return self.moves[position-1]
		else:
			print 'Invalid move!'
			return Move()

def Status(Pokemon):
	os.system('clear')
	Pokemon.printStats()

def MoveInfo(Pokemon):
	os.system('clear')

	Pokemon.printMoves()
	print 'Select a move:', 
	opt = input()

	move =  Pokemon.getMove(opt)
	if move != -1:
		move.moveInfo()


'''switch = 	{1 : Status(Pokemon),
			 2 : MoveInfo(Move),}'''

def menu(Pokemon):
	option = 1
	os.system('clear')

	while(option != 0):
		print "===\nMenu:"
		print '\t1) See the Poke\'s stats'
		print '\t2) See the Poke\'s moves'
		print '\t?) To exit...'
		
		print 'Choice:',
		option = input()

		if option == 1:
			Status(Pokemon)
		elif option == 2:
			MoveInfo(Pokemon)
		else:
			option = 0


	os.system('clear')
	print 'Go in the shadow'



def main():
	p1 = Pokemon("Bulba", "Bulbasaur", 11)
	menu(p1)


	#print "Pokemon battle system in Python!"


if __name__ == "__main__": main()