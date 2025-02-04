import pygame as pg
from control.control import Control
from all_states.main_menu_states.main_menu import Main_menu
from all_states.main_menu_states.options_menu import Options
from all_states.in_game_states.in_game import Game
from all_states.in_game_states.pause_menu import Pause_menu

STATE_DICT = {
    'main_menu' : Main_menu(),
    'options' : Options(),
    'game' : Game(),
    'pause_menu' : Pause_menu()
}

pg.init()

game = Control()
game.setup_states(STATE_DICT, "main_menu")

game.main_game_loop()
pg.quit()
exit()