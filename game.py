import libtcodpy as libtcod
import constants as const
import engine

gameState = "playing"

# Sets up for the program
# -----------------------------------------------------------------------------
def programSetup():
	libtcod.console_set_custom_font(const.fontName, 
		libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
	libtcod.sys_set_fps(const.fps)
	libtcod.console_init_root(const.consoleWidth, const.consoleHeight, 
		'python/libtcod tutorial')


# MAIN GAME LOOP FUNCTION
# -----------------------------------------------------------------------------
def gameLoop():
	while not libtcod.console_is_window_closed() and gameState != "gameDone":
		libtcod.console_set_default_foreground(const.root, libtcod.white)
		libtcod.console_clear(const.root)
		libtcod.console_put_char(const.root, engine.player_x, engine.player_y, '@',
			libtcod.BKGND_NONE)
		libtcod.console_flush()
		key = libtcod.console_check_for_keypress(libtcod.KEY_PRESSED)
		handleInput(key)

# Player input handling (Temp, replaced once AI is implimented)
# -----------------------------------------------------------------------------
def handleInput(key):
	global gameState
	if key.vk != libtcod.KEY_NONE:
		if key.c == ord('4'):
			engine.player_x -= 1
		elif key.c == ord('6'):
			engine.player_x += 1
		elif key.c == ord('8'):
			engine.player_y -= 1
		elif key.c == ord('2'):
			engine.player_y += 1
		elif key.c == ord('q'):
			gameState = "gameDone"
	return