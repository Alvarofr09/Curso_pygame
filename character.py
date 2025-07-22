import pygame
import constantes

class Character():
	def __init__(self, x, y):
		self.shape = pygame.Rect(0, 0, constantes.WIDTH_CHARACTER, constantes.HEIGHT_CHARACTER)
		self.shape.center = (x, y)

	def draw(self, window):
		pygame.draw.rect(window, constantes.COLOR_CARACTER, self.shape)

	def move(self, delta_x, delta_y):
		self.shape.x = self.shape.x + delta_x
		self.shape.y = self.shape.y + delta_y