import random, pygame, sys
from pygame.locals import *
from random import randint

class Dicey():

	def __init__(self):

		global rando, mousex, mousey, DISPLAYSURF, clock, hover, mouseClicked, text, font, rando, DARK_GREEN, GOX, GOY, GO1_BUTTON, GO2_BUTTON, BOXRECT, ICON_100, ICON_DICE, ICON_COIN, ICON_100_H, ICON_DICE_H, ICON_COIN_H, ICON_100_X, ICON_100_Y, ICON_DICE_X, ICON_DICE_Y, ICON_COIN_X, ICON_COIN_Y, ICON_100_HOVER, ICON_DICE_HOVER, ICON_COIN_HOVER, RECT_100, RECT_COIN, RECT_DICE, current_mode

		pygame.init()

		mousex = 0 # used to store x coordinate of mouse event
		mousey = 0 # used to store y coordinate of mouse event

		DISPLAYSURF = pygame.display.set_mode((400, 300))
		clock = pygame.time.Clock()
		pygame.display.set_caption('Dicey')

		self.rando = 6

		self.font = pygame.font.Font(None, 200)
		self.text = self.font.render(str(self.rando), True, (0, 128, 0))

		self.hover = False
		self.mouseClicked = False

		DARK_GREEN = (0, 51, 25)

		###
		#GO BUTTON STUFFS
		GOX = 175
		GOY = 250

		GO1_BUTTON = pygame.image.load('pictures/go.png')
		GO2_BUTTON = pygame.image.load('pictures/go2.png')
		BOXRECT = pygame.Rect(GOX, GOY, 50, 50)

		###
		self.current_mode = "dice"


		###
		#100 icon stuff
		if self.current_mode == "100":
			ICON_100_X = 0
			ICON_100_Y = 265
		else:
			ICON_100_X = 0
			ICON_100_Y = 275

		ICON_100 = pygame.image.load('pictures/100_icon_on.png')
		ICON_100_H = pygame.image.load('pictures/100_icon_on_highlight.png')

		self.ICON_100_HOVER = False

		RECT_100 = pygame.Rect(ICON_100_X, ICON_100_Y, 25, 35)


		###
		#dice icon stuff
		if self.current_mode == "dice":
			ICON_DICE_X = 26
			ICON_DICE_Y = 265
		else:
			ICON_DICE_X = 26
			ICON_DICE_Y = 275

		ICON_DICE = pygame.image.load('pictures/dice_icon_on.png')
		ICON_DICE_H = pygame.image.load('pictures/dice_icon_on_highlight.png')

		self.ICON_DICE_HOVER = False

		RECT_DICE = pygame.Rect(ICON_DICE_X, ICON_DICE_Y, 25, 35)


		###
		#coin icon stuff
		if self.current_mode == "coin":
			ICON_COIN_X = 52
			ICON_COIN_Y = 265
		else:
			ICON_COIN_X = 52
			ICON_COIN_Y = 275

		ICON_COIN = pygame.image.load('pictures/coin_icon_on.png')	
		ICON_COIN_H = pygame.image.load('pictures/coin_icon_on_highlight.png')

		self.ICON_COIN_HOVER = False

		RECT_COIN = pygame.Rect(ICON_COIN_X, ICON_COIN_Y, 25, 35)


	def main(self):

		while True:
			self.mouseClicked = False 

			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()
				elif event.type == MOUSEMOTION:
					mousex, mousey = event.pos
				elif event.type == MOUSEBUTTONUP:
					mousex, mousey = event.pos
					self.mouseClicked = True

			self.hover = False
			if BOXRECT.collidepoint(mousex, mousey):
				self.hover = True

			if (self.hover == True) and (self.mouseClicked == True):
				if self.current_mode == "dice":
					self.rando = randint(1,6)
					self.text = self.font.render(str(self.rando), True, (0, 128, 0))
				if self.current_mode == "100":
					self.rando = randint(1,100)
					self.text = self.font.render(str(self.rando), True, (0, 128, 0))
				if self.current_mode == "coin":
					self.rando = randint(1,2)
					if self.rando == 1:
						self.text = self.font.render("H", True, (0, 128, 0))
					else:
						self.text = self.font.render("T", True, (0, 128, 0))




			self.ICON_100_HOVER = False
			if RECT_100.collidepoint(mousex, mousey):
				self.ICON_100_HOVER = True

			if (self.ICON_100_HOVER == True) and (self.mouseClicked == True):
				self.current_mode = "100"


			self.ICON_DICE_HOVER = False
			if RECT_DICE.collidepoint(mousex, mousey):
				self.ICON_DICE_HOVER = True

			if (self.ICON_DICE_HOVER == True) and (self.mouseClicked == True):
				self.current_mode = "dice"


			self.ICON_COIN_HOVER = False
			if RECT_COIN.collidepoint(mousex, mousey):
				self.ICON_COIN_HOVER = True

			if (self.ICON_COIN_HOVER == True) and (self.mouseClicked == True):
				self.current_mode = "coin"

			self.draw()



	def draw(self):


		#background-color
		DISPLAYSURF.fill((204, 255, 204))   

		#menu background
		pygame.draw.rect(DISPLAYSURF, DARK_GREEN, pygame.Rect(0, 250, 400, 50))

		#roll
		DISPLAYSURF.blit(self.text,(160 , 60))

		#checking to see if it should play the roll animation
		if (self.hover == True) and (self.mouseClicked == True):
			self.roll_animation()


		#checking if which go icon to use.	
		self.menu_hover()

		pygame.display.update()
		clock.tick(30)



	def roll_animation(self):

		count = 6
		while count >= 0:
			DISPLAYSURF.fill((204, 255, 204)) 
			textx = self.font.render(str(count), True, (0, 128, 0))
			DISPLAYSURF.blit(textx,(160 , 60))
			pygame.draw.rect(DISPLAYSURF, DARK_GREEN, pygame.Rect(0, 250, 400, 50))
			DISPLAYSURF.blit(GO2_BUTTON, (GOX, GOY))
			self.menu_hover()
			count -=1
			pygame.display.update()
			clock.tick(30)


	def menu_hover(self):

		if self.current_mode == "100":
			ICON_100_X = 0
			ICON_100_Y = 265
		else:
			ICON_100_X = 0
			ICON_100_Y = 275

		if self.current_mode == "coin":
			ICON_COIN_X = 52
			ICON_COIN_Y = 265
		else:
			ICON_COIN_X = 52
			ICON_COIN_Y = 275

		if self.current_mode == "dice":
			ICON_DICE_X = 26
			ICON_DICE_Y = 265
		else:
			ICON_DICE_X = 26
			ICON_DICE_Y = 275



		if self.hover:
			DISPLAYSURF.blit(GO2_BUTTON, (GOX, GOY))
		else:
			DISPLAYSURF.blit(GO1_BUTTON, (GOX, GOY))
		
		if self.ICON_100_HOVER or self.current_mode == "100":
			DISPLAYSURF.blit(ICON_100_H, (ICON_100_X, ICON_100_Y))
		else:
			DISPLAYSURF.blit(ICON_100, (ICON_100_X, ICON_100_Y))

		if self.ICON_COIN_HOVER or self.current_mode == "coin":
			DISPLAYSURF.blit(ICON_COIN_H, (ICON_COIN_X, ICON_COIN_Y))
		else:
			DISPLAYSURF.blit(ICON_COIN, (ICON_COIN_X, ICON_COIN_Y))

		if self.ICON_DICE_HOVER or self.current_mode == "dice":
			DISPLAYSURF.blit(ICON_DICE_H, (ICON_DICE_X, ICON_DICE_Y))
		else:
			DISPLAYSURF.blit(ICON_DICE, (ICON_DICE_X, ICON_DICE_Y))

	def check_mode(self):
		if self.current_mode == "100":
			ICON_100_X = 0
			ICON_100_Y = 265
		else:
			ICON_100_X = 0
			ICON_100_Y = 275

		if self.current_mode == "dice":
			ICON_DICE_X = 26
			ICON_DICE_Y = 265
		else:
			ICON_DICE_X = 26
			ICON_DICE_Y = 275

		if self.current_mode == "coin":
			ICON_COIN_X = 52
			ICON_COIN_Y = 265
		else:
			ICON_COIN_X = 52
			ICON_COIN_Y = 275



d = Dicey()
d.main()