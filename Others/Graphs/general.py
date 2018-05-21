class Graph:
	def __init__(self, file):
		file = file.read().split()
		self.n_vertex = int(file[0])
		self.type = file[1]
		self.n_edges  = int(file[2])

		self.graph = {}

		for i in range(0, self.n_edges):
			origin  = int(file[i*3 + 3])
			destiny = int(file[i*3 + 4])
			weight  = int(file[i*3 + 5])

			if origin in self.graph:
				self.graph[origin].append( (destiny, weight) )
			else:
				self.graph[origin] = [ (destiny ,weight) ]

			if self.type == 'N':
				if destiny in self.graph:
					self.graph[destiny].append( (origin, weight) )
				else:
					self.graph[destiny] = [ (origin ,weight) ]



	def show(self):
		print("Vertex: " + str(self.n_vertex))
		print("Edges: " + str(self.n_edges))
		print("Type: " + self.type)

		for orig, dest in self.graph.items():
			print(orig, '-> ', end='')
			for d, w in dest:
				print("[" + str(d) + "|" + str(w) + "]", end = "  ")
			print()

def rewind(file):
	file.seek(0)

def main():
	file = open("entrada.in", 'r', encoding='utf-8-sig')
	#print(file.read())
	rewind(file)

	g = Graph(file)
	g.show()

if __name__ == "__main__": main()