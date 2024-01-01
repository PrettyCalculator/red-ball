import pygame
from settings import *
from tiles import Tile
from player import Player
from functions import load_image


class HomeScreen:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        image_wall = load_image('wall.png')
        image_wall = pygame.transform.scale(image_wall, (tile_size, tile_size))

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == "X":
                    tile = Tile((x, y), image_wall)
                    self.tiles.add(tile)
                elif cell == "P":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.jump()
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        self.player.update()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
