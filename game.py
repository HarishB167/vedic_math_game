import pygame
import time
import random

from game_intro import GameIntro

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Vedic Math Game')
clock = pygame.time.Clock()

backgroundImg = pygame.image.load('images/background.png')


def quitgame():
	pygame.quit()
	quit()



game_intro = GameIntro(gameDisplay, clock)
game_intro.start()

