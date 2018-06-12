import sys
import pygame

def game_Runner():
    
    pygame.init()                                   # Initialize
    screen = pygame.display.set_mode((1080, 720))   # create a screen
    pygame.display.set_caption("Game")              # set the title of the window

    background_color = (100, 100, 100)              # set the background color

    # loop of processing
    while True:

        # loop of listerning event: keyboard and mouse
        for event in pygame.event.get():
            
            # quit event
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(background_color)               # fill the color during the loop

        pygame.display.flip()                       # update the most recently screen activity

game_Runner()