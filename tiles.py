from settings import *


class Tile(pygame.sprite.Sprite):  # класс всех тайлов
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):  # функция перемещения тайла в соответствии с движением мяча
        self.rect.x += x_shift



