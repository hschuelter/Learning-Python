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

	# -----------------------------------------------
	# Getters:
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

	# -----------------------------------------------



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

