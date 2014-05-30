#Imports
#------------------------------------------------------------------------------
import engine

#Classes
#------------------------------------------------------------------------------
class LightSource:
  # Constructor
  # Takes the intensity of the light (how much it adds to the light level of
  # the tile it's on), the distance the light goes (in a radius), the length
  # of time in turns it lasts, with -1 being indefinite.
  # Defaults to (5, 5, 200)
  def __init__(self, intensity = 5, distance = 5, lifetime = 200):
    self.intensity = intensity
    self.distance = distance
    self.lifetime = lifetime

  # Burn.
  # Simple class, reduces the lifetime of a lightsource by the passed value.
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

