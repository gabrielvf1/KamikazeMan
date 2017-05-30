import pygame as pg
from settings import *
import os

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
        self.image=pg.image.load(os.path.join(img_folder,img)).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y


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
        
        return False



    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game=game
        self.image=pg.image.load(os.path.join(img_folder,"bloco.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class bomba(pg.sprite.Sprite):
        def __init__(self,game,x,y):
            self.bomba_group=game.bomba
            pg.sprite.Sprite.__init__(self,self.bomba_group)
            self.game=game
            self.image= pg.image.load(os.path.join(img_folder,"bomba.png")).convert()
            self.rect=self.image.get_rect()
            self.x=x
            self.y=y

        def draw(self,x,y):
            pressed=pg.key.get_pressed()
            if pressed[pg.K_SPACE]:
             self.game.screen.blit(self.image,(x*TILESIZE,y*TILESIZE))
                    # def explosao(self):