import pygame
import time
import random

from libs import Button, MessageBox, InputBox, Colors, Level

pygame.init()


class Multiplication():

	def __init__(self, gameDisplay, clock):

		self.gameDisplay = gameDisplay
		self.clock = clock

		self.illustration_button_img = pygame.image.load('images/button_illustration.png')
		self.illustration_button_img_hovered = pygame.image.load('images/button_illustration_hovered.png')

		self.button_multiplication_skill_1_img = pygame.image.load('images/button_multiplication_skill_1.png')
		self.illustration_text = pygame.image.load('images/illustration_multiplication_1.png')

		self.backgroundImg = pygame.image.load('images/background_2.png')
		self.back_img = pygame.image.load('images/back_icon.png')
		self.back_img_hovered = pygame.image.load('images/back_icon_hovered.png')

		self.level_1_img = pygame.image.load('images/button_level_1.png')
		self.level_2_img = pygame.image.load('images/button_level_2.png')
		self.level_3_img = pygame.image.load('images/button_level_3.png')
		self.level_1_hovered_img = pygame.image.load('images/button_level_1_hovered.png')
		self.level_2_hovered_img = pygame.image.load('images/button_level_2_hovered.png')
		self.level_3_hovered_img = pygame.image.load('images/button_level_3_hovered.png')

		self.back_pressed = False

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

			# Add Level 1,2 & 3 buttons
			self.add_button(self.level_1_img, self.level_1_hovered_img, 300, 250, self.play_level_1)
			self.add_button(self.level_2_img, self.level_2_hovered_img, 300, 350, self.play_level_2)
			self.add_button(self.level_3_img, self.level_3_hovered_img, 300, 450, self.play_level_3)

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

	def back_press(self):
		self.back_pressed = True
		time.sleep(0.2)

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

	def play_level_1(self):
		level_1 = LevelMultiplication1(self.gameDisplay, self.clock)
		level_1.start()

	def play_level_2(self):
		pass
	
	def play_level_3(self):
		level_3 = LevelMultiplication3(self.gameDisplay, self.clock)
		level_3.start()	


