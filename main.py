import pygame
from settings import *
from level import Level
from homescreen import HomeScreen

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
pygame.display.set_caption("Шарик")

home = HomeScreen(homescreen_map, screen)
game = Level(level_map, screen)
clock = pygame.time.Clock()

running = True
fps = 60
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color('gray'))
    if mode == 'home':
        home.run()
    elif mode == 'game':
        game.run()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
