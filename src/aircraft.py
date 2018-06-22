# Aircraft object

import pygame

class Aircraft():

    def __init__(self, game_settings, screen):

        # Load the image
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load('images/aircraft.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set aircraft to the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for the aircraft's center
        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.moveing_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.aircraft_speed_factor
        if self.moveing_left and self.rect.left > 0:
            self.center -= self.game_settings.aircraft_speed_factor

        # update rect object from self.center
        self.rect.centerx = self.center

    def blit_image(self):
        self.screen.blit(self.image, self.rect)