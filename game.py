import libtcodpy as libtcod
import constants as const
from engine import gEngine

gameState = "playing"
playerState = "idle"

# Sets up for the program
# -----------------------------------------------------------------------------
def programSetup():
	libtcod.console_set_custom_font(const.fontName,
		libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
	libtcod.sys_set_fps(const.fps)
	libtcod.console_init_root(const.consoleWidth, const.consoleHeight,
		'Stay in the Light')
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

def funkyLight():
	tiles = gEngine.findArea(22,30,5)
	for tile in tiles:
		tile.foreColor = libtcod.orange
		tile.backColor = libtcod.blue

# Player input handling (Temp, replaced once AI is implimented)
# -----------------------------------------------------------------------------
def handleInput(key):
	global gameState
	global playerState
	if key.vk != libtcod.KEY_NONE:
		cx = 0
		cy = 0
		if key.c == ord('4'):
			cx -= 1
			playerState = "moving"
		elif key.c == ord('6'):
			cx += 1
			playerState = "moving"
		elif key.c == ord('8'):
			cy -= 1
			playerState = "moving"
		elif key.c == ord('2'):
			cy += 1
			playerState = "moving"
		elif key.c == ord('5'):
			playerState = "moving"
		elif key.c == ord('q'):
			gameState = "gameDone"
		elif key.c == ord('l'):
			funkyLight()
		if(playerState == "moving"):
			if( gEngine.isTileWalkable(cx + gEngine.player.x, cy + gEngine.player.y) ):
				playerState = "moved"
				gEngine.player.move(cx + gEngine.player.x, cy + gEngine.player.y)
			else:
				playerState = "idle"
	return
