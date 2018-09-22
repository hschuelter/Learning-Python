import Settings
import pygame
import random

def setup():
	# resolution = (1280, 720)
	resolution = (720, 540)

	pygame.display.set_caption('Joguito')
	screen  = pygame.display.set_mode(resolution)

	return screen


def draw(screen):
	background = (255, 255, 255)

	info = pygame.display.Info()
	w = info.current_w
	h = info.current_h

	circle_radius = 5
	circle_thickness = 5

	screen.fill(background)
	pygame.draw.circle(screen, (0,0,255), (random.randint(circle_radius, w - circle_radius ), random.randint(circle_radius, h - circle_radius)), circle_radius, circle_thickness)
	update(screen)


def update(screen):
	pygame.display.flip()

def main():
	print("Starting...")
	screen = setup()

	running = True
	while(running):
		draw(screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

if __name__ == "__main__": main()
