import pygame
from tiles import Tile, JumpTile
from settings import *
from player import Player
from functions import load_image


class Level:
    def __init__(self, level_data, surface):
        # настройка уровня
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.jump_tiles = pygame.sprite.Group()

        image_wall = load_image('wall.png')
        image_wall = pygame.transform.scale(image_wall, (tile_size, tile_size))

        image_jump = pygame.Surface((tile_size, tile_size))

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == "X":
                    tile = Tile((x, y), image_wall)
                    self.tiles.add(tile)
                if cell == "P":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                if cell == 'J':
                    jump_tile = JumpTile((x, y), image_jump)
                    self.jump_tiles.add(jump_tile)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.is_jump = False
                    player.jump_speed = -15
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
        for sprite in self.jump_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.jump_speed = -20
                    player.direction.y = 0
                    player.is_jump = False
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        # квадратики уровня
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.jump_tiles.update(self.world_shift)
        self.jump_tiles.draw(self.display_surface)
        self.scroll_x()

        # сам герой
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)