#Imports
#------------------------------------------------------------------------------
import constants as const
import libtcodpy as libtcod
from actor import Actor

#Global
#------------------------------------------------------------------------------


#Classes
#------------------------------------------------------------------------------
class Engine:
	# Constructor
	# Takes nothing so far.
	#----------------------------------------------------------------------------
	def __init__(self):
		self.player = Actor(const.mapWidth/2, const.mapHeight/2)

	#Draw function
	# Takes nothing.
	#----------------------------------------------------------------------------
	def drawFrame(self):
		# Setup some offscreen consoles for each element of the UI (Map, status,
		# messages)
		mapConsole = libtcod.console_new(const.mapWidth, const.mapHeight)

		#Draw the actors to the mapConsole. Save the player for last.
		# draw dem actors.

		#Draw the player.
		self.player.draw(mapConsole)



		#Blit all the offscreen consoles to the root
		libtcod.console_blit(mapConsole, 0, 0, 0, 0, const.root, 1, 1)

		#Show dem changes
		libtcod.console_flush()

	#Draws the lines that border the UI.
	#Takes nothing
	#----------------------------------------------------------------------------
	def drawUILines(self):
		#The top and bottom border
		for x in range(const.consoleWidth):
			libtcod.console_put_char_ex(const.root, x, 0, libtcod.CHAR_HLINE, 
				libtcod.white, libtcod.black)
			libtcod.console_put_char_ex(const.root, x, const.consoleHeight-1, 
				libtcod.CHAR_HLINE, libtcod.white, libtcod.black)
			libtcod.console_put_char_ex(const.root, x, const.mapHeight+1, 
				libtcod.CHAR_HLINE, libtcod.white, libtcod.black)

		#The left and right border	
		for y in range(const.consoleHeight):
			libtcod.console_put_char_ex(const.root, 0, y, '|', 
				libtcod.white, libtcod.black)
			libtcod.console_put_char_ex(const.root, const.consoleWidth-1, y, '|', 
				libtcod.white, libtcod.black)
			if(y <= const.mapHeight and y > 0):
				libtcod.console_put_char_ex(const.root, const.mapWidth+1, y, '|', 
					libtcod.white, libtcod.black)

		#The corners
		libtcod.console_put_char_ex(const.root, const.consoleWidth-1, 
			const.consoleHeight-1, '#', libtcod.white, libtcod.black)		
		libtcod.console_put_char_ex(const.root, 0, 
			const.consoleHeight-1, '#', libtcod.white, libtcod.black)
		libtcod.console_put_char_ex(const.root, 0, 0, '#', libtcod.white, 
			libtcod.black)
		libtcod.console_put_char_ex(const.root, const.consoleWidth-1, 0, '#',
		 	libtcod.white, libtcod.black)

		libtcod.console_flush()

gEngine = Engine()