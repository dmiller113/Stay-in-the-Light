# Imports
# ------------------------------------------------------------------------------
import constants as const
import libtcodpy as libtcod
import sys
# Classes
# ------------------------------------------------------------------------------


class Tile:
    # Constructor.
    # Takes a symbol, fore color, background color, movement blocking, vision
    # blocking, a light source that's on that tile, and an optional type that
    # will fill the rest in for you if it matches the types of tiles declared
    # in the const module. ex: Tile('#', libtcod.white, libtcod.black, true,
    # false)

    def __init__(self, symbol, foreColor, backColor, blocking, transparent,
                 seen=False, setType=False):
        if not setType:
            self.symbol = symbol
            self.foreColor = foreColor
            self.backColor = backColor
            self.blocking = blocking
            self.transparent = transparent
            self.seen = seen
            self.light_level = 0.5
            self.light_list = 0
        else:
            print setType

    # Draw function. Puts the symbol on the screen at the x,y position using
    # its fore and back colors.
    # Takes a libtcod console on which to draw on.
    # -------------------------------------------------------------------------
    def draw(self, console, x, y):
        libtcod.console_put_char_ex(
            console, x, y, self.symbol, self.foreColor * self.light_level,
            self.backColor)


class Map:
    # Constructor
    # takes a seed to stick in the random generator
    # -------------------------------------------------------------------------

    def __init__(self, randSeed=const.debugRandomSeed):
        self.randSeed = randSeed
        self.createMap(self.randSeed)

    # Draw function. Calls the draw function of each tile in the current map.
    # Takes a libtcod console to draw on
    # -------------------------------------------------------------------------
    def draw(self, console):
        for y in range(const.mapHeight):
            for x in range(const.mapWidth):
                self.curMap[x][y].draw(console, x, y)

    # Map creation function. Calls the debug map creation if the randomSeed is
    # equal to the debug value.
    # Takes a randomSeed to base the random number generator on.
    # -------------------------------------------------------------------------
    def createMap(self, randSeed):
        if randSeed == const.debugRandomSeed:
            self.debugMap()

    # Debug map creation function. Creates a blank room with various objects to
    # test various functions, abilities, and effects.
    # Takes nothing.
    # -------------------------------------------------------------------------
    def debugMap(self):
        self.curMap = [
            [Tile('.', libtcod.white, libtcod.black, False, True) for
                y in range(const.mapHeight)] for x in range(const.mapWidth)]
        for x in range(const.mapWidth):
            self.curMap[x][0].symbol = '#'
            self.curMap[x][0].blocking = True
            self.curMap[x][0].transparent = False
            self.curMap[x][const.mapHeight - 1].symbol = '#'
            self.curMap[x][const.mapHeight - 1].blocking = True
            self.curMap[x][const.mapHeight - 1].transparent = False
        for y in range(const.mapHeight):
            self.curMap[0][y].symbol = '#'
            self.curMap[0][y].blocking = True
            self.curMap[0][y].transparent = False
            self.curMap[const.mapWidth - 1][y].symbol = '#'
            self.curMap[const.mapWidth - 1][y].blocking = True
            self.curMap[const.mapWidth - 1][y].transparent = False
        self.curMap[21][29].symbol = '#'
        self.curMap[21][29].blocking = True
        self.curMap[21][29].transparent = False
