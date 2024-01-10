from level import Level
from homescreen import HomeScreen
from levelscreen import LevelScreen
from pause import *
from functions import load_image
from sound import Sound

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
pygame.display.set_caption('red-ball')

home = HomeScreen(homescreen_map, screen)
level = LevelScreen(homescreen_map, screen)

clock = pygame.time.Clock()
background = [load_image('background.jpg'), load_image('fone8.jpg'),
              load_image('fone4.jpg'), load_image('fone7.png'), load_image('fone1.png'), load_image('fone2.png')]
pause_button = Pause()
pause_menu = PauseMenu()
transition_menu = TransitionMenu()
passed_menu = PassedMenu()

sound = Sound()
sound.background()

running = True
fps = 60
count = 0
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
                if value == 'exit':
                    game.to_start()
                elif value == 'resume':
                    game.setup_level(game.level_data)
                elif value == 'volume':
                    sound.update_volume()
        elif mode == 'transition':
            if event.type == pygame.MOUSEMOTION:
                transition_menu.get_focused(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                value = transition_menu.get_clicked(event.pos)
                if value == 'exit':
                    game.to_start()
                elif value == 'resume':
                    game.change_level()
        elif mode == 'passed':
            if event.type == pygame.MOUSEMOTION:
                passed_menu.get_focused(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                value = passed_menu.get_clicked(event.pos)
                if value == 'exit':
                    game.to_start()

    if mode == 'home':
        count = 0
        screen.fill(pygame.Color("#87cefa"))
        home.run()
    elif mode == 'level':
        count = 0
        screen.fill(pygame.Color("#87cefa"))
        level.run()
    elif mode == 'game':
        if count == 0:
            from settings import num

            game = Level(screen, num)
            count += 1
        bg_surf = pygame.transform.scale(background[num], (screen_width, screen_height))
        screen.blit(bg_surf, (0, 0))
        game.pause = False
        game.run()
        pause_button.update(screen)
    elif mode == 'exit':
        count = 0
        running = False
    elif mode == 'pause':
        game.pause = True
        pause_menu.update(screen)
    elif mode == 'transition':
        transition_menu.update(screen, game.count_stars())
    elif mode == 'passed':
        passed_menu.update(screen, game.count_stars())
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
