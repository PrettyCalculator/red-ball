import pygame
from functions import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, layout):
        super().__init__()
        self.image = load_image('wall.png')
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
