from settings import *
from level import Level
from homescreen import HomeScreen
from levelscreen import LevelScreen
from pause import Pause, PauseMenu
from functions import load_image
from sound import Sound

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
pygame.display.set_caption("Шарик")

home = HomeScreen(homescreen_map, screen)
level = LevelScreen(homescreen_map, screen)
game = Level(screen)

clock = pygame.time.Clock()
bg_surf = load_image('background.jpg')
pause_button = Pause()
pause_menu = PauseMenu()

sound = Sound()
sound.background()

running = True
fps = 60
while running:
    from settings import mode

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            sound.click()
        if mode == 'game':
            if event.type == pygame.MOUSEMOTION:
                pause_button.get_focused(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN and pause_button.get_focused:
                pause_button.get_clicked()
        elif mode == 'pause':
            if event.type == pygame.MOUSEMOTION:
                pause_menu.get_focused(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                value = pause_menu.get_clicked(event.pos)
                if value:
                    sound.background_sound.set_volume(value)

    if mode == 'home':
        screen.fill(pygame.Color("#87cefa"))
        home.run()
    elif mode == 'level':
        screen.fill(pygame.Color("#87cefa"))
        level.run()
    elif mode == 'game':
        bg_surf = pygame.transform.scale(bg_surf, (screen_width, screen_height))
        screen.blit(bg_surf, (0, 0))
        game.pause = False
        game.run()
        pause_button.update(screen)
    elif mode == 'exit':
        running = False
    elif mode == 'pause':
        game.pause = True
        pause_menu.update(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
