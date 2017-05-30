import pygame
import random

#CORES
Preto = (0,0,0)

Largura=800
Altura=600
FPS= 30

pygame.init()
pygame.mixer.init()
screen =  pygame.display.set_mode((WIDHT,HEIGHT)) #Largura, Altura
pygame.display.set_caption("JOGO")
clock=pygame.time.Clock()

todas_imagens=pygame.sprite.Group()

crashed= False
while not crashed:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True




	todas_imagens.update()



	tela.fill(Preto)
	todas_imagens.draw()

	pygame.display.flip()

pygame.quit()
quit()



