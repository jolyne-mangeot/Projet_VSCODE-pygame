import pygame as pg

class Main_menu_manager:
    def __init__(self):
        """
            inits selected option, last option to check for on-same-button
            mouse-hover, and misc. values like font color. for all main_menu
            derived classes
        """
        self.selected_index = 0
        self.last_option = None
        self.selected_color = (255,255,0)
        self.deselected_color = (255,255,255)
    
    def draw_menu_options(self):
        """
            for all main_menu states, enumerate buttons and places them before
            checking for selected index button to place it on the same position
        """
        for index, option in enumerate(self.rendered["deselected"]):
            option[1].center = (self.screen_rect.centerx, self.from_top + index*self.spacer)
            if index == self.selected_index:
                selected_render = self.rendered["selected"][index]
                selected_render[1].center = option[1].center
                self.screen.blit(selected_render[0], selected_render[1])
            else:
                self.screen.blit(option[0],option[1])
    
    def update_menu(self):
        """
            update_menu checks for all changes keyboard or mouse
            related
        """
        self.mouse_hover_sound()
        self.change_selected_option()
    
    def get_event_menu(self, event):
        """
            get all events for Main_menu states from the main_game_loop
            in Control. is done after individual get_event from active menu
        """
        if event.type == pg.KEYDOWN:
            if event.key in [pg.K_ESCAPE, pg.K_LSHIFT] and not self.quit:
                self.next = self.before
                self.done = True
            elif event.key in [pg.K_UP, pg.K_z]:
                self.change_selected_option(-1)
            elif event.key in [pg.K_DOWN, pg.K_s]:
                self.change_selected_option(1)
            
            elif event.key in [pg.K_RETURN]:
                self.select_option(self.selected_index)
        self.mouse_menu_click(event)
    
    def mouse_hover_sound(self):
        """
            reinstate a check loop for all buttons to trigger a set behaviour
            like sound but also checks if hovered button is the same as before
        """
        for index, option in enumerate(self.rendered["deselected"]):
            if option[1].collidepoint(pg.mouse.get_pos()):
                if self.last_option != option:
                    self.last_option = option
    
    def mouse_menu_click(self, event):
        """
            after all keyboard related get_event's, launch a check loop
            for mouse behaviour to select an option
        """
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            for index, option in enumerate(self.rendered["deselected"]):
                if option[1].collidepoint(pg.mouse.get_pos()):
                    self.selected_index = index
                    self.select_option(index)
                    break
    
    def pre_render_options(self):
        """
            Selects a font and pre-renders it regardless of hovered / selected
            option. all for display
        """
        font_selected = pg.font.SysFont("arial", 40)
        font_deselected = pg.font.SysFont("arial", 40)

        rendered_msg = {"deselected":[], "selected":[]}
        for option in self.options:
            deselected_render = font_deselected.render(option, 1 , self.deselected_color)
            deselected_rect = deselected_render.get_rect()
            selected_render = font_selected.render(option, 1 , self.selected_color)
            selected_rect = selected_render.get_rect()
            rendered_msg["deselected"].append((deselected_render, deselected_rect))
            rendered_msg["selected"].append((selected_render, selected_rect))
        self.rendered = rendered_msg
    
    def select_option(self, index):
        """
            change the active state with done attribute and change it
            to correct user input
        """
        if index == len(self.next_list):
            self.quit = True
        else:
            self.next = self.next_list[index]
            self.done = True
            self.selected_index = 0
    
    def change_selected_option(self, operant=0):
        """
            for keyboard behaviour, change based on operant the selected
            option : single direction for now (up or down)
        """
        for index, option in enumerate(self.rendered["deselected"]):
            if option[1].collidepoint(pg.mouse.get_pos()):
                self.selected_index = index
        if operant:
            self.selected_index += operant
            max_indicator = len(self.rendered["deselected"]) - 1
            if self.selected_index < 0:
                self.selected_index = max_indicator
            elif self.selected_index > max_indicator:
                self.selected_index = 0