import numpy as np
import pygame
from bloco import blocos

class mapa:
	def __init__(self,bloco,width,height,screen):
		self.bloco=bloco
		self.width=width
		self.height=height
		self.screen=screen
	
	def draw_map(superior,inferior,esquerda,direita,meio):
		for bloco in superior:
			bloco.draw()

		for bloco in inferior:
			bloco.draw()

		for bloco in esquerda:
			bloco.draw()

		for bloco in direita:
			bloco.draw()

		for bloco in meio:
			bloco.draw()
