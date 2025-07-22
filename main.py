import constantes
from character import Character

import pygame

pygame.init()

window = pygame.display.set_mode((constantes.WIDTH_SCREEN, constantes.HEIGHT_SCREEN))
pygame.display.set_caption("Juego de prueba")

player = Character(50, 50)


# Variables de movimineot
move_up = False
move_down = False
move_left = False
move_right = False

# Crontolar Frame Rate
clock = pygame.time.Clock()

running = True

while(running):
	# FPS
	clock.tick(constantes.FPS)

	window.fill(constantes.COLOR_BG)
	# Calcular mov jugador
	delta_x = 0
	delta_y = 0

	if move_right == True:
		delta_x = constantes.VELOZ
	if move_left == True:
		delta_x = -constantes.VELOZ
	if move_up == True:
		delta_y = -constantes.VELOZ
	if move_down == True:
		delta_y = constantes.VELOZ

	# MOver jugador
	player.move(delta_x, delta_y)

	player.draw(window)
	for event in pygame.event.get():
		# Cerrar el juego
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN	:
			if event.key == pygame.K_a:
				move_left = True
			if event.key == pygame.K_d:
				move_right = True
			if event.key == pygame.K_w:
				move_up = True
			if event.key == pygame.K_s:
				move_down = True
			if event.key == pygame.K_ESCAPE:
				running = False
			
		if event.type == pygame.KEYUP	:
			if event.key == pygame.K_a:
				move_left = False
			if event.key == pygame.K_d:
				move_right = False
			if event.key == pygame.K_w:
				move_up = False
			if event.key == pygame.K_s:
				move_down = False

	pygame.display.update()

pygame.quit()