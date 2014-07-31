# Imports
# ------------------------------------------------------------------------------
import libtcodpy as libtcod

# Classes
# ------------------------------------------------------------------------------


class LightSource:
    # Constructor
    # Takes the intensity of the light (how much it adds to the light level of
    # the tile it's on), the distance the light goes (in a radius), the length
    # of time in turns it lasts, with -1 being indefinite, and the color of the
    # light
    # Defaults to (5, 5, 200, )

    def __init__(self, intensity=5, distance=5, lifetime=200,
                 light_color=libtcod.white):
        self.intensity = intensity
        self.distance = distance
        self.lifetime = lifetime
        self.light_color = light_color
        self.light_map = None
        self.needs_remapping = True

    # Burn.
    # Simple function, reduces the lifetime of a lightsource
    # by the passed value.
    # Value defaults to 1.
    # if the lifetime is 0, it attempts to destroy the lightSource.
    # if the lifetime is -1, it simply returns.
    def burn(self, value):
        if self.lifetime == -1:
            return
        elif self.lifetime == 0:
            # Mark the lightsource for destruction.
            # then return
            return
        else:
            self.lifetime -= value

    # Setup function, gets called after this is composed onto the base actor
    # Contains the construction parts that would require the base actor.
    def setup(self):
        # import
        from engine import gEngine
        parent = self.parent
        gEngine.findLightingMap(
            parent.x, parent.y, self.distance, self.light_map)

    # Lighting calculation function. Gets called during the map drawing
    # phase to determine how to add the light source's light to the map.
    def calculate_lighting(self):
        # Figure out if the current FoV map around this light source needs
        # recalculating
        if self.needs_remapping:
            # Recalculate the array that holds the information of visibility
            # of tiles around this model.
            pass
        # For tiles around this light, calculate the color and intensity of the
        # light. Calculation is multiplication of the color of the tile's fore
        # ground and the light's color. Intensity is the multiplication of the
        # light and the tile's light intensity. If the tile is not in FoV to
        # the light, don't touch that tile.
        pass
