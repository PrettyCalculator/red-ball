import pygame
from settings import *
from level import Level
from homescreen import HomeScreen
from functions import load_image

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
pygame.display.set_caption("Шарик")

home = HomeScreen(homescreen_map, screen)
game = Level(level_map, screen)
clock = pygame.time.Clock()
bg_surf = load_image('background.jpg')
running = True
fps = 60
while running:
    from settings import mode

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if mode == 'home':
        screen.fill(pygame.Color("#87cefa"))
        home.run()
    elif mode == 'game':
        bg_surf = pygame.transform.scale(bg_surf, (screen_width, screen_height))
        screen.blit(bg_surf, (0, 0))
        game.run()
    elif mode == 'exit':
        running = False
    elif mode == 'level':
        pass
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
