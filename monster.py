import pygame
from player import Player
from functions import load_image
from settings import *


class Monster(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(load_image('monstr2.png', -1), (tile_size, tile_size))
        self.direction = pygame.math.Vector2(0, 0)
        self.direction.y = -1
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 1

    def update(self, x_shift):
        self.rect.y += self.speed * self.direction.y
        self.rect.x += x_shift