class LevelMultiplication1(Level):

	display_width = 800
	display_height = 600
	correct_answers = 0	

	def __init__(self, gameDisplay, clock):
		super().__init__(gameDisplay, clock)

		self.button_multiplication_skill_1_img = pygame.image.load('images/button_multiplication_skill_1.png')
		self.illustration_text = pygame.image.load('images/illustration_multiplication_1.png')

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
			# self.add_button(self.illustration_button_img, self.illustration_button_img_hovered, 300, 150, self.show_illustration)

			# Add play button
			self.add_button(self.play_button, self.play_button_hovered, 300, 150, self.play)

			pygame.display.update()
			self.clock.tick(15)

	def next_question(self):
		self.generate_numbers()
		self.result = self.num1 + (self.num2-10)
		if hasattr(self, 'input_box'):
			self.input_box = InputBox(self.input_box.rect.x, self.input_box.rect.y, 96, 32, self.result, self.gameDisplay, True)

		self.start_time = pygame.time.get_ticks() 
		# print(f"Setting new question : num1 {self.num1}, num2 {self.num2}, result {self.result}")

	def play(self):

		self.next_question()

		self.gameDisplay.blit(self.back_img_hovered, (225,50))

		while True:

			for event in pygame.event.get():
				# print(event)
				if event.type == pygame.QUIT:
					self.quitgame()

				if hasattr(self, "input_box") and self.input_box.handle_event(event):
					self.correct_answers += 1
					self.timeout_time = max(10 - int(self.correct_answers / 10), 3)
					self.create_message_box("Correct", self.gameDisplay)
					self.next_question()

			self.gameDisplay.blit(self.backgroundImg, (0,0))

			self.show_timer()
			self.show_score()

			if not self.time_out():
				self.show_answer_n_illustration()
				self.next_question()
				self.correct_answers = 0
				self.timeout_time = 10

			# Adding back button
			self.add_button(self.back_img, self.back_img_hovered, 100, 70, self.back_press)

			self.show_question()


			self.input_box.update()

			self.input_box.draw(self.gameDisplay)


			if self.back_pressed == True:
				self.back_pressed = False
				return True

			# self.message_display(f"{self.num1} x {self.num2}")

			pygame.display.update()
			self.clock.tick(15)

	def show_question(self):
		center_of_box_x = self.display_width / 2

		y_offset = 100

		# Adding layer 1 text
		# Adding "Base"
		txt_surface_base = self.get_font(20).render("Base", True, Colors.DARK_RED)
		txt_rect_base = txt_surface_base.get_rect()
		txt_rect_base.top = y_offset+20
		txt_rect_base.left = self.display_width/2 - txt_rect_base.width/2
		self.gameDisplay.blit(txt_surface_base, txt_rect_base)

		# Each element has : element, Color, y_value, left_value, right_value, centered
		elements_list = [
							# Layer 1
							["Numbers", Colors.DARK_BLUE, y_offset+20, -1, txt_rect_base.left - 10, -1],
							[self.num1, Colors.DARK_BLUE, y_offset+60, -1, txt_rect_base.left - 10, -1],
							[f"x {self.num2}", Colors.DARK_BLUE, y_offset+100, -1, txt_rect_base.left - 10, -1],

							## Base already added.
							["10", Colors.DARK_RED, y_offset+60, -1, txt_rect_base.right, -1],
							["10", Colors.DARK_RED, y_offset+100, -1, txt_rect_base.right, -1],

							["Difference", Colors.DARK_GREEN, y_offset+20, txt_rect_base.right + 10, -1, -1],
							[self.num1-10, Colors.DARK_GREEN, y_offset+60, txt_rect_base.right + 20, -1, -1],
							[self.num2-10, Colors.DARK_GREEN, y_offset+100, txt_rect_base.right + 20, -1, -1],

							# Layer 2
							# [f"{self.num1} + {self.num2-10}", Colors.BLACK, rect.y+180, -1, center_of_box_x-10, -1],
							# [f"|", Colors.BLACK, rect.y+180, -1, center_of_box_x, -1],
							# [f"{self.num1-10} x {self.num2-10}", Colors.BLACK, rect.y+180, center_of_box_x+10, -1, -1],

							# [f"{self.num1 + self.num2-10} | {(self.num1-10) * (self.num2-10)}", Colors.BLACK, rect.y+220, -1, -1, 1],

							["input_box", f"{self.num1 + self.num2-10}", Colors.BLACK, y_offset+220, -1, center_of_box_x-10, -1],
							[f"|", Colors.BLACK, y_offset+220, -1, center_of_box_x, -1],
							# [f"{(self.num1-10) * (self.num2-10)}", Colors.BLACK, rect.y+220, center_of_box_x+10, -1, -1],

							# Layer 3
							# [f"{self.num1} x {self.num2} = {self.result}", Colors.BLACK, rect.y+260, -1, -1, 1],
						]
		for element in elements_list:
			if element[0] == "input_box":
				if not hasattr(self, "input_box"):
					self.input_box = InputBox(element[5]-50, element[3], 96, 32, self.result, self.gameDisplay, True)
				continue
			txt_surface = self.get_font(20).render(str(element[0]), True, element[1])
			txt_rect = txt_surface.get_rect()
			txt_rect.top = element[2]

			if element[5] == 1:
				txt_rect.center = (self.display_width/2, txt_rect.center[1])
			elif element[3] < 0:
				txt_rect.right = element[4]
			else:
				txt_rect.left = element[3]

			self.gameDisplay.blit(txt_surface, txt_rect)

	def display_answer_layer(self, rect, x_offset):

		center_of_box_x = x_offset + rect.width/2

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
							[f"{self.num1} + {self.num2-10}", Colors.BLACK, rect.y+180, -1, center_of_box_x-10, -1],
							[f"|", Colors.BLACK, rect.y+180, -1, center_of_box_x, -1],
							[f"{self.num1-10} x {self.num2-10}", Colors.BLACK, rect.y+180, center_of_box_x+10, -1, -1],

							# [f"{self.num1 + self.num2-10} | {(self.num1-10) * (self.num2-10)}", Colors.BLACK, rect.y+220, -1, -1, 1],

							[f"{self.num1 + self.num2-10}", Colors.BLACK, rect.y+220, -1, center_of_box_x-10, -1],
							[f"|", Colors.BLACK, rect.y+220, -1, center_of_box_x, -1],
							[f"{(self.num1-10) * (self.num2-10)}", Colors.BLACK, rect.y+220, center_of_box_x+10, -1, -1],

							# Layer 3
							[f"{self.num1} x {self.num2} = {self.num1 * self.num2}", Colors.BLACK, rect.y+260, -1, -1, 1],
						]

		## Encountering for "difference multiplication" having more than one digit.
		if ((self.num1-10) * (self.num2-10)) > 9:
			elements_list.pop()

			element_1_1 = [f"{self.num1+self.num2-10} + {int((self.num1-10)*(self.num2-10)/10)}", Colors.BLACK, rect.y+260, -1, center_of_box_x-10, -1]
			element_1_2 = [f"|", Colors.BLACK, rect.y+260, -1, center_of_box_x, -1]
			element_1_3 = [f"{((self.num1-10) * (self.num2-10))%10}", Colors.BLACK, rect.y+260, center_of_box_x+10, -1, -1]


			element_2_1 = [f"{self.num1+self.num2-10 + int((self.num1-10)*(self.num2-10)/10)}", Colors.BLACK, rect.y+300, -1, center_of_box_x-10, -1]
			element_2_2 = [f"|", Colors.BLACK, rect.y+300, -1, center_of_box_x, -1]
			element_2_3 = [f"{((self.num1-10) * (self.num2-10))%10}", Colors.BLACK, rect.y+300, center_of_box_x+10, -1, -1]

			element_3 = [f"{self.num1} x {self.num2} = {self.num1 * self.num2}", Colors.BLACK, rect.y+340, -1, -1, 1]

			elements_list.append(element_1_1)
			elements_list.append(element_1_2)
			elements_list.append(element_1_3)
			elements_list.append(element_2_1)
			elements_list.append(element_2_2)
			elements_list.append(element_2_3)
			elements_list.append(element_3)

		for element in elements_list:
			txt_surface = self.get_font(20).render(str(element[0]), False, element[1])
			txt_rect = txt_surface.get_rect()
			txt_rect.top = element[2]

			if element[5] == 1:
				txt_rect.center = (x_offset + rect.width/2, txt_rect.center[1])
			elif element[3] < 0:
				txt_rect.right = element[4]
			else:
				txt_rect.left = element[3]

			self.gameDisplay.blit(txt_surface, txt_rect)

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


