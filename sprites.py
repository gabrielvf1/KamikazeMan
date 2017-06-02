import pygame as pg
from settings import *
import os
from MenuPersonagens import *
import time      

game_folder=os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y,img):
        self.player_group=game.players
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        pg.sprite.Sprite.__init__(self, self.player_group)
        self.game = game
        self.img=img
        self.image=pg.image.load(os.path.join(img_folder,img)).convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.limitebombas=2


    def move(self, dx=0, dy=0):
    	if not self.collide_with_walls(dx,dy):
        	self.x += dx
        	self.y += dy


    def collide_with_walls(self,dx=0,dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y==self.y + dy:
                return True
        for player in self.player_group:
            if player.x== self.x + dx and player.y==self.y+dy:
                return True
        for wall in self.game.random_wall:
            if wall.x == self.x + dx and wall.y==self.y + dy:
                return True
        for bomba in self.game.bombas:
            if bomba.x == self.x + dx and bomba.y==self.y + dy:
                return True        
        
        return False



    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game=game
        self.image=pg.image.load(os.path.join(img_folder,"bloco.png")).convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class randwall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.random_wall
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game=game
        self.image=pg.image.load(os.path.join(img_folder,"bloco.png")).convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE



class Bomba(pg.sprite.Sprite):
    def __init__(self, game, player,screen):
        self.groups = game.all_sprites, game.bombas
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game=game
        self.explosao1=pg.sprite.Group()
        self.clock = pg.time.Clock()
        self.image=pg.image.load(os.path.join(img_folder,"Bomba.png")).convert_alpha()
        self.rect=self.image.get_rect()
        self.x = player.x
        self.rect.x=self.x
        self.y = player.y
        self.rect.y=self.y
        self.explosionmoment=game.momento+120
        self.raio=2
        self.screen=screen
        self.x1=0
        self.y1=0
        self.donodabomba=player

    def update(self):
        if self.explosionmoment>=self.game.momento:
            self.rect.x = self.x * TILESIZE
            self.rect.y = self.y * TILESIZE
        else:
            explosao1(self.game,self.x,self.y)
            explosao1(self.game,self.x+1,self.y)
            explosao1(self.game,self.x-1,self.y)   
            explosao1(self.game,self.x,self.y+1)
            explosao1(self.game,self.x,self.y-1)

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

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting=False
                    self.quit()
                    quit()
                if event.type == pg.KEYUP:
                    waiting=False


    def explosao(self,player1,player2,bombs):
        if self.explosionmoment+20==self.game.momento:
            del bombs[0]
            self.donodabomba.limitebombas+=1
            self.kill()
            for i in range(self.raio):
                if (self.x==player1.x and self.y==player1.y) or (self.x+i==player1.x and self.y==player1.y) or (self.x-i==player1.x and self.y==player1.y) \
                or (self.x==player1.x and self.y+i==player1.y) or (self.x==player1.x and self.y-i==player1.y):
                    print("Player 2 ganhou!")
                    self.screen.fill(BLACK)
                    self.title_font =os.path.join(img_folder, 'ZOMBIE.TTF')
                    self.draw_text("Parabens Player 2!!", self.title_font,50,RED,WIDTH/2, HEIGHT/2,align="center")
                    self.draw_text("Pressione Qualquer Tecla para Jogar de Novo", self.title_font,20, WHITE,WIDTH/2,HEIGHT*3/4,align="center")
                    pg.display.flip()
                    self.wait_for_key()
                    self.game.playing=False
                    
                    

            if (self.x==player2.x and self.y==player2.y) or (self.x+i==player2.x and self.y==player2.y) or (self.x-i==player2.x and self.y==player2.y) \
            or (self.x==player2.x and self.y+i==player2.y) or (self.x==player2.x and self.y-i==player2.y):
                self.screen.fill(BLACK)
                self.title_font =os.path.join(img_folder, 'ZOMBIE.TTF')
                self.draw_text("Parabens Player 1!!", self.title_font,45,RED,WIDTH/2, HEIGHT/2,align="center")
                self.draw_text("Pressione Qualquer Tecla para Jogar de Novo", self.title_font,20, WHITE,WIDTH/2,HEIGHT*3/4,align="center")
                pg.display.flip()
                self.wait_for_key()
                self.game.playing=False

class explosao1(pg.sprite.Sprite):
    
    def __init__ (self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game=game
        self.image=pg.image.load(os.path.join(img_folder,"Explosao_meio.png")).convert_alpha()
        self.rect=self.image.get_rect()
        self.x = x*TILESIZE
        self.rect.x=self.x
        self.y =y*TILESIZE
        self.rect.y=self.y
        

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE  
        