from settings import *
from tiles import Tile
from player import Player
from functions import load_image


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

        self.btn_rect1 = pygame.Rect(250, 100, tile_size + 50, tile_size + 50)
        self.btn_rect2 = pygame.Rect(550, 100, tile_size + 50, tile_size + 50)
        self.btn_rect3 = pygame.Rect(850, 100, tile_size + 50, tile_size + 50)

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

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        pygame.draw.rect(self.display_surface, pygame.Color('#b30000'), self.btn_rect1, 352, 31)
        pygame.draw.rect(self.display_surface, pygame.Color('#b30000'), self.btn_rect2, 60, 31)
        pygame.draw.rect(self.display_surface, pygame.Color('#b30000'), self.btn_rect3, 60, 31)
        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.btn_rect1.collidepoint(mouse_pos):
                print(1)
            elif self.btn_rect2.collidepoint(mouse_pos):
                print(2)
            elif self.btn_rect3.collidepoint(mouse_pos):
                change_mode('game')
        self.player.update()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
