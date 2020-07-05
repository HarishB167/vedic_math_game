import pygame
import random
import time

from multiplication import LevelMultiplication1

class GamePlay:

	def __init__(self, gameDisplay, clock):

		self.gameDisplay = gameDisplay
		self.clock = clock

		self.backgroundImg = pygame.image.load('images/background_2.png')
		self.level_img = pygame.image.load('images/levels.png')
		self.back_img = pygame.image.load('images/back_icon.png')
		self.back_img_hovered = pygame.image.load('images/back_icon_hovered.png')

		self.button_multiplication_skill_1_img = pygame.image.load('images/button_multiplication_skill_1.png')
		self.button_multiplication_skill_1_img_hovered = pygame.image.load('images/button_multiplication_skill_1_hovered.png')

		self.back_pressed = False


	def start(self):

		while True:

			for event in pygame.event.get():
				# print(event)
				if event.type == pygame.QUIT:
					self.quitgame()

			self.gameDisplay.blit(self.backgroundImg, (0,0))

			# Adding level icon
			self.gameDisplay.blit(self.level_img, (300,50))

			# Adding back button
			self.add_button(self.back_img, self.back_img_hovered, 100, 70, self.back_press)

			# Adding mulitplicatin skill 1 level
			self.add_button(self.button_multiplication_skill_1_img, self.button_multiplication_skill_1_img_hovered, 225, 150, self.multiplication_skill_1)

			if self.back_pressed == True:
				return True

			# self.add_button(self.level_buttong_img, self.level_buttong_img_hovered, 300, 100)

			pygame.display.update()
			self.clock.tick(15)

	def back_press(self):
		self.back_pressed = True
		time.sleep(0.1)

	def multiplication_skill_1(self):
		skill_level = LevelMultiplication1(self.gameDisplay, self.clock)
		skill_level.start()

	def quitgame(self):
		pygame.quit()
		quit()

	def add_button(self, img, img_hovered, x, y, action=None):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if x+img.get_width() > mouse[0] > x and y+img.get_height() > mouse[1] > y:
			self.gameDisplay.blit(img_hovered, (x,y))
			if click[0] == 1 and action != None:
				self.gameDisplay.blit(img, (x,y))
				pygame.display.update()
				action()
		else:
			self.gameDisplay.blit(img, (x,y))


