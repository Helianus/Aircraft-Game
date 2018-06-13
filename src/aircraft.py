# Aircraft object

import pygame

class Aircraft():

    def __init__(self, screen):

        # Load the image
        self.screen = screen
        self.image = pygame.image.load('images/aircraft.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set aircraft to the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blit_image(self):
        self.screen.blit(self.image, self.rect)