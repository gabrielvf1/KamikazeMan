import pygame as pg
from settings import *
import os
from MenuPersonagens import *


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
    def __init__(self, game, player):
        self.groups = game.all_sprites, game.bombas
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game=game
        self.image=pg.image.load(os.path.join(img_folder,"Bomba.png")).convert_alpha()
        self.rect=self.image.get_rect()
        self.x = player.x
        self.rect.x=self.x
        self.y = player.y
        self.rect.y=self.y
        self.explosionmoment=game.momento+120
        self.raio=2

    def update(self):
        if self.explosionmoment>=self.game.momento:
            self.rect.x = self.x * TILESIZE
            self.rect.y = self.y * TILESIZE
        else:
            self.rect.x = 500 * TILESIZE
            self.rect.y = 500 * TILESIZE
            self.x=500 * TILESIZE
            self.y=500 * TILESIZE   

    def explosao(self,player1,player2,bombs):
         if self.explosionmoment==self.game.momento:
            del bombs[0]
            for i in range(self.raio):
                if (self.x==player1.x and self.y==player1.y) or (self.x+i==player1.x and self.y==player1.y) or (self.x-i==player1.x and self.y==player1.y) \
                or (self.x==player1.x and self.y+i==player1.y) or (self.x==player1.x and self.y-i==player1.y):
                    print("Player 2 ganhou!")
                    self.game.loop=False

            if (self.x==player2.x and self.y==player2.y) or (self.x+i==player2.x and self.y==player2.y) or (self.x-i==player2.x and self.y==player2.y) \
            or (self.x==player2.x and self.y+i==player2.y) or (self.x==player2.x and self.y-i==player2.y):
                    print ("Player 1 ganhou!")
                    self.game.loop=False
    