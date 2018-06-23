import pygame
from pygame.sprite import Sprite

class Missile(Sprite):
    # A class to manage missiles fired from the aircraft

    def __init__(self, game_settings, screen, aircraft):
        super().__init__()
        self.screen = screen

        # missile rect at (0, 0) and set it to correct position
        self.rect = pygame.Rect(0, 0, game_settings.missile_width,
            game_settings.missile_height)
        self.rect.centerx = aircraft.rect.centerx
        self.rect.top = aircraft.rect.top

        # store the missile's position as a decimal value
        self.y = float(self.rect.y)

        self.color = game_settings.missile_color
        self.speed_factor = game_settings.missile_speed_factor
    
    def update(self):
        # move the missile up the screen

        # update the decimal position of the missile
        self.y -= self.speed_factor
        # update the rect position
        self.rect.y = self.y

    def draw_Missile(self):
        # draw missile on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)        


    