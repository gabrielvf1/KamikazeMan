import pygame


class bomber:
	def __init__(self,x,y,img,screen):
		self.x=x
		self.y=y
		self.screen=screen
		self.img=pygame.image.load(img)

	def movimentacao(self):
		pressed=pygame.key.get_pressed()
		if pressed[pygame.K_w]:self.y-=3
		elif pressed[pygame.K_s]:self.y+=3
		elif pressed[pygame.K_d]:self.x+=3
		elif pressed[pygame.K_a]:self.x-=3


	def draw(self):
		self.screen.blit(pygame.transform.scale(self.img,(70,64)),(self.x,self.y))


