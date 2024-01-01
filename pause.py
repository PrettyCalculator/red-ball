import pygame
from functions import *
from settings import *


class Pause(pygame.sprite.Sprite):
    initialization()

    POS_SMALL = screen_width - 70, 10
    POS_BIG = screen_width - 90, 10

    SIZE_SMALL = 60, 60
    SIZE_BIG = 80, 80

    img = load_image('pause9.png')
    small = pygame.transform.scale(img, SIZE_SMALL)
    big = pygame.transform.scale(img, SIZE_BIG)

    def __init__(self):
        self.image = Pause.small
        self.size = Pause.SIZE_SMALL
        self.pos = Pause.POS_SMALL
        self.rect = self.image.get_rect(topleft=self.pos)
        self.focused = False

    def change(self):
        if self.focused:
            self.image = Pause.big
            self.pos = Pause.POS_BIG
        else:
            self.image = Pause.small
            self.pos = Pause.POS_SMALL

    def get_focused(self, pos):
        if self.rect.collidepoint(pos):
            self.focused = True
            self.change()
        else:
            self.focused = False
            self.change()

    def get_clicked(self, event):
        pass

    def update(self, screen):
        screen.blit(self.image, self.pos)
