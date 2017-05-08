import pygame

pygame.init()

black=(0,0,
	0)
pink=(255,0,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

is_blue=True
x=30
y=30
color=black
screen=pygame.display.set_mode((800,600))

pygame.display.set_caption('Yeba')

exit=False
clock=pygame.time.Clock()
while not exit:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			exit=True
		if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
			is_blue=not is_blue	

	pressed=pygame.key.get_pressed()
	if pressed[pygame.K_UP]:
		color=pink
		y-=3
	if pressed[pygame.K_DOWN]:
		color=black
		y+=3
	if pressed[pygame.K_RIGHT]:
		color=red
		x+=3
	if pressed[pygame.K_LEFT]:
		color=green
		x-=3
	if pressed[pygame.K_SPACE]:
		color=blue
	screen.fill((255,255,255))	
	pygame.draw.rect(screen,color,pygame.Rect(x,y,60,60))
	pygame.display.flip()					
	clock.tick(60)