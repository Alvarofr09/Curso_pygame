import pygame
import constantes
import math

class Weapon():
	def __init__(self, image, image_bullet):
		self.image_bullet = image_bullet
		self.image_original = image
		self.angle = 0
		self.image = pygame.transform.rotate(self.image_original, self.angle)
		self.shape = self.image.get_rect()
		self.shot = False
		self.last_shot = pygame.time.get_ticks()

	def update(self, character):
		shot_cooldown = constantes.BULLET_COOLDOWN
		bullet = None
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

		#Detectar click del mouse
		#[0] izquierdo, [1] central, [2] derecho
		if pygame.mouse.get_pressed()[0] and self.shot == False and (pygame.time.get_ticks() - self.last_shot >= shot_cooldown):
			bullet = Bullet(self.image_bullet, self.shape.centerx, self.shape.centery, self.angle)
			self.shot = True
			self.last_shot = pygame.time.get_ticks()
		if pygame.mouse.get_pressed()[0] == False:
			self.shot = False
		return bullet

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


class Bullet(pygame.sprite.Sprite):
	def __init__(self, image, x, y, angle):
		pygame.sprite.Sprite.__init__(self)
		self.image_original = image
		self.angle = angle
		self.image = pygame.transform.rotate(self.image_original, self.angle)
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.delta_x = math.cos(math.radians(self.angle)) * constantes.BULLET_VELOZ
		self.delta_y = -math.sin(math.radians(self.angle)) * constantes.BULLET_VELOZ

	def update(self):
		self.rect.x += self.delta_x
		self.rect.y = self.rect.y + self.delta_y

		if self.rect.right < 0 or self.rect.left > constantes.WIDTH_SCREEN or self.rect.bottom < 0 or self.rect.top > constantes.HEIGHT_SCREEN:
			self.kill()

	def draw(self, window):
		window.blit(self.image, (self.rect.centerx, self.rect.centery - int(self.image.get_height())))