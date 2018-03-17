from Pokemon import Pokemon
import random as ran
import os

genderlist = ['BOY', 'GIRL', 'OTHER'] #Polemic

class Player:

	def __init__(self, name = 'Red', gender = 1, ):
		self.name = name
		self.trainer_id = ran.randint(0,65535)
		self.gender = gender - 1

		self.PokemonList= []
		self.PokemonBox = [] 
		self.Badges = []

	def playerStats(self):
		os.system('clear')
		print('Player: ' + self.name)
		print('Trainer ID: ' + str(self.trainer_id) )
		print('')
		
		for i in range(0, len(self.PokemonList) ):
			print( str(i+1) + ')'),
			self.PokemonList[i].printSimpleStats()

		print('')