pygame.init()

display_width=800
display_height=600
PersonagensDisplay = pygame.display.set_mode((display_width,display_height))
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


def Menu_Personagens(Imagem_Estatica,Personagem1,Personagem2,Personagem3,Personagem4,Iniciar_Jogo,Voltar):
	PersonagensDisplay.blit(Imagem_Estatica(0,0))
	PersonagensDisplay.blit(Personagem1(100,100))
	PersonagensDisplay.blit(Personagem2(300,100))
	PersonagensDisplay.blit(Personagem3(500,100))
	PersonagensDisplay.blit(Personagem4(700,100))
	PersonagensDisplay.blit(Iniciar_Jogo(100,400))
	PersonagensDisplay.blit(Voltar(100,500))

Imagem_Inicial=Menu_Personagens(menu_Img_personagens,Img_personagem1,Img_personagem2,Img_personagem3,Img_personagem4)