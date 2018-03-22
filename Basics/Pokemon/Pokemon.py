import random as ran
import copy
import time
import os
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

	def useMove(self, move, pokemon, battle):

		damage = self.calculateDamage(move, pokemon, battle)

		accuracy = move.accuracy

		luck = ran.randint(0,100)
		move.current_PP -= 1
		miss = 0


		if luck <= accuracy:
			miss = 0
			pokemon.current_hp -= damage
		else:
			miss = 1

		battle.round()

		print(self.nickname + ' used ' + move.name)

		print('Luck: ' + str(luck))
		print('Accuracy: ' + str(accuracy))
		print('Damage: ' + str(damage))
		print('')

		if miss == 1:			
			print('But, it missed...')


		if move.category == 2:
			print(move.effect)

		time.sleep(1)

	def calculateDamage(self, move, target, battle):
		# Physical
		if move.category == 0: 
			a = self.attack
			d = target.defense
		
		# Special
		elif move.category == 1:
			a = self.sp_attack
			d = target.sp_defense
		
		#Other
		else:
			return 0

		modifier = 1
		damage = ( ( ( ( ( (2 * self.level)/5) + 2) * move.base_power * (a/d) )/ 50.0 ) + 2 ) * modifier
		damage = int(damage) 

		return damage
