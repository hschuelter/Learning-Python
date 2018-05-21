import argparser

def main(args):
	file = open("entrada.in")
	file.read()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Graph")
	parser.add_argument('--file', '-f',
						type=str,
						help="Select the file to build the Graph",
						default="entrada.in")

	args = parser.parse_args()

	main(args)