import pygame

pygame.init()

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

display_width=800
display_height=600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Bomberman')
clock = pygame.time.Clock()
crashed = False

menu_Img=pygame.image.load('menu_teste.png')
iniciar_img=pygame.image.load('iniciar_img_transp.png')
sair_img=pygame.image.load('sair_img_transp.png')
iniciar_img_selecionada=pygame.image.load('iniciar_img_transp_selecionada.png')
sair_img_selecionada=pygame.image.load('sair_img_transp_selecionada.png')
def Menu(ImagemFundo,ImagemIniciar,ImagemSair):
	gameDisplay.blit(ImagemFundo,(0,0))
	gameDisplay.blit(ImagemIniciar,(131,269))
	gameDisplay.blit(ImagemSair,(125,349))


imagemAtual=Menu(menu_Img,iniciar_img_selecionada,sair_img)

while not crashed:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			crashed=True
		imagemAtual
		if event.type==pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				imagemAtual=Menu(menu_Img,iniciar_img,sair_img_selecionada)
			elif event.key == pygame.K_UP:
				imagemAtual=Menu(menu_Img,iniciar_img_selecionada,sair_img)



	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()