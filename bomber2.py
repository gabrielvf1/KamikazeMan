import pygame
import mapa
import numpy as np
class bomber2:
	def __init__(self,x,y,img,screen,mapa):
		self.x=x
		self.dx=0
		self.y=y
		self.dy=0
		self.screen=screen
		self.img=pygame.image.load(img)
		self.mapa=mapa
		self.rect=self.img.get_rect(topleft=(self.x, self.y),width=68, height=62)

	def movimentacao(self):
		pressed=pygame.key.get_pressed()	
		if pressed[pygame.K_UP]:
			self.dy=-3
			self.y=self.y+self.dy
		elif pressed[pygame.K_DOWN]:
			self.dy=3
			self.y=self.y+self.dy
		elif pressed[pygame.K_RIGHT]:
			self.dx=3
			self.x=self.x+self.dx
		elif pressed[pygame.K_LEFT]:
			self.dx=-3
			self.x=self.x+self.dx
		self.rect=self.img.get_rect(topleft=(self.x, self.y),width=68, height=62)

	def draw(self):
		self.screen.blit(pygame.transform.scale(self.img,(68,62)),(self.x,self.y))