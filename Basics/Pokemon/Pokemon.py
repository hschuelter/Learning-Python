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

		#self.nature = ran.randint(0,24)
		self.gainStat = ran.randint(0,4)
		self.loseStat = ran.randint(0,4)

		self.shiny = (ran.randint(1,8192) / 8192)

		self.moves = []


	def setStats(self, hp, attack, defense, sp_attack, sp_defense, speed):
		self.current_hp = hp

		self.stats = []
		self.stats.append(hp)
		self.stats.append(attack)
		self.stats.append(defense)
		self.stats.append(sp_attack)
		self.stats.append(sp_defense)
		self.stats.append(speed)

		# self.hp = hp
		# self.attack = attack
		# self.defense = defense
		# self.sp_attack = sp_attack
		# self.sp_defense = sp_defense
		# self.speed = speed

	def updateStats(self):

		gain = self.gainStat
		loss = self.loseStat

		if gain == loss:
			return

		self.stats[gain+1] += (self.stats[gain+1])//10

		self.stats[loss+1] = int( (self.stats[loss+1]) - (self.stats[loss+1])/10.0 ) 





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

		print('HP:\t' + str(self.current_hp) + '/' + str(self.stats[0]))


	def printGenericBaseStats(self):
		print('\nBase Stats:')
		print('HP:\t' + str(self.stats[0]))
		print('ATK:\t' + str(self.stats[1]))
		print('DEF:\t' + str(self.stats[2]))
		print('SP.ATK:\t' + str(self.stats[3]))
		print('SP.DEF:\t' + str(self.stats[4]))
		print('SPEED:\t' + str(self.stats[5]))

		print('--\n')

	def printPokeBaseStats(self):
		print('\nBase Stats:')
		print('HP:\t' + str(self.current_hp) + '/' + str(self.stats[0]))
		print('ATK:\t' + str(self.stats[1]))
		print('DEF:\t' + str(self.stats[2]))
		print('SP.ATK:\t' + str(self.stats[3]))
		print('SP.DEF:\t' + str(self.stats[4]))		
		print('SPEED:\t' + str(self.stats[5]))
		

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
		poke.updateStats()
		return poke

	def addOT(self, player):
		self.trainer_ot = player.trainer_id

	def useMove(self, move, target, battle):
		crit = 0

		damage, crit = self.calculateDamage(move, target, battle)

		accuracy = move.accuracy

		luck = ran.randint(0,100)
		move.current_PP -= 1
		miss = 0


		if luck <= accuracy:
			miss = 0
			target.current_hp -= damage
			if target.current_hp < 0:
				target.current_hp = 0 
		else:
			miss = 1

		battle.round()

		print(self.nickname + ' used ' + move.name)
		if crit == 1 and move.category != 2:
			print('It was a critical hit!')

		#print('Luck: ' + str(luck))
		print('Accuracy: ' + str(accuracy))
		print('Damage: ' + str(damage))
		print('')

		if miss == 1:			
			print('But, it missed...')


		if move.category == 2:
			print(move.effect)

		time.sleep(1)

	def calculateModifier(self, move, target, battle):
		weather = battle.weather
		stab = 1
		typing = 1
		rdm = ran.randint(85,100) / 100.0
		crit = 0

		if self.typing[0] == move.typing or self.typing[1] == move.typing:
			stab = 1.5

		#typing = typing * effect(target.typing[0], move.typing) * effect(target.typing[1], move.typing)
		
		#crit, random

		if (ran.randint(1,96) % 16) == 0:
			crit = 1 

		mod = weather * stab * typing * rdm * (crit + 1)

		return mod, crit

	def calculateDamage(self, move, target, battle):
		
		# Physical
		if move.category == 0: 
			a = self.stats[1] 	# ATK
			d = target.stats[2]	# DEF
		
		# Special
		elif move.category == 1:
			a = self.stats[3]	#SP ATK
			d = target.stats[4] #SP DEF
		
		#Other
		else:
			return 0, 0

		modifier, crit = self.calculateModifier(move, target, battle)
		damage = ( ( ( ( ( (2 * self.level)/5.0) + 2) * move.base_power * (a/ (d * 1.0) ) )/ 50.0 ) + 2 ) * modifier
		damage = int(damage) 

		return damage, crit
