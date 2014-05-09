#Imports
#------------------------------------------------------------------------------
import constants as const
import libtcodpy as libtcod
import sys
#Classes
#------------------------------------------------------------------------------
class Tile:
  #Constructor.
  #Takes a symbol, fore color, background color, movement blocking, vision
  # blocking, a light source that's on that tile, and an optional type that
  # will fill the rest in for you if it matches the types of tiles declared in
  # the const module. ex: Tile('#', libtcod.white, libtcod.black, true, false)
  def __init__(self, symbol, foreColor, backColor, blocking, transparent,\
    seen = False, setType = False):
    if not setType:
      self.symbol = symbol
      self.foreColor = foreColor
      self.backColor = backColor
      self.blocking = blocking
      self.transparent = transparent
      self.seen = seen
    else:
      print setType

  # Draw function. Puts the symbol on the screen at the x,y position using
  # its fore and back colors.
  # Takes a libtcod console on which to draw on.
  #----------------------------------------------------------------------------
  def draw(self, console, x, y):
    libtcod.console_put_char_ex(console, x, y, self.symbol,
      self.foreColor, self.backColor)

class Map:
  #Constructor
  #takes a seed to stick in the random generator
  #----------------------------------------------------------------------------
  def __init__(self, randSeed = 113113113):
    self.randSeed = randSeed
    self.curMap = [[Tile('#', libtcod.white, libtcod.black, True, False) for
      y in range(const.mapHeight)] for x in range(const.mapWidth)]

  # Draw function. Calls the draw function of each tile in the current map.
  # Takes a libtcod console to draw on
  #----------------------------------------------------------------------------
  def draw(self, console):
    for y in range(const.mapHeight):
      for x in range(const.mapWidth):
        self.curMap[x][y].draw(console)

