import pygame

import time

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
		width = max(200, self.txt_surface.get_width()+10)
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

		# print(f"x_pos {x_pos}, y_pos {y_pos}, width {self.size[0]}, height {self.size[1]}")
		screen.blit(txt_surface, (rect.x+txt_x_pos, rect.y+txt_y_pos))
		pygame.draw.rect(screen, (0,100,0), rect, 2)
		

