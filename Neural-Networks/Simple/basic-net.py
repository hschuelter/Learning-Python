import numpy as np
import os
#
from SimpleNetwork import SimpleNetwork

def net_training(net, input_, output_):
	os.system('clear')

	#synapses
	net.syn0 = 2*np.random.random(( input_.shape[1],net.input)) - 1 # 8 neurons

	net.syn1 = 2*np.random.random((net.input, output_.shape[1])) - 1


	#training
	for i in xrange(100000):
		net.l0 = input_
		net.l1 = net.sigmoid(np.dot(net.l0, net.syn0)) #input layer
		net.l2 = net.sigmoid(np.dot(net.l1, net.syn1)) #output layer

		l2_error = output_ - net.l2

		if(i % 20000) == 0:
			print("(" + str(i/20000) + ") Error: " + str( np.mean(np.abs(l2_error)) ) )

		l2_delta = l2_error * net.deri_sigmoid(net.l2)

		l1_error = l2_delta.dot(net.syn1.T)
		l1_delta = l1_error * net.deri_sigmoid(net.l1)

		#backpropagation

		net.syn0 += net.l0.T.dot(l1_delta)
		net.syn1 += net.l1.T.dot(l2_delta)

	return net

def main():

	#input data

	x = np.array([
				  [0,0,0],
				  [0,1,1],
				  [1,0,1],
				  [1,1,0],
				  [0,0,1],
				  [0,1,0],
				  [1,0,0],
				  [1,1,1]
				])

	#output data

	y = np.array([
				  [0],
				  [0],
				  [0],
				  [0],
				  [1],
				  [1],
				  [1],
				  [1]
				])

	np.random.seed(1)


	in_size = x.shape[0]
	col_in  = x.shape[1]

	out_size= y.shape[0]
	col_out = y.shape[1]

	net = SimpleNetwork(in_size, out_size, col_in, col_out)

	net.train(x, y)

	net.out()

	inputs = np.array([0,0,0])
	print(inputs)
	print( net.think(inputs) )



if __name__ == "__main__": main()