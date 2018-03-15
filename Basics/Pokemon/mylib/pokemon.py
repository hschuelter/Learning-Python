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

	# -----------------------------------------------
	# Getters:	
	def getMove(self, position):
		if position > 0 and position <= len(self.moves):
			return self.moves[position-1]
		else:
			print 'Invalid move!'
			return Move()
			
	# -----------------------------------------------

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


	def catchPokemon(self):
		poke = copy.deepcopy(self)
		return poke
