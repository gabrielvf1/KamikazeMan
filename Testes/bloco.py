import pygame

class blocos:
	def __init__(self,img,screen):
		self.img=pygame.image.load(img)
		self.screen=screen
	def draw(self,i,u):
		self.screen.blit(pygame.transform.scale(self.img,(51,51)),(i,u))