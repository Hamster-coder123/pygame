
import pygame

import random

import time

import os

class fireballs:
    def __init__(self):
        self.ballX = random.randint(0, 852)
        self.ballY = 0
        self.ballvel = 5
        self.ballcol = random.sample(range(0,256), 3)
        self.isdead = False
        self.touch = False

    def falling(self):
        if(self.ballY < 500):
            self.ballY = self.ballY + self.ballvel
            self.isdead = False
        else:
            self.isdead = True
        return self.isdead

    def draw(self, win):
        # pygame.display.update()
        pygame.draw.circle(win,self.ballcol, (self.ballX, self.ballY), 15)

class healthball:
    def __init__(self):
        self.hballX = random.randint(0, 852)
        self.hballY = 0
        self.hballvel = 2
        self.hballcol = (0,0,0)
        self.isdead = False
        self.touch = False

    def falling(self):
        if(self.hballY < 500):
            self.hballY = self.hballY + self.hballvel
            self.isdead = False
        else:
            self.isdead = True
        return self.isdead
    
    def draw(self, win):
        pygame.draw.circle(win,self.hballcol, (self.hballX, self.hballY), 15)

class goblin:
    def __init__(self):
        self.gobvel = 4
        self.isdead = False
        self.touch = False
        
        self.gobY = 410
        self.pick = random.randint(1,2)
        if(self.pick == 1):
            self.gobX = 0
            self.gob = pygame.image.load("gobrun.png")
        else:
            self.gobX = 788
            self.gob = pygame.image.load("gobrun2.png")


    def running(self):
        if(self.pick == 1):
            if(self.gobX < 900):
                self.gobX = self.gobX + self.gobvel
                self.isdead = False
            else:
                self.isdead = True
        else:
            if(self.gobX > 0):
                self.gobX = self.gobX - self.gobvel
                self.isdead = False
            else:
                self.isdead = True    

        return self.isdead
    def draw(self, win):
        win.blit(self.gob,(self.gobX,self.gobY))