import pygame
from tiles import *
from settings import *
from player import Player
from functions import load_image, initialization


class Level:
    def __init__(self, surface):
        # настройка уровня
        self.display_surface = surface
        self.levels = levels
        self.level_index = 0
        self.level_data = self.levels[self.level_index]
        self.setup_level(self.level_data)
        self.world_shift = 0
        self.pause = False
        self.passed = False

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.jump_tiles = pygame.sprite.Group()
        self.pump_tiles = pygame.sprite.Group()
        self.repump_tiles = pygame.sprite.Group()
        self.water_tiles = pygame.sprite.Group()
        self.star1 = pygame.sprite.GroupSingle()
        self.star2 = pygame.sprite.GroupSingle()
        self.star3 = pygame.sprite.GroupSingle()
        self.posts = pygame.sprite.Group()
        self.door = pygame.sprite.GroupSingle()
        self.lava = pygame.sprite.Group()
        self.monstr = pygame.sprite.Group()

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

        image_door = load_image('door.png', -1)
        image_door = pygame.transform.scale(image_door, (tile_size + 7, tile_size + 7))

        image_lava = load_image('lava.jpg', -1)
        image_lava = pygame.transform.scale(image_lava, (tile_size, tile_size))

        image_monstr = load_image('monstr2.png', -1)
        image_monstr = pygame.transform.scale(image_monstr, (tile_size, tile_size))

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
                    jump_tile = Tile((x, y), image_jump)
                    self.jump_tiles.add(jump_tile)
                elif cell == '1':
                    pump_tile = Tile((x, y), image_pump)
                    self.pump_tiles.add(pump_tile)
                elif cell == '2':
                    repump_tile = Tile((x, y), image_repump)
                    self.repump_tiles.add(repump_tile)
                elif cell == 'W':
                    water_tile = Tile((x, y), image_water)
                    self.water_tiles.add(water_tile)
                elif cell == "S":
                    star_tile = Tile((x, y + 30), image_star)
                    self.star1.add(star_tile)
                elif cell == "s":
                    star_tile = Tile((x, y + 30), image_star)
                    self.star2.add(star_tile)
                elif cell == "c":
                    star_tile = Tile((x, y + 30), image_star)
                    self.star3.add(star_tile)
                elif cell == "K":
                    post_tile = Tile((x, y + 36), image_post)
                    self.posts.add(post_tile)
                elif cell == 'D':
                    door_tile = Tile((x, y), image_door)
                    self.door.add(door_tile)
                elif cell == 'L':
                    lava_tile = Tile((x, y), image_lava)
                    self.lava.add(lava_tile)
                elif cell == 'M':
                    monstr_tile = Tile((x, y), image_monstr)
                    self.monstr.add(monstr_tile)

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
        if self.door.sprite.rect.colliderect(player.rect):
            pass
        player.left_collide = f1
        player.right_collide = f2

    def vertical_movement_collision(self):
        player = self.player.sprite
        wall = self.tiles.sprites()
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

        for sprite in self.lava.sprites():
            if sprite.rect.colliderect(player.rect):
                self.setup_level(self.level_data)
                player.rect.x = 350
                player.rect.y = 2

        if self.star1.sprite.rect.colliderect(player.rect) and self.stars1:
            self.stars1 = False
            self.num_star += 1
        if self.stars1:
            self.star1.update(self.world_shift)
            self.star1.draw(self.display_surface)
        if self.num_star < 1:
            self.display_surface.blit(self.small_stars, (-30, -100, 0, 0))

        if self.star2.sprite.rect.colliderect(player.rect) and self.stars2:
            self.stars2 = False
            self.num_star += 1
        if self.stars2:
            self.star2.update(self.world_shift)
            self.star2.draw(self.display_surface)
        if self.num_star < 2:
            self.display_surface.blit(self.small_stars, (30, -100, 20, 20))

        if self.star3.sprite.rect.colliderect(player.rect) and self.stars3:
            self.stars3 = False
            self.num_star += 1
        if self.stars3:
            self.star3.update(self.world_shift)  # звезда
            self.star3.draw(self.display_surface)
        if self.num_star < 3:
            self.display_surface.blit(self.small_stars, (90, -100, 20, 20))

        if self.num_star == 1:
            self.display_surface.blit(self.stars, (-250, -113, 0, 0))
        elif self.num_star == 2:
            self.display_surface.blit(self.stars, (-250, -113, 0, 0))
            self.display_surface.blit(self.stars, (-180, -113, 0, 0))
        elif self.num_star == 3:
            self.display_surface.blit(self.stars, (-250, -113, 0, 0))
            self.display_surface.blit(self.stars, (-180, -113, 0, 0))
            self.display_surface.blit(self.stars, (-110, -113, 0, 0))

        for sprite in self.posts.sprites():
            if sprite.rect.colliderect(player.rect):
                self.setup_level(self.level_data)
                player.rect.x = 350
                player.rect.y = 2

        if player.rect.y >= 600:
            self.setup_level(self.level_data)
            player.rect.x = 350
            player.rect.y = 20

    def run(self):
        if not self.pause:
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
            self.door.update(self.world_shift)
            self.door.draw(self.display_surface)
            self.lava.update(self.world_shift)
            self.lava.draw(self.display_surface)
            self.monstr.update(self.world_shift)
            self.monstr.draw(self.display_surface)

            self.scroll_x()

            # сам герой
            self.player.update()
            self.horizontal_movement_collision()
            self.vertical_movement_collision()
            self.player.draw(self.display_surface)
        else:
            self.tiles.draw(self.display_surface)
            self.jump_tiles.draw(self.display_surface)
            self.pump_tiles.draw(self.display_surface)
            self.repump_tiles.draw(self.display_surface)
            self.water_tiles.draw(self.display_surface)
            self.posts.draw(self.display_surface)
            self.horizontal_movement_collision()
            self.vertical_movement_collision()
            self.player.draw(self.display_surface)
