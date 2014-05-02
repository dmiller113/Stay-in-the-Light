#Imports
#------------------------------------------------------------------------------
import constants as const
from actor import Actor

#Global
#------------------------------------------------------------------------------


#Classes
#------------------------------------------------------------------------------
class Engine:
	def __init__(self):
		self.player = Actor(const.consoleWidth/2, const.consoleHeight/2) 

gEngine = Engine()