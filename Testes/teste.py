import pygame 
pygame.init()
screen=pygame.display.set_mode((800,600))
a = pygame.Rect((1, 1), (2, 2))
b = pygame.Rect((0, 0), (2, 2))
c = pygame.Rect((0, 0), (1, 1))
print(a.colliderect(b))
# 1
print(a.colliderect(c))
# 0
print(b.colliderect(c))
# 1