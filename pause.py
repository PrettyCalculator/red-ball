import pygame
from functions import *
from settings import *


class Pause(pygame.sprite.Sprite):
    initialization()
    small = load_image('pause9.png')
    small = pygame.transform.scale(small, (60, 60))
    big = load_image('pause9.png')
    big = pygame.transform.scale(big, (80, 80))

    def __init__(self):
        self.image = Pause.small
        self.focused = False

    def change(self):
        if self.focused:
            self.image = Pause.big
        else:
            self.image = Pause.small

    def update(self, screen):
        self.change()
        screen.blit(self.image, (screen_width - 70, 10))

