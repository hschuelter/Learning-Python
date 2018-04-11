import numpy as np
import os

class SimpleNetwork:

	def __init__(self, _in, _out, col_input, col_output, hidden=1):
		# _in  is the number of neurons in input layer
		# _out is the number of neurons in output layer
		# col_input is the number of columns of the input data
		
		self.input = _in
		self.output = _out
		self.col_input = col_input
		self.col_output= col_output


		self.l0 = np.zeros( (self.input, self.input) )	# input data
		self.l1 = np.zeros( (self.input, self.input) ) 	# input layer
		self.l2 = np.zeros( (1, _out) )		# output layer

		#self.syn = np.zeros(hidden + 1)
		self.syn0 = np.zeros( (self.col_input, self.input) )
		self.syn1 = np.zeros( (  self.input,   self.col_output) )


	def train(self, inputs, outputs):
		os.system('clear')
		#synapses
		self.syn0 = 2*np.random.random(( inputs.shape[1],self.input)) - 1 # 8 neurons

		self.syn1 = 2*np.random.random((self.input, outputs.shape[1])) - 1


		#training
		for i in xrange(100000):
			self.l0 = inputs
			self.l1 = self.sigmoid(np.dot(self.l0, self.syn0)) #input layer
			self.l2 = self.sigmoid(np.dot(self.l1, self.syn1)) #output layer

			l2_error = outputs - self.l2

			if(i % 20000) == 0:
				print("(" + str(i/20000) + ") Error: " + str( np.mean(np.abs(l2_error)) ) )

			l2_delta = l2_error * self.deri_sigmoid(self.l2)

			l1_error = l2_delta.dot(self.syn1.T)
			l1_delta = l1_error * self.deri_sigmoid(self.l1)

			#backpropagation

			self.syn0 += self.l0.T.dot(l1_delta)
			self.syn1 += self.l1.T.dot(l2_delta)

	def think(self, inputs):
		l1 = np.zeros( (self.input, self.input) )
		l1 = self.sigmoid(np.dot(inputs, self.syn0))
		answer =  self.sigmoid(np.dot(l1, self.syn1))

		return answer


	
	def out(self, stat=False):
		print('\n=====')
		print('Output after training:')
		print(self.l2)		
		print('')

	def sigmoid(self, x):
		return 1/(1 + np.exp(-x))

	def deri_sigmoid(self, x):
		return x * (1-x)
