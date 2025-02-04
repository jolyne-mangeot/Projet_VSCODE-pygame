import pygame as pg
from control.states_control import States
from all_states.main_menu_states.main_menu_manager import Main_menu_manager

pg.font.init()

class Main_menu(States, Main_menu_manager):
    def __init__(self):
        """
            inits values specific to the menu such as navigation and
            placement of options
        """
        States.__init__(self)
        Main_menu_manager.__init__(self)
        self.next = "game"
        self.options = ["Play", "Options", "Quit"]
        self.next_list = ["game", "options"]
        self.pre_render_options()
        self.from_top = 200
        self.spacer = 75
    
    def cleanup(self):
        """
            cleans up all menu related data
        """
        pass

    def startup(self):
        """
            initiates all menu-related data
        """
        pass

    def get_event(self, event):
        """
            get all pygame-related events proper to the menu before
            checking main menu shared events
        """
        if event.type == pg.QUIT:
            self.quit = True
        if event.type == pg.KEYDOWN:
            if event.key in [pg.K_ESCAPE, pg.K_LSHIFT]:
                self.quit = True
        self.get_event_menu(event)
    
    def update(self):
        """
            trigger all changes such as mouse hover or changing selected
            option, done after having checked in control class change on
            done and quit attribute from menu_manager inheritance
        """
        self.update_menu()
        self.draw()
    
    def draw(self):
        """
            init all display related script
        """
        self.screen.fill((255,0,0))
        self.draw_menu_options()