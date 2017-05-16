import numpy as np
import pygame
from bloco import blocos

def criar_mapa(bloco,width,height,screen):
	delta_width=np.arange(0,width,50)
	delta_height=np.arange(0,height,50)
	delta_blocos=np.arange(100,width,100)
	delta_bloco2=np.arange(100,height-100,100)
	#Bordas
	for i in delta_height:
		bloco.draw(0,i)
		bloco.draw(width-50,i)
	for i in delta_width:
		bloco.draw(i,0)
		bloco.draw(i,600)


	#Blocos do meio	
	for i in delta_blocos:
		for u in delta_bloco2:	
			bloco.draw(i,u)	