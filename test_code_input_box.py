import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)


class InputBox:

	def __init__(self, x, y, w, h, text=''):
		self.rect = pg.Rect(x, y, w, h)
		self.color = COLOR_INACTIVE
		self.text = text
		self.txt_surface = FONT.render(text, True, self.color)
		self.active = False

	def handle_event(self, event):
		if event.type == pg.MOUSEBUTTONDOWN:
			# If the user clicked on the input_box rect.
			if self.rect.collidepoint(event.pos):
				# Toggle the active variable.
				self.active = not self.active
			else:
				self.active = False
			# Change the current color of the input box.
			self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
		if event.type == pg.KEYDOWN:
			if self.active:
				if event.key == pg.K_RETURN:
					print(self.text)
					self.text = ''
				elif event.key == pg.K_BACKSPACE:
					self.text = self.text[:-1]
				else:
					self.text += event.unicode
				# Re-render the text.
				self.txt_surface = FONT.render(self.text, True, self.color)

	def update(self):
		# Resize the box if the text is too long.
		width = max(200, self.txt_surface.get_width()+10)
		self.rect.w = width

	def draw(self, screen):
		# Blit the text.
		screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
		# Blit the rect.
		pg.draw.rect(screen, self.color, self.rect, 2)



def main():
	clock = pg.time.Clock()
	input_box1 = InputBox(100, 100, 140, 32)
	input_box2 = InputBox(100, 300, 140, 32)
	input_boxes = [input_box1, input_box2]
	done = False

	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				done = True
			for box in input_boxes:
				box.handle_event(event)

		for box in input_boxes:
			box.update()

		screen.fill((30, 30, 30))
		for box in input_boxes:
			box.draw(screen)

		pg.display.flip()
		clock.tick(30)

def handle_event(event, rect, active, color, text, txt_surface):

	if event.type == pg.MOUSEBUTTONDOWN:
		# If the user clicked on the input_box rect.
		if rect.collidepoint(event.pos):
			# Toggle the active variable.
			active = not active
		else:
			active = False
		# Change the current color of the input box.
		color = COLOR_ACTIVE if active else COLOR_INACTIVE
	if event.type == pg.KEYDOWN:
		if active:
			if event.key == pg.K_RETURN:
				print(text)
				text = ''
			elif event.key == pg.K_BACKSPACE:
				text = text[:-1]
			else:
				text += event.unicode
			# Re-render the text.
			txt_surface = FONT.render(text, True, color)

	return active, color, text, txt_surface


def update(txt_surface, rect):
	# Resize the box if the text is too long.
	width = max(200, txt_surface.get_width()+10)
	rect.w = width

	return rect

def draw(screen, txt_surface, rect, color):
	# Blit the text.
	screen.blit(txt_surface, (rect.x+5, rect.y+5))
	# Blit the rect.
	pg.draw.rect(screen, color, rect, 2)

def main2():
	clock = pg.time.Clock()

	rect = pg.Rect(100, 100, 140, 32)
	color = COLOR_INACTIVE
	text = ''
	txt_surface = FONT.render(text, True, color)
	active = False


	done = False

	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				done = True

			active, color, text, txt_surface = handle_event(event, rect, active, color, text, txt_surface)

		rect = update(txt_surface, rect)

		screen.fill((30, 30, 30))
		draw(screen, txt_surface, rect, color)

		pg.display.flip()
		clock.tick(30)

## TODO:
# Know about these functions
#
# rect.collidepoint(event.pos)
# Returns true if the given point is inside the rectangle

# FONT.render(text, True, color)
# draw text on a new Surface

# txt_surface.get_width()
# Getting width of Surface (object)

# pg.draw.rect(screen, color, rect, 2)
# Draws a rectangle on the given surface.
# https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect

# pg.Rect(100, 100, 140, 32)
# pygame object for storing rectangular coordinates

# FONT.render(text, True, color)
# draw text on a new Surface

if __name__ == '__main__':
	main2()
	pg.quit()