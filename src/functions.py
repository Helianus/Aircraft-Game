import sys
import pygame
from missile import Missile


def check_keydown_events(event, game_settings, screen, aircraft, missiles):
    # respond to keypresses
    if event.key == pygame.K_RIGHT:
        aircraft.moving_right = True
    elif event.key == pygame.K_LEFT:
        aircraft.moveing_left = True
    elif event.key == pygame.K_SPACE:
        # new missile and add it to the group
        new_missile = Missile(game_settings, screen, aircraft)
        missiles.add(new_missile)

def check_keyup_events(event, aircraft):
    # respond to key releases
     if event.key == pygame.K_RIGHT:
        aircraft.moving_right = False
     elif event.key == pygame.K_LEFT:
        aircraft.moveing_left = False




def check_events(game_settings, screen, aircraft, missiles):
    # loop of listerning event: keyboard and mouse
    for event in pygame.event.get():
        # quit event
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, aircraft, missiles)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, aircraft)
           

def update_screen(game_settings, screen, aircraft, missiles):
        
        screen.fill(game_settings.background_color)  # fill the color during the loop

        # redraw all missiles behind aircraft and UFO
        for missile in missiles.sprites():
            missile.draw_Missile()

        aircraft.blit_image()
        
        pygame.display.flip()                        # update the most recently screen activity
        
        