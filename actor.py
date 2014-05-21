#Imports
#------------------------------------------------------------------------------
import libtcodpy as libtcod

#Classes
#------------------------------------------------------------------------------
class Actor:
	# Constructor
	# Takes an x,y position with 0,0 being upper left corner; a single character,
	# which is the symbolic representation of the actor; and the fore and back
	# colors used to draw it.
	#----------------------------------------------------------------------------
	def __init__(self, x = 0, y = 0, symbol = '@', frontColor = libtcod.white,
		backColor = libtcod.black):
		self.x = x
		self.y = y
		self.symbol = symbol
		self.frontColor = frontColor
		self.backColor = backColor

	# Draw function. Puts the symbol on the screen at its x,y position using
	# its fore and back colors.
	# Takes a libtcod console on which to draw on.
	#----------------------------------------------------------------------------
	def draw(self, console):
		libtcod.console_put_char_ex(console, self.x, self.y, self.symbol,
			self.frontColor, self.backColor)

	# Movement function. Checks for nothing with X,Y so avoid passing bad values.
	# Takes the new position of the Actor
	def move(self, x, y):
		self.x = x
		self.y = y
