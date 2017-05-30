import pygame
import random
import os

#CORES
Preto = (0,0,0)
Verde = (0,255,0)


Largura=800
Altura=600
FPS= 30

game_folder=os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(img_folder, "bomberman 1.png")).convert()
		self.image.set_colorkey(Preto)
		# self.image=pygame.Surface((50,50))
		# self.image.fill(Verde)
		self.rect = self.image.get_rect()
		self.rect.centerx = Largura/2
		self.rect.bottom = Altura - 20 #ONDE SERA DESENHADA
		self.speedx = 0
		self.speedy= 0
		# self.y_velocidade = 5	 #ONDE SERA DESENHADA

	def update(self):
		self.speedx = 0
		self.speedy = 0
		keystate=pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speedx = -5
		if keystate[pygame.K_RIGHT]:
			self.speedx = 5
		self.rect.x += self.speedx
		if self.rect.right > Largura:
			self.rect.right = Largura
		if self.rect.left < 0:
			self.rect.left = 0
		if keystate[pygame.K_DOWN]:
			self.speedy = 5
		if keystate[pygame.K_UP]:
			self.speedy = -5
		self.rect.y += self.speedy
		if self.rect.bottom > Altura:
			self.rect.bottom = Altura
		if self.rect.top < 0:
			self.rect.top = 0

		# self.rect.x += 5
		# self.rect.y += self.y_velocidade
		# if self.rect.bottom > Altura - 200:
		# 	self.y_velocidade = -5
		# if self.rect.top <200:
		# 	self.y_velocidade = 5
		# if self.rect.left > Largura:
		# 	self.rect.right = 0





pygame.init()
pygame.mixer.init()
tela =  pygame.display.set_mode((Largura,Altura))
pygame.display.set_caption("JOGO")
clock=pygame.time.Clock()

todas_imagens=pygame.sprite.Group()
player = Player()
todas_imagens.add(player)


crashed= False
while not crashed:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True


	todas_imagens.update()

	tela.fill(Preto)
	todas_imagens.draw(tela)

	pygame.display.flip()

pygame.quit()
quit()



