from settings import *
from tiles import Tile
from player import Player
from functions import load_image
import sqlite3


class LevelScreen:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        image_wall = load_image('wall.png')
        image_wall = pygame.transform.scale(image_wall, (tile_size, tile_size))

        self.star0 = load_image('star_0.png', -1)
        self.star0 = pygame.transform.scale(self.star0, (80, 35))
        self.star1 = load_image('star_1.png', -1)
        self.star1 = pygame.transform.scale(self.star1, (80, 35))
        self.star2 = load_image('star_2.png', -1)
        self.star2 = pygame.transform.scale(self.star2, (80, 35))
        self.star3 = load_image('star_3.png', -1)
        self.star3 = pygame.transform.scale(self.star3, (80, 35))

        self.level_close = load_image('level_close.png')

        self.btn_rect1 = pygame.Rect(250, 100, tile_size + 50, tile_size + 50)
        self.btn_rect2 = pygame.Rect(550, 100, tile_size + 50, tile_size + 50)
        self.btn_rect3 = pygame.Rect(850, 100, tile_size + 50, tile_size + 50)
        self.btn_exit = pygame.Rect(950, 550, 200, 40)

        self.all = [[self.display_surface, pygame.Color('#b30000'), self.btn_rect1, 352, 2],
                    [self.display_surface, pygame.Color('#b30000'), self.btn_rect2, 60, 2],
                    [self.display_surface, pygame.Color('#b30000'), self.btn_rect3, 60, 2]]

        self.coordinates = [(250, 100), (550, 100), (850, 100)]

        self.text1 = font.render("1", True, pygame.Color('#a8d8ff'))
        self.text2 = font.render("2", True, pygame.Color('#a8d8ff'))
        self.text3 = font.render("3", True, pygame.Color('#a8d8ff'))
        self.exit = font.render("Exit", True, pygame.Color('#a8d8ff'))

        self.all_text = [(self.text1, (300, 137)),
                         (self.text2, (600, 137)),
                         (self.text3, (900, 137))]

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == "X":
                    self.tiles.add(Tile((x, y), image_wall))
                elif cell == "P":
                    self.player.add(Player((x, y)))

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        for sprite in pygame.sprite.spritecollide(player, self.tiles, False):
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.jump()
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def windows(self):
        con = sqlite3.connect('data/db/database.sqlite')
        cursor = con.cursor()
        self.result = cursor.execute("""SELECT * FROM levels""").fetchall()
        last = 0
        x_pos = [268, 568, 868]
        for i in range(len(self.all)):
            if self.result[i][1] == 1 or last == 1 or i == 0:
                pygame.draw.rect(*self.all[i])
                self.display_surface.blit(*self.all_text[i])
                last = self.result[i][1]
                if self.result[i][2] == 0:
                    self.display_surface.blit(self.star0, (x_pos[i], 175))
                elif self.result[i][2] == 1:
                    pass
                    self.display_surface.blit(self.star1, (x_pos[i], 175))
                elif self.result[i][2] == 2:
                    self.display_surface.blit(self.star2, (x_pos[i], 175))
                else:
                    self.display_surface.blit(self.star3, (x_pos[i], 175))
            else:
                level = pygame.transform.scale(self.level_close, (118, 118))
                screen.blit(level, self.coordinates[i])
        con.commit()
        con.close()

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        pygame.draw.rect(self.display_surface, pygame.Color('#b30000'), self.btn_exit, 20, 5)
        self.display_surface.blit(self.exit, (1020, 555))
        self.windows()
        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.btn_rect1.collidepoint(mouse_pos):
                change_num(0)
                change_mode('game')
            elif self.btn_rect2.collidepoint(mouse_pos) and self.result[0][1] == 1:
                change_num(1)
                change_mode('game')
            elif self.btn_rect3.collidepoint(mouse_pos) and self.result[1][1] == 1:
                change_num(2)
                change_mode('game')
            elif self.btn_exit.collidepoint(mouse_pos):
                change_num(3)
                change_mode('home')
        self.player.update()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
