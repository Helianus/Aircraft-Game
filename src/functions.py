import sys
import pygame

def check_events(aircraft):
    # loop of listerning event: keyboard and mouse
    for event in pygame.event.get():
        # quit event
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                aircraft.moving_right = True
            elif event.key == pygame.K_LEFT:
                aircraft.moveing_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                aircraft.moving_right = False
            elif event.key == pygame.K_LEFT:
                aircraft.moveing_left = False


def update_screen(game_settings, screen, aircraft):
        
        screen.fill(game_settings.background_color)  # fill the color during the loop

        aircraft.blit_image()
        
        pygame.display.flip()                        # update the most recently screen activity
        