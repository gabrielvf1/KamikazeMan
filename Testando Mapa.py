import pygame, sys
from pygame.locals import *


CinzaParede = (105,105,105)
CinzaBlocoDestrutivo = (192,192,192)
CinzaBlocoFixo = (128,128,128)
VerdeAndar = (0,128,0)


BlocoFixo = 0
BlocoDestrutivo = 1
Parede = 2
BlocoAndar = 3

Cores = {
			BlocoFixo : CinzaBlocoFixo,
			BlocoDestrutivo : CinzaBlocoDestrutivo,
			Parede : CinzaParede,
			BlocoAndar : VerdeAndar
		}

MapaTile =  [[Parede,Parede,Parede,Parede,Parede,Parede,Parede,Parede,Parede,Parede],
			[Parede,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,Parede],
			[Parede,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,Parede],
			[Parede,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,Parede],
			[Parede,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,Parede],
			[Parede,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,Parede],
			[Parede,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,VerdeAndar,Parede],
			[Parede,Parede,Parede,Parede,Parede,Parede,Parede,Parede,Parede,Parede]]


TamanhoDoQuadrado = 40
MapaProLado = 10
MapaPraCima = 8

pygame.init()
DisplaySurf = pygame.display.set_mode((MapaProLado*TamanhoDoQuadrado,MapaPraCima*TamanhoDoQuadrado))

while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	for row in range(MapaPraCima):
		for coluna in range(MapaProLado):
			pygame.draw.rect(DisplaySurf,Cores[MapaTile[row][coluna]],(coluna*TamanhoDoQuadrado,row*TamanhoDoQuadrado,TamanhoDoQuadrado,TamanhoDoQuadrado))

	pygame.display.update()