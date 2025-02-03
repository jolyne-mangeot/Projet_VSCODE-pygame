import pygame as pg
from control.states_control import States
from all_states.main_menu_states.main_menu_manager import Main_menu_manager

pg.font.init()

class Options(States, Main_menu_manager):
    def __init__(self):
        """
            states all navigation paths and options to create buttons for,
            as well as their placement on the screen
        """
        States.__init__(self)
        Main_menu_manager.__init__(self)
        self.next = "main_menu" # only for indication, changes based on chosen option
        self.before = "main_menu" # used for back button, never changes
        self.options = ["Music", "Sound", "Graphics", "Controls", "Main_menu"]
        self.next_list = ["options", "options", "options", "options", "main_menu"]
        self.pre_render_options()
        self.from_top = 60
        self.spacer = 60
    
    def cleanup(self):
        """
            cleans up all menu related data
        """
        pass

    def startup(self):
        """
            initiates all menu related data
        """
        pass

    def get_event(self, event):
        """
            get all events and checks for custom conditions for the active
            menu only
        """
        if event.type == pg.QUIT:
            self.quit = True
        self.get_event_menu(event)
    
    def update(self):
        """
            update the menu with all new informations such as hovering or
            selecting an option as well as playing a sound when happening,
            then launch draw method
        """
        self.update_menu()
        self.draw()
    
    def draw(self):
        """
            launch all display related scripts proper to this menu before
            the main_menu states shared scripts
        """
        self.screen.fill((255,0,0))
        self.draw_menu_options()