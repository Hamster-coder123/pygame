'''
falling functions
    fireball movement

death function
    death counter 

main game
    draws everything
    movement inputs
    updates frames
'''

import pygame

import random

import time

import os

from balls import fireballs, healthball, goblin

from thegame import maingame

from utils import highscore, maxscore

pygame.init()


run = True

win = pygame.display.set_mode((852, 480))

starttime = time.time()

audio = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.01)



            









game = maingame()

ball = fireballs()

gob = goblin()

hball = healthball()

startball = time.time()

healthtime = time.time()

gobtime = time.time()

hballist = [hball]

ballist = [ball]

gobllist = [gob]

def gameover(win):
    font = pygame.font.SysFont(None, 100)
    img = font.render(f'{"GAME OVER"}', True, (0,0,0))
    win.blit(img, (250,150))
    pygame.mixer.music.pause()
    my_sound = pygame.mixer.Sound('gameover.mp3')
    my_sound.play()
    my_sound.set_volume(0.5)

def maindraw(ballist, maingame, win, over, hballist, gobllist):
    maingame.draw(win)
    for balls in ballist:
        isdead = balls.falling()
        if(isdead):
            ballist.remove(balls)
        else:
            balls.draw(win)
    if(over):
        gameover(win)
    for hball in hballist:

        hball.falling()
        hball.draw(win)
        if(hball.isdead):
            hballist.remove(hball)
        else:
            hball.draw(win)

    for gob in gobllist:

        gob.running()        
        gob.draw(win)
        if(gob.isdead):
            gobllist.remove(gob)
        else:
            gob.draw(win)

    pygame.display.update()
    return ballist

over = False

while run:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False
    
    if(game.deaths >= game.lives and (not over)):
        over = True
        overtime = time.time()
        maindraw(ballist, game, win, over, hballist, gobllist)
        pygame.time.delay(2000)
        highscore(game.score)
        break
    
    


    game.updatescore(time.time())


    elapsedtime = time.time() - starttime
    game.move(win)
    game.draw(win)
    # print(elapsedtime - starttime)

    if(time.time() - startball > 0.4):
        startball = time.time()
        ballist.append(fireballs())
    ballist = maindraw(ballist, game, win, over, hballist, gobllist)
    game.death(ballist, gobllist)


    if(time.time() - healthtime > 8):
        healthtime = time.time()
        hballist.append(healthball())
    game.addlife(hballist)

    rtime = random.randint(4, 10)

    if(time.time() - gobtime > rtime):
        gobtime = time.time()
        gobllist.append(goblin())
    







'''

A few thoughts on the game:
Ball Game
- Have limited (say 3 lives) that can be displayed as hearts on the screen 
- The goal here is to avoid the objects coming from the sky 
- If an object from the sky touches the character - then a life is lost
- After three lost lives, the game is over 
- The score is based on the number of balls the character is able to dodge 
- The game increases difficulty as one progresses in the game 
- Different types of objects - circles, squares 
- Objects coming in faster
- Different sizes of objects 
- Increased frequency of objects 
More so: 
- Add wind effects (to make the nature a bit more unpredictable) 
- Add sound and visual effects if a life is lost
villain character 
comes from the side and the user has to jump over it 
'''