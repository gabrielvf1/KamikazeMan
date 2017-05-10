import pygame
from bomber import bomber
import numpy as np
import time
from mapa import criar_mapa
from bloco import blocos

pygame.init()

#Tela
width=750
height=650	
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("KamikazeMan")
#Images
bloco_centro=blocos('bloco_centro.png',screen)

#Cores
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
purple=(255,0,255)
yellow=(255,255,0)
cyan=(0,255,255)
cinza = (211,211,211)


gameExit=False

clock=pygame.time.Clock()
#Sprites
bomber=bomber(50,50,'bomberman 1.png',screen)

while not gameExit:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			gameExit=True

	bomber.movimentacao()		
	criar_mapa(bloco_centro,width,height,screen)

	bomber.draw()
	pygame.display.flip()
	clock.tick(60)
	screen.fill(cinza)