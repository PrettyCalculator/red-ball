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

        image_wall = load_image('wall6.png')
        image_wall = pygame.transform.scale(image_wall, (tile_size, tile_size))

        btn_width, btn_height = 270, 70
        btn_x, btn_y = screen_width // 2 - btn_width // 2, screen_height // 2 - btn_height // 2
        self.btn_rect = pygame.Rect(btn_x + 250, btn_y - 70, btn_width, btn_height)
        self.btn_rect1 = pygame.Rect(btn_x + 250, btn_y + 50, btn_width, btn_height)
        self.text1 = font.render("Play", True, pygame.Color('#a8d8ff'))
        self.text2 = font.render("Exit", True, pygame.Color('#a8d8ff'))
        self.text_x = btn_x + 780 // 2 - self.text1.get_width() // 2
        self.text_y = btn_y - 70 // 2 - self.text1.get_height() // 2
        self.text_x1 = btn_x + 770 // 2 - self.text1.get_width() // 2
        self.text_y1 = btn_y + 170 // 2 - self.text1.get_height() // 2

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
        pygame.draw.rect(self.display_surface, pygame.Color('#b30000'), self.btn_rect, 35, 3)
        pygame.draw.rect(self.display_surface, pygame.Color('#b30000'), self.btn_rect1, 35, 3)
        self.display_surface.blit(self.text1, (self.text_x, self.text_y))
        self.display_surface.blit(self.text2, (self.text_x1, self.text_y1))
        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.btn_rect.collidepoint(mouse_pos):
                change_mode('level')
            if self.btn_rect1.collidepoint(mouse_pos):
                change_mode('exit')
        self.player.update()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
