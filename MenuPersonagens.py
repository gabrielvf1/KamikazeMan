import pygame
pygame.init()

display_width=800
display_height=600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Bomberman_Personagens')
clock = pygame.time.Clock()
crashed = False

menu_Img_personagens=pygame.image.load('Imagens\MenuPersonagens\IdeiaMenu.png')
Img_personagem1=pygame.image.load('Imagens\MenuPersonagens\Delc.png')
Img_personagem1_selecionado=pygame.image.load('Imagens\MenuPersonagens\Delc_Selecionado.png')
Img_personagem2=pygame.image.load('Imagens\MenuPersonagens\Gabriel.png')
Img_personagem2_selecionado=pygame.image.load('Imagens\MenuPersonagens\Gabriel_Selecionado.png')
Img_personagem3=pygame.image.load('Imagens\MenuPersonagens\Matheus.png')
Img_personagem3_selecionado=pygame.image.load('Imagens\MenuPersonagens\Matheus_Selecionado.png')
Img_personagem4=pygame.image.load('Imagens\MenuPersonagens\Vini.png')
Img_personagem4_selecionado=pygame.image.load('Imagens\MenuPersonagens\Vini_Selecionado.png')
Img_Inciar_jogo=pygame.image.load('Imagens\MenuPersonagens\Iniciar_jogo.png')
Img_Voltar=pygame.image.load('Imagens\MenuPersonagens\Voltar.png')
Img_Voltar_selecionada=pygame.image.load('Imagens\MenuPersonagens\Voltar_selecionada.png')
Img_Inciar_jogo_selecionada=pygame.image.load('Imagens\MenuPersonagens\Iniciar_jogo_selecionada.png')


def Menu_Personagens(Imagem_Estatica,Personagem1,Personagem2,Personagem3,Personagem4,Iniciar_Jogo,Voltar):
	gameDisplay.blit(Imagem_Estatica,(0,0))
	gameDisplay.blit(pygame.transform.scale(Personagem1,(175,220)),(12.5,65))
	gameDisplay.blit(pygame.transform.scale(Personagem2,(175,220)),(212.5,65))
	gameDisplay.blit(pygame.transform.scale(Personagem3,(175,220)),(412.5,65))
	gameDisplay.blit(pygame.transform.scale(Personagem4,(175,220)),(612.5,65))
	gameDisplay.blit(Iniciar_Jogo,(100,400))
	gameDisplay.blit(Voltar,(100,500))

marcacao_cima_baixo=1
marcacao=1
marcacao_transicao=1
Imagem_menu=Menu_Personagens(menu_Img_personagens,Img_personagem1_selecionado,Img_personagem2,Img_personagem3,Img_personagem4,Img_Inciar_jogo,Img_Voltar)

while not crashed:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			crashed=True
		if event.type==pygame.KEYDOWN:

			if marcacao==1  and event.key == pygame.K_RIGHT:
				Imagem_menu=Menu_Personagens(menu_Img_personagens,Img_personagem1,Img_personagem2_selecionado,Img_personagem3,Img_personagem4,Img_Inciar_jogo,Img_Voltar)
				marcacao=2
				marcacao_cima_baixo=1
			elif marcacao==2 and event.key==pygame.K_RIGHT:
				Imagem_menu=Menu_Personagens(menu_Img_personagens,Img_personagem1,Img_personagem2,Img_personagem3_selecionado,Img_personagem4,Img_Inciar_jogo,Img_Voltar)
				marcacao=3
				marcacao_cima_baixo=1
			elif marcacao==3 and event.key==pygame.K_RIGHT:
				Imagem_menu=Menu_Personagens(menu_Img_personagens,Img_personagem1,Img_personagem2,Img_personagem3,Img_personagem4_selecionado,Img_Inciar_jogo,Img_Voltar)
				marcacao=4
				marcacao_cima_baixo=1
			if marcacao==2 and event.key == pygame.K_LEFT:
				Imagem_menu=Menu_Personagens(menu_Img_personagens,Img_personagem1_selecionado,Img_personagem2,Img_personagem3,Img_personagem4,Img_Inciar_jogo,Img_Voltar)
				marcacao=1
				marcacao_cima_baixo=1
			elif marcacao==3 and event.key == pygame.K_LEFT:
				Imagem_menu=Menu_Personagens(menu_Img_personagens,Img_personagem1,Img_personagem2_selecionado,Img_personagem3,Img_personagem4,Img_Inciar_jogo,Img_Voltar)
				marcacao=2
				marcacao_cima_baixo=1
			elif marcacao==4 and event.key == pygame.K_LEFT:
				Imagem_menu=Menu_Personagens(menu_Img_personagens,Img_personagem1,Img_personagem2,Img_personagem3_selecionado,Img_personagem4,Img_Inciar_jogo,Img_Voltar)
				marcacao=3
				marcacao_cima_baixo=1
			if marcacao_cima_baixo == 1 and event.key == pygame.K_DOWN:
				Imagem_menu=Menu_Personagens(menu_Img_personagens,Img_personagem1,Img_personagem2,Img_personagem3,Img_personagem4,Img_Inciar_jogo_selecionada,Img_Voltar)
				marcacao_cima_baixo=2
				marcacao=1
			elif marcacao_cima_baixo == 2 and event.key == pygame.K_DOWN:
				Imagem_menu=Menu_Personagens(menu_Img_personagens,Img_personagem1,Img_personagem2,Img_personagem3,Img_personagem4,Img_Inciar_jogo,Img_Voltar_selecionada)
				marcacao_cima_baixo=1
			if marcacao_cima_baixo == 1 and event.key == pygame.K_UP:
				Imagem_menu=Menu_Personagens(menu_Img_personagens,Img_personagem1,Img_personagem2,Img_personagem3,Img_personagem4,Img_Inciar_jogo_selecionada,Img_Voltar)
				marcacao_cima_baixo=2
			elif marcacao_cima_baixo==2 and event.key==pygame.K_UP:
				Imagem_menu=Menu_Personagens(menu_Img_personagens,Img_personagem1_selecionado,Img_personagem2,Img_personagem3,Img_personagem4,Img_Inciar_jogo,Img_Voltar)





	pygame.display.update()
	clock.tick(60)
pygame.quit()
quit()	