import pygame
import os,sys
import time

from pygame.constants import *
White = (255,255,255)
tela=pygame.display.set_mode((300,200))
tela.fill((White))
rect1=pygame.Surface((50,50))
rect1.fill((255,0,0))
tela.blit(rect1,(125,75))
pygame.display.update()
time.sleep(4)