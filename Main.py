import pygame
from bomber import bomber
import numpy as np
import time
from mapa import mapa
from bloco import *
from MenuInicial import MenuInicial
from ClasseBomba import Bomba

MenuInicial()
pygame.init()

#Tela
width=750
height=650	
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("KamikazeMan")
#players
bomber=bomber(50,50,'bomberman 1.png',screen,mapa)

#blocos superior
bloco1=blocos(0,0,'bloco_centro.png',screen)
bloco2=blocos(50,0,'bloco_centro.png',screen)
bloco3=blocos(100,0,'bloco_centro.png',screen)
bloco4=blocos(150,0,'bloco_centro.png',screen)
bloco5=blocos(200,0,'bloco_centro.png',screen)
bloco6=blocos(250,0,'bloco_centro.png',screen)
bloco7=blocos(300,0,'bloco_centro.png',screen)
bloco8=blocos(350,0,'bloco_centro.png',screen)
bloco9=blocos(400,0,'bloco_centro.png',screen)
bloco10=blocos(450,0,'bloco_centro.png',screen)
bloco11=blocos(500,0,'bloco_centro.png',screen)
bloco12=blocos(550,0,'bloco_centro.png',screen)
bloco13=blocos(600,0,'bloco_centro.png',screen)
bloco14=blocos(650,0,'bloco_centro.png',screen)

#blocos esquerdo
bloco15=blocos(0,50,'bloco_centro.png',screen)
bloco16=blocos(0,100,'bloco_centro.png',screen)
bloco17=blocos(0,150,'bloco_centro.png',screen)
bloco18=blocos(0,200,'bloco_centro.png',screen)
bloco19=blocos(0,250,'bloco_centro.png',screen)
bloco20=blocos(0,300,'bloco_centro.png',screen)
bloco21=blocos(0,350,'bloco_centro.png',screen)
bloco22=blocos(0,400,'bloco_centro.png',screen)
bloco23=blocos(0,450,'bloco_centro.png',screen)
bloco24=blocos(0,500,'bloco_centro.png',screen)
bloco25=blocos(0,550,'bloco_centro.png',screen)
bloco26=blocos(0,600,'bloco_centro.png',screen)

#blocos inferior
bloco27=blocos(50,600,'bloco_centro.png',screen)
bloco28=blocos(100,600,'bloco_centro.png',screen)
bloco29=blocos(150,600,'bloco_centro.png',screen)
bloco30=blocos(200,600,'bloco_centro.png',screen)
bloco31=blocos(250,600,'bloco_centro.png',screen)
bloco32=blocos(300,600,'bloco_centro.png',screen)
bloco33=blocos(350,600,'bloco_centro.png',screen)
bloco34=blocos(400,600,'bloco_centro.png',screen)
bloco35=blocos(450,600,'bloco_centro.png',screen)
bloco36=blocos(500,600,'bloco_centro.png',screen)
bloco37=blocos(550,600,'bloco_centro.png',screen)
bloco38=blocos(600,600,'bloco_centro.png',screen)
bloco39=blocos(650,600,'bloco_centro.png',screen)
bloco40=blocos(700,600,'bloco_centro.png',screen)

#blocos direita
bloco41=blocos(700,0,'bloco_centro.png',screen)
bloco42=blocos(700,50,'bloco_centro.png',screen)
bloco43=blocos(700,100,'bloco_centro.png',screen)
bloco44=blocos(700,150,'bloco_centro.png',screen)
bloco45=blocos(700,200,'bloco_centro.png',screen)
bloco46=blocos(700,250,'bloco_centro.png',screen)
bloco47=blocos(700,300,'bloco_centro.png',screen)
bloco48=blocos(700,350,'bloco_centro.png',screen)
bloco49=blocos(700,400,'bloco_centro.png',screen)
bloco50=blocos(700,450,'bloco_centro.png',screen)
bloco51=blocos(700,500,'bloco_centro.png',screen)
bloco52=blocos(700,550,'bloco_centro.png',screen)

#blocos meio
bloco53=blocos(100,100,'bloco_centro.png',screen)
bloco54=blocos(200,100,'bloco_centro.png',screen)
bloco55=blocos(300,100,'bloco_centro.png',screen)
bloco56=blocos(400,100,'bloco_centro.png',screen)
bloco57=blocos(500,100,'bloco_centro.png',screen)

bloco58=blocos(100,200,'bloco_centro.png',screen)
bloco59=blocos(200,200,'bloco_centro.png',screen)
bloco60=blocos(300,200,'bloco_centro.png',screen)
bloco61=blocos(400,200,'bloco_centro.png',screen)
bloco62=blocos(500,200,'bloco_centro.png',screen)
# bloco63=blocos(700,550,'bloco_centro.png',screen)
# bloco64=blocos(700,550,'bloco_centro.png',screen)
# bloco65=blocos(700,550,'bloco_centro.png',screen)
# bloco66=blocos(700,550,'bloco_centro.png',screen)
# bloco67=blocos(700,550,'bloco_centro.png',screen)
# bloco68=blocos(700,550,'bloco_centro.png',screen)
# bloco69=blocos(700,550,'bloco_centro.png',screen)
# bloco70=blocos(700,550,'bloco_centro.png',screen)
# bloco71=blocos(700,550,'bloco_centro.png',screen)


lista_blocos_superior=[bloco1,bloco2,bloco3,bloco4,bloco5,bloco6,bloco7,bloco8,bloco9,bloco10,bloco11,bloco12,bloco13,bloco14]
lista_blocos_inferiores=[bloco27,bloco28,bloco29,bloco30,bloco31,bloco32,bloco33,bloco34,bloco35,bloco36,bloco37,bloco38,bloco39,bloco40]
lista_blocos_esquerda=[bloco15,bloco16,bloco17,bloco18,bloco19,bloco20,bloco21,bloco22,bloco23,bloco24,bloco25,bloco25,bloco26]
lista_blocos_direita=[bloco41,bloco42,bloco43,bloco44,bloco45,bloco46,bloco47,bloco48,bloco49,bloco50,bloco51,bloco52]
lista_blocos_meio=[bloco53,bloco54,bloco55,bloco56,bloco57,bloco58,bloco59,bloco60,bloco61,bloco62]#,bloco63,bloco64,bloco65,bloco66,bloco67,bloco68,bloco69,bloco70,bloco71,bloco27]
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

bombs=[]
momento = 0

while not gameExit:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			gameExit=True
	if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
		clock.tick(5)
		bombs.append(Bomba(momento,bomber,screen))
	for bomb in bombs:
		bomb.drawbomba()
		bomb.update(momento,bomber,bombs)

	bomber.movimentacao()
	print(bloco43.rect) 
	bloco43.colisao(bomber)
	pygame.draw.rect(screen,red,(650,100,51,51))
	mapa.draw_map(lista_blocos_superior, lista_blocos_inferiores, lista_blocos_esquerda, lista_blocos_direita,lista_blocos_meio)
	momento+=1

	bomber.draw()
	pygame.display.flip()
	clock.tick(60)
	screen.fill(cinza)