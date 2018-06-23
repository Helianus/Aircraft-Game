# Setting of the game
class Setting():
    def __init__(self):
        
        #screen settings
        self.screen_width = 1080
        self.screen_height = 720
        self.background_color = (255, 255, 255)

        # aircraft settings
        self.aircraft_speed_factor = 1.5

        # missile settings
        self.missile_speed_factor = 1
        self.missile_width = 3
        self.missile_height = 15
        self.missile_color = 60, 60, 60