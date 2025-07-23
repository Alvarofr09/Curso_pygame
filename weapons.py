import pygame
import constantes
import math

class Weapon():
	def __init__(self, image):
		self.image_original = image
		self.angle = 0
		self.image = pygame.transform.rotate(self.image_original, self.angle)
		self.shape = self.image.get_rect()

	def update(self, character):
		self.shape.center = character.shape.center
		if (character.flip):
			self.shape.x = self.shape.x - character.shape.width/2
			self.flip(True)
		else:
			self.shape.x = self.shape.x + character.shape.width/2
			self.flip(False)

		#Mover pistola con raton
		mouse_pos = pygame.mouse.get_pos()
		dif_x = mouse_pos[0] - self.shape.centerx
		dif_y = - (mouse_pos[1] - self.shape.centery)
		self.angle = math.degrees(math.atan2(dif_y, dif_x))
		if not character.flip:
			if self.angle > 10:
				self.angle = 10
			if self.angle < -12:
				self.angle = -12
		if character.flip:
			if self.angle > 170:
				self.angle = 170
			if self.angle < -155:
				self.angle = -155

	def flip(self, flip):
		if (flip):
			img_flip = pygame.transform.flip(self.image_original, True, False)
			self.image = pygame.transform.rotate(img_flip, self.angle)
		else:
			img_flip = pygame.transform.flip(self.image_original, False, False)
			self.image = pygame.transform.rotate(img_flip, self.angle)

	def draw(self, window):
		self.image = pygame.transform.rotate(self.image, self.angle)
		window.blit(self.image, self.shape)
		#pygame.draw.rect(window, constantes.COLOR_WEAPON, self.shape, 1)