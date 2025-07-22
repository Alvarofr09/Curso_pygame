import constantes
from character import Character

import pygame

player = Character(50, 50)

pygame.init()

window = pygame.display.set_mode((constantes.WIDTH_SCREEN, constantes.HEIGHT_SCREEN))
pygame.display.set_caption("Juego de prueba")
running = True

while(running):
	player.draw(window)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.update()

pygame.quit()