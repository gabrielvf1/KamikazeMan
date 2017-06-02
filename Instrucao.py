import pygame
def Instrucao():
    pygame.init()
    black = (0,0,0)
    white=(255,255,255)
    red=(255,0,0)
    display_width=800
    display_height=600
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Bomberman')
    clock = pygame.time.Clock()
    crashed = False

    intrucao_img = pygame.image.load('img\InstrucaoNovo.png')
    def Instru(ImagemFundo):
        gameDisplay.blit(ImagemFundo,(0,0))
    Instru(intrucao_img)
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    return
        

        pygame.display.update()
        clock.tick(60)


    pygame.quit()
    quit()
