import pygame
import constantes
from character import Character
from weapons import Weapon
import os


# Funciones
# Escalar imagenes
def scale_img(image, scale):
	w = image.get_width()
	h = image.get_height()
	new_image = pygame.transform.scale(image, (w*scale, h*scale))
	return new_image

# Contar elementos
def count_element(folder):
	return len(os.listdir(folder))

# Listar nombres elementos
def folder_name(folder):
	return os.listdir(folder)


pygame.init()

window = pygame.display.set_mode((constantes.WIDTH_SCREEN, constantes.HEIGHT_SCREEN))
pygame.display.set_caption("Juego de prueba")



# Importar imagenes
animations = []
for i in range(7):
	img = pygame.image.load(f"assets//images//characters//player//player_{i}.png")
	img = scale_img(img, constantes.SCALE_CHARACTER)
	animations.append(img)

# Enemigos
folder_enemies = "assets/images/characters/enemies"
enemies_types = folder_name(folder_enemies)
animations_enemies = []
for types in enemies_types:
	lista_temp = []
	ruta_temp = f"assets/images/characters/enemies/{types}"
	num_animations = count_element(ruta_temp)

# Arma
gun_image = pygame.image.load("assets//images//weapons//gun.png")
gun_image = scale_img(gun_image, constantes.SCALE_GUN)

# Bullet
bullet_image = pygame.image.load("assets//images//weapons//bullet.png")
bullet_image = scale_img(bullet_image, constantes.SCALE_BULLET)

# Crear jugador
player = Character(60, 60, animations)

# Crear arma
gun = Weapon(gun_image, bullet_image)

#crear un grupo de sprites
bullet_group = pygame.sprite.Group()

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

	# Mover jugador
	player.move(delta_x, delta_y)

	#Animacion de jugador
	player.update()
	bullet = gun.update(player)
	if bullet:
		bullet_group.add(bullet)
	for bullet in bullet_group:
		bullet.update()
	
	#print(bullet_group)
	
	
	player.draw(window)
	gun.draw(window)
	for bullet in bullet_group:
		bullet.draw(window)
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