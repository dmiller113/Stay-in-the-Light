#Imports
#------------------------------------------------------------------------------
import constants as const
import libtcodpy as libtcod
from actor import Actor
import lightSource as light
from map import Tile, Map
import math

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
		self.curMap = Map()
		x = Actor(4,5)
		y = light.LightSource()
		x.addComponent(y)

	#Draw function
	#Takes nothing.
	#----------------------------------------------------------------------------
	def drawFrame(self):
		# Setup some offscreen consoles for each element of the UI (Map, status,
		# messages)
		mapConsole = libtcod.console_new(const.mapWidth, const.mapHeight)

		#Draw the map to screen
		self.curMap.draw(mapConsole)

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

	#Checks that the specified tile is a tile can be walked on.
	#Takes the x,y coord of the tile
	#Returns true if the tile is a valid tile, and could be walked on.
	#----------------------------------------------------------------------------
	def isTileWalkable(self, tileX, tileY):
		if( (tileY < const.mapHeight and tileY >= 0) and (tileX < const.mapWidth
		and tileX >= 0)):
			return not self.curMap.curMap[tileX][tileY].blocking

	#Finds the distance between two tiles.
	#Takes the x,y coords of two tiles, in (x1, y1, x2, y2) order
	#Returns the distance between the tiles
	#----------------------------------------------------------------------------
	def findDistance(self, tileX1, tileY1, tileX2, tileY2):
		distance = math.sqrt((tileX1 - tileX2)**2 + (tileY1 - tileY2)**2)
		return distance

	#Grabs a circular area of tiles based upon a center and a radius.
	#Takes the x,y coords of the center tile and the radius. Radius 1 returns
	#only the center tile.
	#Returns a list of tiles in the area
	#----------------------------------------------------------------------------
	def findArea(self, tileX, tileY, radius = 2):
		radius -= 1
		if( (tileX - radius < 0 or tileX + (radius + 1) >= const.mapWidth)
		or (tileY - radius < 0 or tileY + (radius + 1) >= const.mapHeight) ):
			return None
		returnList = []
		#This method is pretty bad for anything larger than radius 4
		for x in range( (tileX - radius), (tileX + (radius + 1)) ):
			for y in range( (tileY - radius), (tileY + (radius + 1)) ):
				if self.findDistance(tileX, tileY, x, y) <= radius:
					returnList.append(self.curMap.curMap[x][y])
		return returnList
	#Grabs a circular area of tiles based upon a center and a radius.
	#Takes the x,y coords of the center tile and the radius.
	#Sets the passed lightMap to the region made in the function
	#----------------------------------------------------------------------------
	def findLightingMap(self, centerX, centerY, radius = 2, lightMap = None):
		if lightMap is None:
			return
		curMap = self.curMap.curMap
		lightMap = libtcod.map_new(radius*2, radius*2)
		for x in range( (tileX - radius), (tileX + (radius + 1)) ):
			for y in range( (tileY - radius), (tileY + (radius + 1)) ):
				libtcod.map_set_properties(lightMap, x, y, curMap[x][y].transparent,
					(not curMap[x][y].blocking) )

gEngine = Engine()
