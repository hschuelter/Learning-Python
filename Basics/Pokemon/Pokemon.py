import random as ran
import copy
import time
##
from Player import Player
from Move import Move

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


	def setStats(self, hp, attack, defense, sp_attack, sp_defense, speed):
		self.hp = hp
		self.current_hp = hp

		self.attack = attack
		self.defense = defense
		self.sp_attack = sp_attack
		self.sp_defense = sp_defense
		self.speed = speed

	# -----------------------------------------------
	# Getters:	
	def getMove(self, position):
		if position > 0 and position <= len(self.moves):
			return self.moves[position-1]
		else:
			print ('Invalid move!')
			return Move()
			
	# -----------------------------------------------

	
	def printSimpleStats(self):
		if self.shiny == 0:
			print (self.nickname  + ' (' + self.species + ')'), 
		else:
			print (self.nickname  + ' (' + self.species + ') *'), 

		print ('Level:  ' + str(self.level) )

	def printBattleStats(self):
		if self.shiny == 0:
			print (self.nickname  + ' (' + self.species + ')'), 
		else:
			print (self.nickname  + ' (' + self.species + ') *'), 

		print ('Level:  ' + str(self.level) )

		print('HP:\t' + str(self.current_hp) + '/' + str(self.hp))


	def printGenericBaseStats(self):
		print('\nBase Stats:')
		print('HP:\t' + str(self.hp))
		print('ATK:\t' + str(self.attack))
		print('DEF:\t' + str(self.defense))
		print('SP.ATK:\t' + str(self.sp_attack))
		print('SP.DEF:\t' + str(self.sp_defense))
		print('SPEED:\t' + str(self.speed))

		print('--\n')

	def printPokeBaseStats(self):
		print('\nBase Stats:')
		print('HP:\t' + str(self.current_hp) + '/' + str(self.hp))
		print('ATK:\t' + str(self.attack))
		print('DEF:\t' + str(self.defense))
		print('SP.ATK:\t' + str(self.sp_attack))
		print('SP.DEF:\t' + str(self.sp_defense))
		print('SPEED:\t' + str(self.speed))

		print('--\n')
	

	def learnMove(self, move):
		if len(self.moves) < 4:
			self.moves.append(move)

		else:
			print ('Your Pokemon can\'t learn more than four moves...')
			print ('Choose one to forget:')

			self.printMoves()

			option = input()

			self.moves[option-1] = move


	def changeNickname(self, new_nickname):
		self.nickname = new_nickname


	def catchPokemon(self):
		poke = copy.deepcopy(self)
		return poke

	def addOT(self, player):
		self.trainer_ot = player.trainer_id

	def useMove(self, move, pokemon):
		damage = move.base_power // 4
		accuracy = move.accuracy

		move.current_PP -= 1

		print(self.nickname + ' used ' + move.name)
		print('Damage: ' + str(damage))
		print('Accuracy: ' + str(accuracy))

		luck = ran.randint(0,100)
		if luck < accuracy:
			pokemon.current_hp -= damage
		else:
			print('But, it missed...')

		if move.category == 2:
			print(move.effect)

		time.sleep(2)
