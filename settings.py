import pygame


def change_mode(value):
    global mode
    mode = value


pygame.mixer.init()

level_map = [
    'XX                                                                                                 XXXXXXXXXXXXXXXXX',
    'XXX    P                                                                     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XX                                    XX                                                    XXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XX                      s    XXX                                                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XX         XXX        XXX        X     X                                                               XXXXXXXXXXXXXXXXXXXXXX',
    'XX                      K  XX         XX                                                             XXXXXXXXXXXXXXXXXXXXX',
    'XX K   S        1  2    XXX    c    K XXX                                                              XXXXXXXXXXXXXXXXXXXXXX',
    'XXJJJJJJJJJJXXXXXXXXXXXXJJXXXXXXXXXXXXXXXXXXX    XXXX      XXXXXXXX     XXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XX                                                          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXJJJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

homescreen_map = [
    '',
    '  P',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    'XXXXXXXXXXXXXXXXXXX']
pygame.font.init()
tile_size = 64
screen_width = 1200
screen_height = len(homescreen_map) * tile_size
jump_speed = -15
screen = pygame.display.set_mode((screen_width, screen_height))
mode = 'home'
font = pygame.font.Font(None, 50)
volume = 1
