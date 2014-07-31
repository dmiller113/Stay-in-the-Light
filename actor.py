# Imports
# ------------------------------------------------------------------------------
import libtcodpy as libtcod

# Classes
# ------------------------------------------------------------------------------


class Actor:
    # Constructor
    # Takes an x,y position with 0,0 being upper left corner; a single
    # character which is the symbolic representation of the actor; and the
    # fore and back colors used to draw it.
    # -------------------------------------------------------------------------

    def __init__(self, x=0, y=0, symbol='@', frontColor=libtcod.white,
                 backColor=libtcod.black, visible=True):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.frontColor = frontColor
        self.backColor = backColor
        self.parts = {"LightSource": None}
        self.visible = visible

    # Draw function. Puts the symbol on the screen at its x,y position using
    # its fore and back colors.
    # Takes a libtcod console on which to draw on.
    # -------------------------------------------------------------------------
    def draw(self, console):
        if self.visible:
            libtcod.console_put_char_ex(console, self.x, self.y, self.symbol,
                                        self.frontColor, self.backColor)

    # Movement function. Checks for nothing with X,Y so avoid passing
    # bad values.
    # Takes the new position of the Actor
    def move(self, x, y):
        self.x = x
        self.y = y

    # Add component function.
    # Checks that the passed object isn't none, and then sets the object.parent
    # back to this object, then calls the objects setup so it can construct
    # things that it needs the parent actor for.
    # Takes an object to compose onto the actor
    def addComponent(self, composeObject):
        if composeObject is None:
            return
        className = composeObject.__class__.__name__
        if className in self.parts:
            self.parts[className] = composeObject
            composeObject.parent = self
            composeObject.setup()

    # Register Actor function.
    # Adds the actor into the engine's actor list.
    # Takes nothing
    def register(self):
        # Need to import engine.
        from engine import gEngine
        # Add to the actor's list
        gEngine.actors.append(self)
        # Set our id to the newest ID
        self.ID_ = gEngine.actor_counter
        # Increment the available ID
        gEngine.actor_counter += 1
