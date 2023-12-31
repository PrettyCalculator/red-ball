import pygame
from settings import *
from level import Level
from pause import Pause

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
pygame.display.set_caption("Шарик")


clock = pygame.time.Clock()
level = Level(level_map, screen)
pause_button = Pause()

running = True
fps = 60
while running:
    screen.fill(pygame.Color('gray'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pause_button.get_focused(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and pause_button.get_focused:
            pause_button.get_clicked(event.pos)
    pause_button.update(screen)
    level.run()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
