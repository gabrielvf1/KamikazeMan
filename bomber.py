import pygame


class bomber:
	def __init__(self,x,y,img,screen):
		self.x=x
		self.y=y
		self.screen=screen
		self.img=pygame.image.load(img)

	def draw(self):
		self.screen.blit(self.img,(self.x,self.y))


