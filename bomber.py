import pygame
import mapa
import numpy as np
class bomber:
	def __init__(self,x,y,img,screen,mapa):
		self.x=x
		self.dx=0
		self.y=y
		self.dy=0
		self.screen=screen
		self.img=pygame.image.load(img)
		self.mapa=mapa
		self.rect=self.img.get_rect(topleft=(self.x, self.y))


	def movimentacao(self):
		pressed=pygame.key.get_pressed()
		
		if pressed[pygame.K_w]:
			self.dy=-3
			self.y=self.y+self.dy
		elif pressed[pygame.K_s]:
			self.dy=3
			self.y=self.y+self.dy
		elif pressed[pygame.K_d]:
			self.dx=3
			self.x=self.x+self.dx
		elif pressed[pygame.K_a]:
			self.dx=-3
			self.x=self.x+self.dx
		self.rect=self.img.get_rect(topleft=(self.x, self.y))

	def draw(self):
		self.screen.blit(pygame.transform.scale(self.img,(70,64)),(self.x,self.y))

		
