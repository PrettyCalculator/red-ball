import pygame
from tiles import Tile, JumpTile, PumpTile, WaterTile
from tiles import Tile, JumpTile, PumpTile, Star, Post
from settings import *
from player import Player
from functions import load_image


class Level:
    def __init__(self, level_data, surface):
        # настройка уровня
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.level_data = level_data

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.jump_tiles = pygame.sprite.Group()
        self.pump_tiles = pygame.sprite.Group()
        self.repump_tiles = pygame.sprite.Group()
        self.water_tiles = pygame.sprite.Group()
        self.star1, self.star2, self.star3 = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
        self.posts = pygame.sprite.Group()
        image_wall = load_image('wall.png')
        image_wall = pygame.transform.scale(image_wall, (tile_size, tile_size))

        image_jump = load_image('double_jump.jpg')
        image_jump = pygame.transform.scale(image_jump, (tile_size, tile_size))

        image_pump = load_image('pump.png')
        image_pump = pygame.transform.scale(image_pump, (30, 64))

        image_repump = load_image('repump.png')
        image_repump = pygame.transform.scale(image_repump, (80, 26))

        image_star = load_image('star.png', -1)
        image_star = pygame.transform.scale(image_star, (30, 30))

        image_post = load_image('post.png', -1)
        image_post = pygame.transform.scale(image_post, (30, 30))

        self.stars = load_image('small_star1.png', -1)
        self.small_stars = load_image('small_star.png', -1)

        self.stars1, self.stars2, self.stars3 = True, True, True
        self.num_star = 0

        image_water = pygame.Surface((tile_size, tile_size))
        image_water.fill('blue')

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
                elif cell == 'J':
                    jump_tile = JumpTile((x, y), image_jump)
                    self.jump_tiles.add(jump_tile)
                elif cell == '1':
                    pump_tile = PumpTile((x, y), image_pump)
                    self.pump_tiles.add(pump_tile)
                elif cell == '2':
                    repump_tile = PumpTile((x, y), image_repump)
                    self.repump_tiles.add(repump_tile)
                elif cell == 'W':
                    water_tile = WaterTile((x, y), image_water)
                    self.water_tiles.add(water_tile)
                elif cell == "S":
                    star_tile = Star((x, y + 30), image_star)
                    self.star1.add(star_tile)
                elif cell == "s":
                    star_tile = Star((x, y + 30), image_star)
                    self.star2.add(star_tile)
                elif cell == "c":
                    star_tile = Star((x, y + 30), image_star)
                    self.star3.add(star_tile)
                elif cell == "K":
                    post_tile = Post((x, y + 36), image_post)
                    self.posts.add(post_tile)

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
        f1 = False
        f2 = False
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    f1 = True
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    f2 = True
        for sprite in self.pump_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    f1 = True
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    f2 = True
                if not player.is_big:
                    player.change_size(True)
        for sprite in self.repump_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    f1 = True
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    f2 = True
                if player.is_big:
                    player.change_size(False)
        player.left_collide = f1
        player.right_collide = f2

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.is_double_jump = False
                    player.rect.bottom = sprite.rect.top
                    player.bunnyhop()
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                player.is_double_jump = False
        for sprite in self.jump_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.is_double_jump = True
                    player.bunnyhop()
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
        for sprite in self.pump_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.is_double_jump = False
                    player.rect.bottom = sprite.rect.top
                    player.bunnyhop()
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                if not player.is_big:
                    player.change_size(True)
                player.is_double_jump = False
        for sprite in self.repump_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.is_double_jump = False
                    player.rect.bottom = sprite.rect.top
                    player.bunnyhop()
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                if player.is_big:
                    player.change_size(False)
                player.is_double_jump = False

        for sprite in self.star1.sprites():
            if sprite.rect.colliderect(player.rect):
                self.stars1 = False
            if self.stars1:
                self.star1.update(self.world_shift)
                self.star1.draw(self.display_surface)
                self.display_surface.blit(self.small_stars, (-30, -100, 0, 0))
            else:
                self.display_surface.blit(self.stars, (-250, -113, 0, 0))

        for sprite in self.star2.sprites():
            if sprite.rect.colliderect(player.rect):
                self.stars2 = False
            if self.stars2:
                self.star2.update(self.world_shift)
                self.star2.draw(self.display_surface)
                self.display_surface.blit(self.small_stars, (30, -100, 20, 20))
            else:
                self.display_surface.blit(self.stars, (-180, -113, 0, 0))

        for sprite in self.star3.sprites():
            if sprite.rect.colliderect(player.rect):
                self.stars3 = False
            if self.stars3:
                self.star3.update(self.world_shift)  # звезда
                self.star3.draw(self.display_surface)
                self.display_surface.blit(self.small_stars, (90, -100, 20, 20))
            else:
                self.display_surface.blit(self.stars, (-110, -113, 0, 0))

        for sprite in self.posts.sprites():
            if sprite.rect.colliderect(player.rect):
                self.setup_level(self.level_data)
                player.rect.x = 350
                player.rect.y = 20

    def run(self):
        # квадратики уровня
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.jump_tiles.update(self.world_shift)
        self.jump_tiles.draw(self.display_surface)
        self.pump_tiles.update(self.world_shift)
        self.pump_tiles.draw(self.display_surface)
        self.repump_tiles.update(self.world_shift)
        self.repump_tiles.draw(self.display_surface)
        self.water_tiles.update(self.world_shift)
        self.water_tiles.draw(self.display_surface)

        self.posts.update(self.world_shift)
        self.posts.draw(self.display_surface)

        self.scroll_x()

        # сам герой
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
