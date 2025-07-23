import pygame
import constantes

class Character():
	def __init__(self, x, y, animations):
		self.flip = False
		self.animations = animations
		# Imagen de la animacion que se esta mostrando
		self.frame_index = 0
		#Almacenar la hra actual en ms
		self.update_time = pygame.time.get_ticks()
		self.image = animations[self.frame_index]
		self.shape = self.image.get_rect()
		self.shape.center = (x, y)

	def update(self):
		cooldown_animation = 100
		self.image = self.animations[self.frame_index]
		if pygame.time.get_ticks() - self.update_time >= cooldown_animation:
			self.frame_index = self.frame_index + 1
			self.update_time = pygame.time.get_ticks()
		if self.frame_index >= len(self.animations):
			self.frame_index = 0

	def draw(self, window):
		image_flip = pygame.transform.flip(self.image, self.flip, False)
		window.blit(image_flip, self.shape)
		#pygame.draw.rect(window, constantes.COLOR_CARACTER, self.shape, 1)

	def move(self, delta_x, delta_y):
		if delta_x < 0:
			self.flip = True
		if delta_x > 0:
			self.flip = False
		self.shape.x = self.shape.x + delta_x
		self.shape.y = self.shape.y + delta_y