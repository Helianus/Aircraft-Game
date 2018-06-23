import sys
import pygame
import functions as function
from pygame.sprite import Group
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
    missiles = Group()

    # loop of processing
    while True:

        function.check_events(game_settings, screen, aircraft, missiles)
        aircraft.update()
        missiles.update()
        
        function.update_screen(game_settings, screen, aircraft, missiles)

game_Runner()