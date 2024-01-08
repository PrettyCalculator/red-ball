from tiles import Tile
from settings import *
from player import Player
from functions import load_image
from monster import *
import sqlite3


class Level:
    def __init__(self, surface, num):
        # настройка уровня
        self.display_surface = surface
        self.levels = levels
        self.level_index = num
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
        self.star1, self.star2, self.star3 = (pygame.sprite.GroupSingle(), pygame.sprite.GroupSingle(),
                                              pygame.sprite.GroupSingle())
        self.posts = pygame.sprite.Group()
        self.door = pygame.sprite.GroupSingle()
        self.lava = pygame.sprite.Group()
        self.monster_vertical = pygame.sprite.Group()
        self.monster_horizontal = pygame.sprite.Group()

        image_wall = load_image('wall6.png')
        image_wall = pygame.transform.scale(image_wall, (tile_size, tile_size))

        image_jump = load_image('double_jump.jpg')
        image_jump = pygame.transform.scale(image_jump, (tile_size, tile_size))

        image_pump = load_image('big.png', -1)
        image_pump = pygame.transform.scale(image_pump, (30, 64))

        image_repump = load_image('repump.png')
        image_repump = pygame.transform.scale(image_repump, (80, 26))

        image_star = load_image('star.png', -1)
        image_star = pygame.transform.scale(image_star, (30, 30))

        image_post = load_image('post.png', -1)
        image_post = pygame.transform.scale(image_post, (30, 30))

        image_door = load_image('door.png', -1)
        image_door = pygame.transform.scale(image_door, (tile_size + 7, tile_size + 7))

        image_lava = load_image('lava2.jpg', -1)
        image_lava = pygame.transform.scale(image_lava, (tile_size, tile_size))

        image_monster = load_image('monstr2.png', -1)
        image_monster = pygame.transform.scale(image_monster, (tile_size, tile_size))

        self.stars = load_image('small_star1.png', -1)
        self.small_stars = load_image('small_star.png', -1)

        self.stars1, self.stars2, self.stars3 = True, True, True
        self.num_star = 0

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == "X":
                    self.tiles.add(Tile((x, y), image_wall))
                elif cell == "P":
                    self.player.add(Player((x, y)))
                elif cell == 'J':
                    self.jump_tiles.add(Tile((x, y), image_jump))
                elif cell == '1':
                    self.pump_tiles.add(Tile((x + 17, y), image_pump))
                elif cell == '2':
                    self.repump_tiles.add(Tile((x, y + 39), image_repump))
                elif cell == "S":
                    self.star1.add(Tile((x + 20, y + 30), image_star))
                elif cell == "s":
                    self.star2.add(Tile((x + 20, y + 30), image_star))
                elif cell == "c":
                    self.star3.add(Tile((x + 20, y + 30), image_star))
                elif cell == "K":
                    self.posts.add(Tile((x, y + 36), image_post))
                elif cell == 'L':
                    lava_tile = Tile((x, y), image_lava)
                    self.lava.add(lava_tile)
                elif cell == 'M':
                    self.monster_vertical.add(MonsterVertical((x, y), image_monster))
                elif cell == 'D':
                    self.door.add(Tile((x, y), image_door))
                elif cell == 'm':
                    self.monster_horizontal.add(MonsterHorizontal((x, y), image_monster))

    def count_stars(self):
        c = 0
        if not self.stars1:
            c += 1
        if not self.stars2:
            c += 1
        if not self.stars3:
            c += 1
        return c

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
        for sprite in pygame.sprite.spritecollide(player, self.tiles, False):
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    f1 = True
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    f2 = True
        for sprite in pygame.sprite.spritecollide(player, self.jump_tiles, False):
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    f1 = True
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    f2 = True
        for sprite in pygame.sprite.spritecollide(player, self.pump_tiles, False):
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    f1 = True
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    f2 = True
                if not player.is_big:
                    player.change_size(True)
        for sprite in pygame.sprite.spritecollide(player, self.repump_tiles, False):
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
            if self.level_index + 1 > len(self.levels) - 1:
                change_mode('passed')
                self.update_database()
                self.pause = True
            else:
                self.update_database()
                change_mode('transition')
                self.pause = True
        player.left_collide = f1
        player.right_collide = f2

    def monster_vertical_collision(self):
        for monster in self.monster_vertical.sprites():
            for sprite in pygame.sprite.spritecollide(monster, self.tiles, False):
                if sprite.rect.colliderect(monster.rect):
                    if monster.direction.y < 0:
                        monster.rect.top = sprite.rect.bottom
                        monster.direction.y = - monster.direction.y
                    elif monster.direction.y > 0:
                        monster.rect.bottom = sprite.rect.top
                        monster.direction.y = - monster.direction.y
        for monster in self.monster_vertical.sprites():
            for sprite in pygame.sprite.spritecollide(monster, self.jump_tiles, False):
                if sprite.rect.colliderect(monster.rect):
                    if monster.direction.y < 0:
                        monster.rect.top = sprite.rect.bottom
                        monster.direction.y = - monster.direction.y
                    elif monster.direction.y > 0:
                        monster.rect.bottom = sprite.rect.top
                        monster.direction.y = - monster.direction.y

    def monster_horizontal_collision(self):
        for monster in self.monster_horizontal.sprites():
            for sprite in pygame.sprite.spritecollide(monster, self.tiles, False):
                if sprite.rect.colliderect(monster.rect):
                    if monster.direction.x < 0:
                        monster.rect.left = sprite.rect.right
                    elif monster.direction.x > 0:
                        monster.rect.right = sprite.rect.left
                    monster.direction.x = - monster.direction.x
        for monster in self.monster_horizontal.sprites():
            for sprite in pygame.sprite.spritecollide(monster, self.jump_tiles, False):
                if sprite.rect.colliderect(monster.rect):
                    if monster.direction.x < 0:
                        monster.rect.left = sprite.rect.right
                    elif monster.direction.x > 0:
                        monster.rect.right = sprite.rect.left
                    monster.direction.x = - monster.direction.x

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        for sprite in pygame.sprite.spritecollide(player, self.tiles, False):
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.is_double_jump = False
                    player.rect.bottom = sprite.rect.top
                    player.bunnyhop()
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                player.is_double_jump = False
        for sprite in pygame.sprite.spritecollide(player, self.jump_tiles, False):
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.is_double_jump = True
                    player.bunnyhop()
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
        for sprite in pygame.sprite.spritecollide(player, self.pump_tiles, False):
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
        for sprite in pygame.sprite.spritecollide(player, self.repump_tiles, False):
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

        if pygame.sprite.spritecollide(player, self.monster_vertical, False):
            self.setup_level(self.level_data)

        if pygame.sprite.spritecollide(player, self.monster_horizontal, False):
            self.setup_level(self.level_data)

        if pygame.sprite.spritecollide(player, self.lava, False):
            self.setup_level(self.level_data)

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

        if player.rect.y >= 600:
            self.setup_level(self.level_data)

    def change_level(self):
        self.level_index += 1
        if self.level_index > len(self.levels) - 1:
            self.to_start()
            change_mode('passed')
        self.level_data = self.levels[self.level_index]
        self.setup_level(self.level_data)

    def to_start(self):
        self.level_index = num
        self.level_data = self.levels[self.level_index]
        self.setup_level(self.level_data)

    def update_database(self):
        con = sqlite3.connect('data/db/database.sqlite')
        cursor = con.cursor()
        stars_game = self.count_stars()
        stars_db = cursor.execute(f"SELECT stars FROM levels WHERE level_id = {self.level_index}").fetchall()[0][0]
        if stars_db < stars_game:
            cursor.execute(f"UPDATE levels SET passed = 1, stars = {self.count_stars()} "
                           f"WHERE level_id = {self.level_index}")
        con.commit()
        con.close()

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

            self.monster_vertical_collision()
            self.monster_vertical.update(self.world_shift)
            self.monster_vertical.draw(self.display_surface)

            self.monster_horizontal_collision()
            self.monster_horizontal.update(self.world_shift)
            self.monster_horizontal.draw(self.display_surface)

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
