import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class JumpTile(Tile):
    pass


class PumpTile(Tile):
    pass


class RePumpTile(Tile):
    pass
