import pygame as pg
import sys
from setting import *
from sprites import *
import random
from MenuPersonagens import *

a=1
Personagems=MenuPersonagem()
class Game:
    def __init__(self):
        pg.init()
        self.loop=True
        # Musica
        musica=["Through The Fire and Flames .mp3 ", "_8 Bit _ Electro House_Lensko - Cetus.mp3","Battle Mode Music - Bomberman 64.mp3","Mortal Kombat 8-bit.mp3"]
        musica_jogo=random.choice(musica)
        pg.mixer.init()
        pg.mixer.music.load(musica_jogo)
        pg.mixer.music.play()

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.momento=0
        self.bombs=[]
 

    def load_data(self):

        pass;

    def new(self):
        self.players=pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.random_wall=pg.sprite.Group()
        self.bombas=pg.sprite.Group()
        self.explosao=pg.sprite.Group()
        self.player1 = Player(self, 1, 1,Personagems[0])
        self.player2 = Player(self,13,9,Personagems[1])
        for x in range(1, 15):
            randwall(self, x, 0)
        for y in range (0,11):
        	randwall(self,0,y)
        for x in range(1, 16):
        	randwall(self, x, 10)
        for y in range (1,10):
        	randwall(self,14,y)
        #BLOCOS CENTRO
        for u in list(range(2,14,2)):
        	for i in list(range(2,9,2)):
        		for x in range(u,u+1):
        			randwall(self,x,i)
        #Blocos aleatorios
        for i in range(15):
         x=random.randrange(2,14,1)
         y=random.randrange(2,8,1)
         if (x!=13 and y!=9):
                randwall(self,x,y)

    def menu(self):
        Personagems=MenuPersonagem()

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
            for bomb in self.bombs:
                bomb.explosao(self.player1,self.player2,self.bombs)    
            self.momento+=1
           
    
    def quit(self):
        sys.exit()

    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill((200,200,200))
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.random_wall.draw(self.screen)
        pg.display.flip()

    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)    

    def events(self):	 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player2.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player2.move(dx=1)
                if event.key == pg.K_UP:
                    self.player2.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player2.move(dy=1)
                if event.key == pg.K_PERIOD and self.player2.limitebombas>0:
                    self.bombs.append(Bomba(self,self.player2,self.screen))
                    self.player2.limitebombas-=1
                if event.key == pg.K_a:
                    self.player1.move(dx=-1)
                if event.key == pg.K_d:
                    self.player1.move(dx=1)
                if event.key == pg.K_w:
                    self.player1.move(dy=-1)
                if event.key == pg.K_s:
                    self.player1.move(dy=1)
                if event.key == pg.K_SPACE and self.player1.limitebombas>0:
                    self.bombs.append(Bomba(self,self.player1,self.screen))
                    self.player1.limitebombas-=1


    def show_start_screen(self):
        pass

    def show_go_screen(self):
        self.screen.fill(BLACK)
        self.loop=False
        pg.display.flip()


g = Game()
g.show_start_screen()



while g.loop:
    if Personagems[2]==1:
        g.menu()
        g.new()
        g.run()
        g.show_go_screen()
