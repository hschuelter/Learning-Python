import pygame
import random
##
from Settings import Settings
##

def setup():
	# resolution = (1280, 720)
	resolution = (720, 540)
	settings = Settings(resolution, 60)

	pygame.display.set_caption('Joguito')
	screen  = pygame.display.set_mode(resolution)

	return screen, settings


def draw(screen, settings):
	background = (0, 0, 0)
	color = (180, 180, 255)
	black = (10,10,10)
	white = (230,230,230)

	w = settings.resolution[0]
	h = settings.resolution[1]

	y_num = 20
	x_num = 20
	thicc = 10
	cont = 0

	screen.fill(background)
	for y in range(0, y_num):
		for x in range(0, x_num):

			if(cont % 2 == 0):
				color = white
			else:
				color = black
			pygame.draw.rect(screen, color,
							( (w * x) / x_num, 	 # X Starting point
							(h * y) / y_num,	 # Y Starting point
							(w / x_num),		 # X size
							(h / y_num)))		 # Y size
			cont += 1
	update()


def update():
	pygame.display.flip()

def main():
	print("Starting...")

	screen, settings = setup()

	running = True
	while(running):
		draw(screen, settings)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

if __name__ == "__main__": main()
