import pygame
import time
import random

from libs import Button, MessageBox, InputBox, Colors

pygame.init()



class LevelMultiplication1:

	black = (0,0,0)
	display_width = 800
	display_height = 600
	correct_answers = 0

	def __init__(self, gameDisplay, clock):

		self.gameDisplay = gameDisplay
		self.clock = clock

		self.backgroundImg = pygame.image.load('images/background_2.png')
		self.back_img = pygame.image.load('images/back_icon.png')
		self.back_img_hovered = pygame.image.load('images/back_icon_hovered.png')

		self.illustration_button_img = pygame.image.load('images/button_illustration.png')
		self.illustration_button_img_hovered = pygame.image.load('images/button_illustration_hovered.png')

		self.button_multiplication_skill_1_img = pygame.image.load('images/button_multiplication_skill_1.png')
		self.illustration_text = pygame.image.load('images/illustration_multiplication_1.png')

		## Play button
		self.play_button = pygame.image.load('images/button_play_2.png')
		self.play_button_hovered = pygame.image.load('images/button_play_2_hovered.png')

		self.back_pressed = False


	def generate_numbers(self):
		self.num1 = random.randrange(11,20)
		self.num2 = random.randrange(11,20)

		print(f"Num 1 : {self.num1}, Num 2 : {self.num2}")
		return self.num1, self.num2

	def start(self):

		time.sleep(0.2)

		while True:

			for event in pygame.event.get():
				# print(event)
				if event.type == pygame.QUIT:
					self.quitgame()

			self.gameDisplay.blit(self.backgroundImg, (0,0))

			# Adding multiplication level icon
			self.gameDisplay.blit(self.button_multiplication_skill_1_img, (225,50))

			# Adding back button
			self.add_button(self.back_img, self.back_img_hovered, 100, 70, self.back_press)

			if self.back_pressed == True:
				self.back_pressed = False
				return True

			# Add information/illustration about skill
			self.add_button(self.illustration_button_img, self.illustration_button_img_hovered, 300, 150, self.show_illustration)

			# Add play button
			self.add_button(self.play_button, self.play_button_hovered, 300, 250, self.play)

			pygame.display.update()
			self.clock.tick(15)

	def back_press(self):
		self.back_pressed = True
		time.sleep(0.2)

	def quitgame(self):
		pygame.quit()
		quit()

	def get_font(self, size):
		return pygame.font.Font("freesansbold.ttf", size)


	def text_objects(self, text, font):
		textSurface = font.render(text, True, self.black)
		return textSurface, textSurface.get_rect()

	def message_display(self, text):
		largeText = pygame.font.Font('freesansbold.ttf',32)
		TextSurf, TextRect = self.text_objects(text, largeText)
		TextRect.center = ((self.display_width/2),(self.display_height/4))
		self.gameDisplay.blit(TextSurf, TextRect)

		pygame.display.update()

	def next_question(self):
		self.generate_numbers()
		self.result = self.num1 * self.num2
		self.input_box = InputBox(100, 300, 140, 32, self.result, self.gameDisplay, True)
		self.start_time = pygame.time.get_ticks() 
		# print(f"Setting new question : num1 {self.num1}, num2 {self.num2}, result {self.result}")

	def show_timer(self):
		counting_time = pygame.time.get_ticks() - self.start_time

		 # change milliseconds into minutes, seconds, milliseconds
		counting_minutes = str(int(counting_time/60000)).zfill(2)
		counting_seconds = str( int((counting_time%60000)/1000) ).zfill(2)
		counting_millisecond = str(int(counting_time%1000)).zfill(3)

		counting_string = "%s:%s:%s" % (counting_minutes, counting_seconds, counting_millisecond)

		counting_text = self.get_font(15).render(str(counting_string), 1, (30,30,30))
		counting_rect = counting_text.get_rect()
		counting_rect.top = 50
		counting_rect.right = 750

		self.counting_seconds = int(counting_seconds)

		self.gameDisplay.blit(counting_text, counting_rect)
		self.counting_rect = counting_rect

	def time_out(self):
		return True if (self.counting_seconds < 10) else False

	def show_score(self):
		if hasattr(self, 'counting_rect'):
			right = self.counting_rect.left - 30
		else:
			right = 750

		score_string = f"Score : {str(self.correct_answers).zfill(3)}"

		score_text = self.get_font(15).render(str(score_string), True, (30,30,30))
		score_rect = score_text.get_rect()
		score_rect.top = 50
		score_rect.right = right

		self.gameDisplay.blit(score_text, score_rect)


	def play(self):

		self.next_question()

		self.gameDisplay.blit(self.back_img_hovered, (225,50))

		while True:

			for event in pygame.event.get():
				# print(event)
				if event.type == pygame.QUIT:
					self.quitgame()

				if self.input_box.handle_event(event):
					self.correct_answers += 1
					self.__create_message_box("Correct", self.gameDisplay)
					self.next_question()

			self.gameDisplay.blit(self.backgroundImg, (0,0))

			self.show_timer()
			self.show_score()

			if not self.time_out():
				self.show_answer_n_illustration()
				self.next_question()
				self.correct_answers = 0

			# Adding back button
			self.add_button(self.back_img, self.back_img_hovered, 100, 70, self.back_press)


			self.input_box.update()

			self.input_box.draw(self.gameDisplay)


			if self.back_pressed == True:
				self.back_pressed = False
				return True

			self.message_display(f"{self.num1} x {self.num2}")

			pygame.display.update()
			self.clock.tick(15)

	def display_answer_layer(self, rect, x_offset):

		layers = [1, 2, 3]

		# Adding layer 1 text
		# Adding "Base"
		txt_surface_base = self.get_font(20).render("Base", True, Colors.DARK_RED)
		txt_rect_base = txt_surface_base.get_rect()
		txt_rect_base.top = rect.y+20
		txt_rect_base.left = x_offset + rect.width/2 - txt_rect_base.width/2
		self.gameDisplay.blit(txt_surface_base, txt_rect_base)

		# Each element has : element, Color, y_value, left_value, right_value, centered
		elements_list = [
							# Layer 1
							["Numbers", Colors.DARK_BLUE, rect.y+20, -1, txt_rect_base.left - 10, -1],
							[self.num1, Colors.DARK_BLUE, rect.y+60, -1, txt_rect_base.left - 10, -1],
							[f"x {self.num2}", Colors.DARK_BLUE, rect.y+100, -1, txt_rect_base.left - 10, -1],

							## Base already added.
							["10", Colors.DARK_RED, rect.y+60, -1, txt_rect_base.right, -1],
							["10", Colors.DARK_RED, rect.y+100, -1, txt_rect_base.right, -1],

							["Difference", Colors.DARK_GREEN, rect.y+20, txt_rect_base.right + 10, -1, -1],
							[self.num1-10, Colors.DARK_GREEN, rect.y+60, txt_rect_base.right + 20, -1, -1],
							[self.num2-10, Colors.DARK_GREEN, rect.y+100, txt_rect_base.right + 20, -1, -1],

							# Layer 2
							[f"{self.num1} + {self.num2-10} | {self.num1-10} x {self.num2-10}", Colors.BLACK, rect.y+180, -1, -1, 1],
							[f"{self.num1 + self.num2-10} | {(self.num1-10) * (self.num2-10)}", Colors.BLACK, rect.y+220, -1, -1, 1],

							# Layer 3
							[f"{self.num1} x {self.num2} = {self.result}", Colors.BLACK, rect.y+260, -1, -1, 1],
							]

		## Encountering for "difference multiplication" having more than one digit.
		if ((self.num1-10) * (self.num2-10)) > 9:
			elements_list.pop()
			elements_list.append([f"{self.num1+self.num2-10} + {int((self.num1-10)*(self.num2-10)/10)} | {((self.num1-10) * (self.num2-10))%10}",
								  Colors.BLACK, rect.y+260, -1, -1, 1])
			elements_list.append([f"{self.num1+self.num2-10 + int((self.num1-10)*(self.num2-10)/10)} | {((self.num1-10) * (self.num2-10))%10}",
								  Colors.BLACK, rect.y+300, -1, -1, 1])
			elements_list.append([f"{self.num1} x {self.num2} = {self.result}", Colors.BLACK, rect.y+340, -1, -1, 1])

		for element in elements_list:
			txt_surface = self.get_font(20).render(str(element[0]), True, element[1])
			txt_rect = txt_surface.get_rect()
			txt_rect.top = element[2]

			if element[5] == 1:
				txt_rect.center = (x_offset + rect.width/2, txt_rect.center[1])
			elif element[3] < 0:
				txt_rect.right = element[4]
			else:
				txt_rect.left = element[3]

			self.gameDisplay.blit(txt_surface, txt_rect)

		# Adding layer 1 text
		# Adding "Base"
		txt_surface_base = self.get_font(20).render("Base", True, (176, 63, 55))
		txt_rect_base = txt_surface_base.get_rect()
		txt_rect_base.top = rect.y+20
		txt_rect_base.left = x_offset + rect.width/2 - txt_rect_base.width/2

		# Adding "Numbers"
		txt_surface_numbers = self.get_font(20).render("Numbers", True, (0,0,100))
		txt_rect_numbers = txt_surface_numbers.get_rect()
		txt_rect_numbers.top = rect.y+20
		txt_rect_numbers.right = txt_rect_base.left - 10

		# Adding "Difference"
		txt_surface_difference = self.get_font(20).render("Diference", True, (0,100,0))
		txt_rect_difference = txt_surface_difference.get_rect()
		txt_rect_difference.top = rect.y+20
		txt_rect_difference.left = txt_rect_base.right + 10

		# Adding num1
		txt_surface_num1 = self.get_font(20).render(str(self.num1), True, (0,0,100))
		txt_rect_num1 = txt_surface_num1.get_rect()
		txt_rect_num1.top = rect.y+60
		txt_rect_num1.right = txt_rect_base.left - 10

		# Adding num2
		txt_surface_num2 = self.get_font(20).render(str(self.num2), True, (0,0,100))
		txt_rect_num2 = txt_surface_num2.get_rect()
		txt_rect_num2.top = rect.y+100
		txt_rect_num2.right = txt_rect_base.left - 10

		# self.gameDisplay.blit(txt_surface_base, txt_rect_base)
		# self.gameDisplay.blit(txt_surface_numbers, txt_rect_numbers)
		# self.gameDisplay.blit(txt_surface_difference, txt_rect_difference)

		# self.gameDisplay.blit(txt_surface_num1, txt_rect_num1)
		# self.gameDisplay.blit(txt_surface_num2, txt_rect_num2)

	def show_answer_n_illustration(self):
		print("show_answer_n_illustration")

		center = (self.display_width/2, self.display_height/2)
		width = self.display_width * 0.7
		height = self.display_height * 0.7

		x_pos = center[0] - width/2
		y_pos = center[1] - height/2

		rect = pygame.Rect(x_pos, y_pos, width, height)

		while True:

			for event in pygame.event.get():
				# print(event)
				if event.type == pygame.QUIT:
					self.quitgame()


			# Adding back button
			self.add_button(self.back_img, self.back_img_hovered, rect.x+10, rect.y+10, self.back_press)

			self.display_answer_layer(rect, x_pos)

			# Adding answer illustration
			pygame.draw.rect(self.gameDisplay, (0,0,0), rect, 1)

			if self.back_pressed == True:
				self.back_pressed = False
				return True

			pygame.display.update()
			self.clock.tick(15)


	# Width will be 600
	# Height will be 400
	def show_illustration(self):

		while True:

			for event in pygame.event.get():
				# print(event)
				if event.type == pygame.QUIT:
					self.quitgame()

			self.gameDisplay.blit(self.backgroundImg, (0,0))

			# Adding multiplication level icon
			self.gameDisplay.blit(self.button_multiplication_skill_1_img, (225,50))

			# Adding back button
			self.add_button(self.back_img, self.back_img_hovered, 100, 70, self.back_press)

			# Adding illustration text tutorial
			self.gameDisplay.blit(self.illustration_text, (100,150))

			if self.back_pressed == True:
				self.back_pressed = False
				return True

			pygame.display.update()
			self.clock.tick(15)

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


	def __create_message_box(self, msg, screen):

		center = (self.display_width/2, self.display_height/2)

		msg_width = self.display_width/4
		msg_height = self.display_height/4

		print(f"In __create_message_box, Width {self.display_width}, Height {self.display_height}")
		print(msg)

		msgBox = MessageBox(msg, center, (msg_width, msg_height))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quitgame()

		msgBox.show(screen)

		pygame.display.update()
		self.clock.tick(15)

		time.sleep(2)



