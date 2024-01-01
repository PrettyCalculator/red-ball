import pygame
from settings import *
from level import Level
from homescreen import HomeScreen
from pause import Pause
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
pause_button = Pause()

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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and pause_button.get_focused:
                pause_button.get_clicked(event.pos)
    if mode == 'home':
        screen.fill(pygame.Color("#87cefa"))
        home.run()
    elif mode == 'game':
        bg_surf = pygame.transform.scale(bg_surf, (screen_width, screen_height))
        screen.blit(bg_surf, (0, 0))
        game.run()
        pause_button.update(screen)
    elif mode == 'exit':
        running = False
    elif mode == 'level':
        pass
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
