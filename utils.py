
import pygame

import random

import time

import os


def highscore(finalscore):
    file = "score.txt"
    
    # # Exclusive creation mode: Creates a new file, raises error if file exists

    # try:
    #     with open("file.txt", "x") as f:
    #         f.write("Created using exclusive mode.")
    # except FileExistsError:
    #     print("Already exists.")
    # Append mode: Creates a new file or appends to an existing file

    with open(file, "a") as f:
      score = f'{str(finalscore)}\n'
      f.write(score)
    

def maxscore():

    with open("score.txt", 'r') as f:
        lines = f.readlines()
        maxscore = 0
        for line in lines:
            score = int(line)
            if(score > maxscore):
                maxscore = score
    return maxscore
