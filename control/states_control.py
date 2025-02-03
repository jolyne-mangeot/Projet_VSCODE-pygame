from control.control import Control

class States(Control):
    def __init__(self):
        Control.__init__(self)
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None