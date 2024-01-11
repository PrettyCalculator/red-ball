from level import Level
from homescreen import HomeScreen
from levelscreen import LevelScreen
from pause import *
from functions import load_image
from sound import Sound

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('red-ball')

home = HomeScreen(homescreen_map, screen)  # инициализация главного экрана
level = LevelScreen(homescreen_map, screen)  # инициализация экрана выбором уровней

clock = pygame.time.Clock()
background = [load_image('background.jpg'), load_image('fone8.jpg'),
              load_image('fone4.jpg'), load_image('fone7.png'), load_image('fone1.png'), load_image('fone2.png')]  # список фонов для всех уровней
pause_button = Pause()  # инициализация паузы в правом верхнем углу
pause_menu = PauseMenu()  # меню паузы
transition_menu = TransitionMenu()  # меню между уровнями
passed_menu = PassedMenu()  # меню после прохождения последнего уровня

sound = Sound()
sound.background()  # фоновая музыка

running = True
fps = 60
count = 0
while running:
    from settings import mode

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # клик при нажатии мышкой
            sound.click()
        if mode == 'game':  # при игре
            if event.type == pygame.MOUSEMOTION:
                pause_button.get_focused(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN and pause_button.get_focused:
                pause_button.get_clicked()
        elif mode == 'pause':  # при паузе
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
        elif mode == 'transition':  # при переходе на другой уровень
            if event.type == pygame.MOUSEMOTION:
                transition_menu.get_focused(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                value = transition_menu.get_clicked(event.pos)
                if value == 'exit':
                    game.to_start()
                elif value == 'resume':
                    game.change_level()
        elif mode == 'passed':  # при прохождении последнего уровня
            if event.type == pygame.MOUSEMOTION:
                passed_menu.get_focused(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                value = passed_menu.get_clicked(event.pos)
                if value == 'exit':
                    game.to_start()

    if mode == 'home':  # на главном экране
        count = 0
        screen.fill(pygame.Color("#87cefa"))
        home.run()
    elif mode == 'level':  # на экране с уровнями
        count = 0
        screen.fill(pygame.Color("#87cefa"))
        level.run()
    elif mode == 'game':  # при игре
        if count == 0:
            from settings import num

            game = Level(screen, num)
            count += 1
        bg_surf = pygame.transform.scale(background[num], (screen_width, screen_height))
        screen.blit(bg_surf, (0, 0))
        game.pause = False
        game.run()
        pause_button.update(screen)
    elif mode == 'exit':  # когда пользователь нажал 'exit' на главном экране
        count = 0
        running = False
    elif mode == 'pause':  # при паузу
        game.pause = True
        pause_menu.update(screen)
    elif mode == 'transition':  # при переходе на другой уровень
        transition_menu.update(screen, game.count_stars())
    elif mode == 'passed':  # при прохождении последнего уровня
        passed_menu.update(screen, game.count_stars())
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
