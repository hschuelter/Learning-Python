import general
import Queue

class Dijktra_Node:
	def __init__(self, distance, before, after):
		self.distance = distance
		self.before = before
		self.after = after

	def show(self):
		print('[ ', end = '')
		print(self.distance, end = '')
		print(' | ', end = '')
		print(self.before, end = '')
		print(' | ', end = '')
		print(self.after, end = '')
		print(' ]', end = '')

def dijkstra(graph):
	d_array = []
	for i in range (0, graph.n_vertex):
		d_array.append( Dijktra_Node(0, 0, 0) )

	for i in range (0, graph.n_vertex):
		print(str(i) + ': ', end = '')
		d_array[i].show()
		print()


def main():
	print("Main")

if __name__ == "__main__": main()