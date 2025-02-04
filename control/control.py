import pygame as pg
import json
from assets.__game_settings__ import CONTROL_SETTINGS_PATH

class Control:
    def __init__(self):
        """
            load game settings and init essential data related to Pygame
        """
        settings = self.load_settings()
        self.__dict__.update(**settings['settings'])
        self.done = False
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
    
    def load_settings(self):
        """
            load settings from json file with set path
        """
        with open(CONTROL_SETTINGS_PATH, "r") as file:
            settings = json.load(file)
        return settings
    
    def setup_states(self, STATE_DICT, start_state):
        """
            recover state dictionary and initialize first state
            based on given parameters ("main_menu" and such)
        """
        self.state_dict = STATE_DICT
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]
    
    def flip_state(self):
        """
            make all necessary changes to attributes to cleanup a state
            and startup another based on next segment set in events such
            as select_option whenever state attribute done is True
            - also save in previous attribute the ended state for
            script sake
        """
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous
    
    def update(self):
        """
            check for state done status to either quit the script loop
            or initialize a new state with flip_state
        """
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update()
    
    def event_loop(self):
        """
            main loop for pygame events which initializes the current state's
            event loop as well
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.state.get_event(event)
    
    def main_game_loop(self):
        """
            access all essential methods to run game loop based on clock ticks
            with event_loop, which launches on the control class scope before
            the current state one, update for each class level as well before
            updating the pygame display
        """
        while not self.done:
            self.delta_time = self.clock.tick(self.fps)/1000
            self.event_loop()
            self.update()
            pg.display.update()