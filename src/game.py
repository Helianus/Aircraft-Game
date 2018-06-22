import sys
import pygame
import functions as function

from setting import Setting
from aircraft import Aircraft

def game_Runner():
    
    pygame.init()                                   # Initialize
    
    game_settings = Setting()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Aircraft Game")

    # create an aircraft
    aircraft = Aircraft(game_settings, screen)    
    # loop of processing
    while True:

        function.check_events(aircraft)
        aircraft.update()
        
        function.update_screen(game_settings, screen, aircraft)

game_Runner()