import sys
import pygame

from setting import Setting
from aircraft import Aircraft

def game_Runner():
    
    pygame.init()                                   # Initialize
    
    game_settings = Setting()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Aircraft Game")

    # create an aircraft
    aircraft = Aircraft(screen)    
    # loop of processing
    while True:

        # loop of listerning event: keyboard and mouse
        for event in pygame.event.get():
            
            # quit event
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(game_settings.background_color)               # fill the color during the loop

        aircraft.blit_image()
        
        pygame.display.flip()                       # update the most recently screen activity

game_Runner()