class LevelMultiplication3(Level):

	display_width = 800
	display_height = 600
	correct_answers = 0

	def __init__(self, gameDisplay, clock):

		super().__init__(gameDisplay, clock)

		self.button_multiplication_skill_1_img = pygame.image.load('images/button_multiplication_skill_1.png')
		self.illustration_text = pygame.image.load('images/illustration_multiplication_1.png')

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

	def next_question(self):
		self.generate_numbers()
		self.result = self.num1 * self.num2
		self.input_box = InputBox(100, 300, 140, 32, self.result, self.gameDisplay, True)
		self.start_time = pygame.time.get_ticks() 
		# print(f"Setting new question : num1 {self.num1}, num2 {self.num2}, result {self.result}")

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
					self.create_message_box("Correct", self.gameDisplay)
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

		center_of_box_x = x_offset + rect.width/2

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
							[f"{self.num1} + {self.num2-10}", Colors.BLACK, rect.y+180, -1, center_of_box_x-10, -1],
							[f"|", Colors.BLACK, rect.y+180, -1, center_of_box_x, -1],
							[f"{self.num1-10} x {self.num2-10}", Colors.BLACK, rect.y+180, center_of_box_x+10, -1, -1],

							# [f"{self.num1 + self.num2-10} | {(self.num1-10) * (self.num2-10)}", Colors.BLACK, rect.y+220, -1, -1, 1],

							[f"{self.num1 + self.num2-10}", Colors.BLACK, rect.y+220, -1, center_of_box_x-10, -1],
							[f"|", Colors.BLACK, rect.y+220, -1, center_of_box_x, -1],
							[f"{(self.num1-10) * (self.num2-10)}", Colors.BLACK, rect.y+220, center_of_box_x+10, -1, -1],

							# Layer 3
							[f"{self.num1} x {self.num2} = {self.result}", Colors.BLACK, rect.y+260, -1, -1, 1],
						]

		## Encountering for "difference multiplication" having more than one digit.
		if ((self.num1-10) * (self.num2-10)) > 9:
			elements_list.pop()

			element_1_1 = [f"{self.num1+self.num2-10} + {int((self.num1-10)*(self.num2-10)/10)}", Colors.BLACK, rect.y+260, -1, center_of_box_x-10, -1]
			element_1_2 = [f"|", Colors.BLACK, rect.y+260, -1, center_of_box_x, -1]
			element_1_3 = [f"{((self.num1-10) * (self.num2-10))%10}", Colors.BLACK, rect.y+260, center_of_box_x+10, -1, -1]


			element_2_1 = [f"{self.num1+self.num2-10 + int((self.num1-10)*(self.num2-10)/10)}", Colors.BLACK, rect.y+300, -1, center_of_box_x-10, -1]
			element_2_2 = [f"|", Colors.BLACK, rect.y+300, -1, center_of_box_x, -1]
			element_2_3 = [f"{((self.num1-10) * (self.num2-10))%10}", Colors.BLACK, rect.y+300, center_of_box_x+10, -1, -1]

			element_3 = [f"{self.num1} x {self.num2} = {self.result}", Colors.BLACK, rect.y+340, -1, -1, 1]

			elements_list.append(element_1_1)
			elements_list.append(element_1_2)
			elements_list.append(element_1_3)
			elements_list.append(element_2_1)
			elements_list.append(element_2_2)
			elements_list.append(element_2_3)
			elements_list.append(element_3)

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

