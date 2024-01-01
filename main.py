import pygame
from settings import *
from level import Level
from homescreen import HomeScreen
from pause import Pause, PauseMenu

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
pygame.display.set_caption("Шарик")

home = HomeScreen(homescreen_map, screen)
game = Level(level_map, screen)
pause_button = Pause()
pause_menu = PauseMenu()

clock = pygame.time.Clock()
running = True
fps = 60
while running:
    from settings import mode
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if mode == 'game':
            if event.type == pygame.MOUSEMOTION:
                pause_button.get_focused(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN and pause_button.get_focused:
                pause_button.get_clicked()
        elif mode == 'pause':
            if event.type == pygame.MOUSEMOTION:
                pause_menu.get_focused(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pause_menu.get_clicked(event.pos)

    if mode == 'home':
        screen.fill(pygame.Color('gray'))
        home.run()
    elif mode == 'game':
        game.pause = False
        screen.fill(pygame.Color('gray'))
        game.run()
        pause_button.update(screen)
    elif mode == 'pause':
        game.pause = True
        pause_menu.update(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
