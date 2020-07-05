import pygame
from game_play import GamePlay

class GameIntro():

	def __init__(self, gameDisplay, clock):

		self.gameDisplay = gameDisplay
		self.clock = clock

		self.backgroundImg = pygame.image.load('images/background.png')
		self.intro_line_1_img = pygame.image.load('images/intro_line_1.png')

		self.play_button = pygame.image.load('images/button_play.png')
		self.play_button_hovered = pygame.image.load('images/button_play_hovered.png')

		self.quit_button = pygame.image.load('images/button_quit.png')
		self.quit_button_hovered = pygame.image.load('images/button_quit_hovered.png')
	

	def start(self):

		while True:

			for event in pygame.event.get():
				# print(event)
				if event.type == pygame.QUIT:
					self.quitgame()

			self.gameDisplay.blit(self.backgroundImg, (0,0))

			# Add intro line 1
			self.gameDisplay.blit(self.intro_line_1_img, (50,50))

			# Add play button
			self.add_button(self.play_button, self.play_button_hovered, 300, 200, self.play_game)
			self.add_button(self.quit_button, self.quit_button_hovered, 300, 300, self.quitgame)

			pygame.display.update()
			self.clock.tick(15)

	def quitgame(self):
		pygame.quit()
		quit()

	def play_game(self):
		print("Game play : todo")

		game_play = GamePlay(self.gameDisplay, self.clock)
		game_play.start()

	# def add_intro_line_1(self, img, img_hovered, x, y):
	# 	mouse = pygame.mouse.get_pos()
	# 	click = pygame.mouse.get_pressed()

	# 	brighten = 128
		

	# 	if x+img.get_width() > mouse[0] > x and y+img.get_height() > mouse[1] > y:
	# 		self.gameDisplay.blit(img_hovered, (x,y))
	# 	else:
	# 		self.gameDisplay.blit(img, (x,y))

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

