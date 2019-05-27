#Класс отвечает за работу с блоками на игровом поле

import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from pygame.rect import  Rect
def ini_blocks(seed_mat):
    bloks = []
    x = y = 100
    for row in seed_mat:
        for col in row:
            bloks.append(block(x, y, col))
            x += 40
        y += 40
        x = 100
    return bloks
def swap_block(bloks,i,j,swaps):
    bloks[i].x ,bloks[j].x = bloks[j].x, bloks[i].x
    bloks[i].y, bloks[j].y = bloks[j].y, bloks[i].y
    swaps+=1
    return swaps
def colider(pos,bloks):
    for i in range(len(bloks)):
        if bloks[i].colid(pos):
             return i
    return -1
def neighb(a,b):
    if((a.x==b.x)or(a.y==b.y))and(a.x<=b.x+40)and(a.x>=b.x-40)and(a.y<=b.y+40)and(a.y>=b.y-40):
        return 1
    return 0
class block(Sprite):
    def __init__(self,x,y,role):
        Sprite.__init__(self)

        self.role = role
        if(role==1):
            self.image = pygame.image.load('img/block.jpg').convert()
        elif(role==2):
            self.image = pygame.image.load('img/red.jpg').convert()
        elif(role == 3):
            self.image = pygame.image.load('img/Violet.jpg').convert()
        elif (role == 4):
            self.image = pygame.image.load('img/yellow.jpg').convert()
        elif (role == 0):
            self.image = pygame.image.load('img/yellow.jpg').convert()
            self.image.set_alpha(0)
        self.x = x
        self.y = y
    def draw(self,surf):
        surf.blit(self.image,(self.x,self.y))
    def colid(self,pos):
        if((pos[0]>self.x)and(pos[0]<(self.x+40))):
            if ((pos[1] > self.y) and (pos[1] < (self.y + 40))):
                return 1
        return 0

