import pygame
from settings import *
from level import Level

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
pygame.display.set_caption("Шарик")

clock = pygame.time.Clock()
level = Level(level_map, screen)

running = True
fps = 60
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color('gray'))
    level.run()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
