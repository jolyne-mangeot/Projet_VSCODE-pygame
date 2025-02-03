import pygame as pg
import json
from assets.__game_settings__ import CONTROL_SETTINGS_PATH

class Control:
    def __init__(self):
        with open(CONTROL_SETTINGS_PATH, "r") as file:
            settings = json.load(file)
        self.__dict__.update(**settings['settings'])
        self.done = False
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
    
    def setup_states(self, STATE_DICT, start_state):
        self.state_dict = STATE_DICT
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]
    
    def flip_state(self):
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous
    
    def update(self):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update()
    
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.state.get_event(event)
    
    def main_game_loop(self):
        while not self.done:
            self.delta_time = self.clock.tick(self.fps)/1000
            self.event_loop()
            self.update()
            pg.display.update()