import pygame as pg
import sys
from setting import *
from sprites import *

img1="Gabriel.png"
img2="bomberman 1.png"
# bombaimg="bomba.png"
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        pass

    def new(self):
        self.players=pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.bomba=pg.sprite.Group()
        self.player1 = Player(self, 1, 1,img1)
        self.player2 = Player(self,5,5,img2)
        self.bomba1=bomba(self,self.player1.x,self.player1.y)
        self.bomba2=bomba(self,self.player2.x,self.player2.y)
        for x in range(1, 15):
            Wall(self, x, 0)
        for y in range (0,11):
        	Wall(self,0,y)
        for x in range(1, 16):
        	Wall(self, x, 10)
        for y in range (1,10):
        	Wall(self,14,y)
        #BLOCOS CENTRO
        for u in list(range(2,14,2)):
        	for i in list(range(2,9,2)):
        		for x in range(u,u+1):
        			Wall(self,x,i)


    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.bomba1.draw(self.player1.x,self.player1.y)
        pg.display.flip()

    def events(self):	 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player1.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player1.move(dx=1)
                if event.key == pg.K_UP:
                    self.player1.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player1.move(dy=1)
                if event.key == pg.K_a:
                	self.player2.move(dx=-1)
                if event.key == pg.K_d:
                	self.player2.move(dx=1)
                if event.key == pg.K_w:
                	self.player2.move(dy=-1)
                if event.key == pg.K_s:
                	self.player2.move(dy=1)
                # if event.key==pg.K_SPACE:

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
