import pygame

class blocos:
	def __init__(self,posx,posy,img,screen):
		self.img=pygame.image.load(img)	
		self.screen=screen
		self.width=self.img.get_width()
		self.height=self.img.get_height()
		self.posx=posx
		self.posy=posy
		self.rect=self.img.get_rect(topleft=(self.posx, self.posy))

	def colisao(self,player):
		col= self.rect.colliderect(player.rect)
		print(col)
		if col==1:
			if player.dx>0:
				player.dx=0
			
			elif player.dx<0:
				player.dx=0
			
			elif player.dy>0:
				player.dy=0
			
			elif player.dy<0:
				player.dy=0


	def draw(self):
		self.screen.blit(pygame.transform.scale(self.img,(51,51)),(self.posx,self.posy))

