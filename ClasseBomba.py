import pygame
from bomber import bomber

clock=pygame.time.Clock()

class Bomba:
	def __init__(self,momento,bomber,screen):

		self.x=bomber.x
		self.y=bomber.y
		self.screen=screen
		self.img=pygame.image.load('Bomba.png')
		self.explosionMoment = momento + 120		
	def Explosao(self,bomber,bombs):
		del bombs[0]
		if self.x==bomber.x and self.y==bomber.y:
			print ("Morreu!!!")
	def update(self,momento,bomber,bombs):
		if momento == self.explosionMoment:
			self.Explosao(bomber,bombs)
	def drawbomba(self):
		self.screen.blit(pygame.transform.scale(self.img,(50,50)),(self.x,self.y))
