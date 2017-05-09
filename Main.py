import pygame
from bomber import bomber

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("KamikazeMan")

#Cores
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
purple=(255,0,255)
yellow=(255,255,0)
cyan=(0,255,255)


gameExit=False

clock=pygame.time.Clock()

bomber=bomber(50,50,'bomberman 1.png',screen)
while not gameExit:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			gameExit=True

	#movimentacao
	pressed=pygame.key.get_pressed()
	if pressed[pygame.K_w]:bomber.y-=3
	elif pressed[pygame.K_s]:bomber.y+=3
	elif pressed[pygame.K_d]:bomber.x+=3
	elif pressed[pygame.K_a]:bomber.x-=3

	screen.fill(black)
	bomber.draw()
	pygame.display.flip()
	clock.tick(60)