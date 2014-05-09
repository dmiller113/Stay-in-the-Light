import libtcodpy as libtcod
import constants as const
from engine import gEngine

gameState = "playing"

# Sets up for the program
# -----------------------------------------------------------------------------
def programSetup():
	libtcod.console_set_custom_font(const.fontName,
		libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
	libtcod.sys_set_fps(const.fps)
	libtcod.console_init_root(const.consoleWidth, const.consoleHeight,
		'python/libtcod tutorial')
	libtcod.console_set_default_foreground(const.root, libtcod.white)
	libtcod.console_clear(const.root)
	gEngine.drawUILines()



# MAIN GAME LOOP FUNCTION
# -----------------------------------------------------------------------------
def gameLoop():
	while not libtcod.console_is_window_closed() and gameState != "gameDone":
		gEngine.drawFrame()
		key = libtcod.console_check_for_keypress(libtcod.KEY_PRESSED)
		handleInput(key)

# Player input handling (Temp, replaced once AI is implimented)
# -----------------------------------------------------------------------------
def handleInput(key):
	global gameState
	if key.vk != libtcod.KEY_NONE:
		if key.c == ord('4'):
			gEngine.player.x -= 1
		elif key.c == ord('6'):
			gEngine.player.x += 1
		elif key.c == ord('8'):
			gEngine.player.y -= 1
		elif key.c == ord('2'):
			gEngine.player.y += 1
		elif key.c == ord('q'):
			gameState = "gameDone"
	return
