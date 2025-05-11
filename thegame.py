
import pygame

import random

import time

import os

from utils import highscore, maxscore

class maingame:
    def __init__(self):
        self.grav = 2
        self.jumpspeed = 20
        self.jumpvel = self.jumpspeed
        self.isjump = False
        self.X = 400
        self.Y = 400
        self.vel = 5
        self.deaths = 0
        self.deathflg = False
        self.lives = 5
        self.score = 0
        self.lasttimeupdate = time.time()
        pygame.display.set_caption("Interactive window")
        
            
    def draw(self, win):
        
        if(self.score > maxscore()):
            maxscorenum = self.score
        else:
            maxscorenum = maxscore()
        
        self.back = pygame.image.load("background.jpg")
        self.charR = pygame.image.load("character.png")
        self.charL = pygame.image.load("char2.png")
        self.stand = pygame.image.load("standing.png")
        win.blit(self.back,(0,0))
        win.blit(self.stand,(self.X,self.Y))
        self.font = pygame.font.SysFont(None, 70)
        self.img = self.font.render(f'{self.lives - self.deaths}', True, (0,0,0))
        win.blit(self.img, (20,20))
        self.scorecard = self.font.render(f'{self.score} CS', True, (0,0,0))
        win.blit(self.scorecard, (700, 20))
        self.scorecard = self.font.render(f'{maxscorenum} HS', True, (0,0,0))
        win.blit(self.scorecard, (700, 80))
        
    def move(self, win):
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_a] and self.X > 0):
            self.X = self.X - self.vel 
            win.blit(self.charR,(self.X, self.Y))    

        if(keys[pygame.K_d] and self.X < 852 - 64):
            self.X = self.X + self.vel 
            win.blit(self.charL,(self.X, self.Y))   
    
        if(not self.isjump):
            if(keys[pygame.K_SPACE] ):
                self.isjump = True
        else:
            self.Y -= self.jumpspeed
            self.jumpspeed -= self.grav
            if(self.jumpspeed < -self.jumpvel):
                self.isjump = False
                self.jumpspeed = self.jumpvel

    def deathsound(self):
        pygame.mixer.music.pause()
        my_sound = pygame.mixer.Sound('death.mp3')
        my_sound.play()
        my_sound.set_volume(0.5)
        pygame.mixer.music.unpause()


    def lifesound(self):
        pygame.mixer.music.pause()
        my_sound = pygame.mixer.Sound('life.mp3')
        my_sound.play()
        my_sound.set_volume(0.5)
        pygame.mixer.music.unpause()



    def death(self, ballist, gobllist):
        self.threshx = self.X + 64
        self.threshx2 = self.X
        self.threshy = self.Y + 64
        self.threshy2 = self.Y 
        
        for balls in ballist:
            ballX = balls.ballX
            ballY = balls.ballY

            if(not balls.touch):
                if((ballX < self.threshx) and (ballX > self.threshx2)): 
                    if((ballY < self.threshy) and (ballY > self.threshy2)):
                        self.deaths = self.deaths + 1
                        print(self.deaths, "deaths")
                        self.deathsound()
                        balls.touch = True

        for gob in gobllist:
            gobX = gob.gobX
            gobY = gob.gobY

            if(not gob.touch):
                if((gobX < self.threshx) and (gobX > self.threshx2)): 
                    if((gobY < self.threshy) and (gobY > self.threshy2)):
                        self.deaths = self.deaths + 4
                        print(self.deaths, "deaths")
                        self.deathsound()
                        gob.touch = True






    def updatescore(self, currenttime):
        if(currenttime - self.lasttimeupdate > 0.5):
            self.score += 1
            self.lasttimeupdate = currenttime




    def addlife(self, hlist):
        for hball in hlist:
             
            if(not hball.touch):
                if((hball.hballX < self.threshx) and (hball.hballX > self.threshx2)): 
                    if((hball.hballY < self.threshy) and (hball.hballY > self.threshy2)):
                        self.lives += 1
                        print("+ 1 life")
                        self.lifesound()
                        hball.touch = True

