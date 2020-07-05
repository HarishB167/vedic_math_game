import pygame

import time
import random

pygame.init()

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

class Colors:

	DARK_BLUE = (0, 0, 100)
	DARK_GREEN = (0, 100, 0)
	DARK_RED = (176, 63, 55)
	BLACK = (0,0,0)

## Reference for this code.
## https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame
class InputBox:

	def __init__(self, x, y, w, h, result, screen, active=False, text=''):
		self.result = result
		self.screen = screen
		self.rect = pygame.Rect(x, y, w, h)
		self.text = text
		self.active = active
		self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
		self.txt_surface = FONT.render(text, True, self.color)

	def handle_event(self, event):
		result = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			# If the user clicked on the input_box rect.
			if self.rect.collidepoint(event.pos):
				# Toggle the active variable.
				self.active = not self.active
			else:
				self.active = False
			# Change the current color of the input box.
			self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
		if event.type == pygame.KEYDOWN:
			if self.active:
				if event.key == pygame.K_RETURN:
					print(self.text)
					
					self.text = ''
				elif event.key == pygame.K_BACKSPACE:
					self.text = self.text[:-1]
				else:
					self.text += event.unicode

				# Re-render the text.
				self.txt_surface = FONT.render(self.text, True, self.color)
				self.update()
				self.draw(self.screen)

				# check if text entered is result
				try:
					val = int(self.text)

					if val == self.result:
						print("Correct.")
						return True
				except ValueError:
					pass

		return result

	def update(self):
		# Resize the box if the text is too long.
		width = max(50, self.txt_surface.get_width()+10)
		self.rect.w = width

	def draw(self, screen):
		# Blit the text.
		screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
		# Blit the rect.
		pygame.draw.rect(screen, self.color, self.rect, 2)


class Button:
	
	# ic - inactive color
	# ac - active color
	def __init__(self, msg, x, y, w, h, ic, ac, action=None):

		self.msg = msg
		self.x = x
		self.y = y
		self.width = w
		self.height = h
		self.ic = ic
		self.ac = ac
		self.action = action

		self.current_color = self.ic


	def handle_event(self, event):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if self.x+self.w > mouse[0] > self.x and self.y+self.h > mouse[1] > self.y:
			self.current_color = self.ac
			if click[0] == 1 and self.action != None:
				self.action()
		else:
			self.current_color = self.ic

	def update(self):
		pass

	def text_objects(self, text, font):
		textSurface = font.render(text, True, black)
		return textSurface, textSurface.get_rect()

	def draw(self, screen):
		pygame.draw.rect(screen, self.current_color, (self.x,self.y,self.w,self.h))

		smallText = pygame.font.Font("freesansbold.ttf",20)
		textSurf, textRect = self.text_objects(msg, smallText)
		textRect.center = ( (self.x+(self.w/2)), (self.y+(self.h/2)) )
		screen.blit(textSurf, textRect)


class MessageBox:

	def __init__(self, msg, center, size, ok_func=None, cancel_func=None):
		self.msg = msg
		self.center = center
		self.size = size
		self.ok_func = ok_func
		self.cancel_func = cancel_func

	def show(self, screen):

		x_pos = self.center[0] - self.size[0]/2
		y_pos = self.center[1] - self.size[1]/2

		txt_surface = FONT.render(self.msg, True, (0,0,0))

		txt_w = txt_surface.get_width()

		txt_x_pos = self.size[0]/2 - txt_w/2
		txt_y_pos = 0.2 * self.size[1]/2

		rect = pygame.Rect(x_pos, y_pos, self.size[0], self.size[1])
		rect2 = pygame.Rect(x_pos+1, y_pos+1, self.size[0]-2, self.size[1]-2)

		# print(f"x_pos {x_pos}, y_pos {y_pos}, width {self.size[0]}, height {self.size[1]}")
		pygame.draw.rect(screen, (0,100,0), rect, 2)
		pygame.draw.rect(screen, (100,255,100), rect2)
		screen.blit(txt_surface, (rect.x+txt_x_pos, rect.y+txt_y_pos))
		

class Level:

	timeout_time = 10

	def __init__(self, gameDisplay, clock):
		self.gameDisplay = gameDisplay
		self.clock = clock

		self.backgroundImg = pygame.image.load('images/background_2.png')
		self.back_img = pygame.image.load('images/back_icon.png')
		self.back_img_hovered = pygame.image.load('images/back_icon_hovered.png')

		self.illustration_button_img = pygame.image.load('images/button_illustration.png')
		self.illustration_button_img_hovered = pygame.image.load('images/button_illustration_hovered.png')

		## Play button
		self.play_button = pygame.image.load('images/button_play_2.png')
		self.play_button_hovered = pygame.image.load('images/button_play_2_hovered.png')

		self.back_pressed = False

	def generate_numbers(self):
		self.num1 = random.randrange(11,20)
		self.num2 = random.randrange(11,20)

		print(f"Num 1 : {self.num1}, Num 2 : {self.num2}")
		return self.num1, self.num2

	def back_press(self):
		self.back_pressed = True
		time.sleep(0.2)

	def quitgame(self):
		pygame.quit()
		quit()

	def get_font(self, size):
		return pygame.font.Font("freesansbold.ttf", size)


	def text_objects(self, text, font):
		textSurface = font.render(text, True, Colors.BLACK)
		return textSurface, textSurface.get_rect()

	def message_display(self, text):
		largeText = pygame.font.Font('freesansbold.ttf',32)
		TextSurf, TextRect = self.text_objects(text, largeText)
		TextRect.center = ((self.display_width/2),(self.display_height/4))
		self.gameDisplay.blit(TextSurf, TextRect)

		pygame.display.update()

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
		return True if (self.counting_seconds < self.timeout_time) else False

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

	def create_message_box(self, msg, screen):

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

		time.sleep(0.5)