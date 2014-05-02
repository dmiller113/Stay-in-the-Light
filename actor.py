#Imports
#------------------------------------------------------------------------------
import libtcodpy as libtcod

#Classes
#------------------------------------------------------------------------------
class Actor:
	def __init__(self, x = 0, y = 0, symbol = '@', frontColor = libtcod.white,
		backColor = libtcod.black):
		self.x = x
		self.y = y
		self.symbol = symbol
		self.frontColor = frontColor
		self.backColor = backColor