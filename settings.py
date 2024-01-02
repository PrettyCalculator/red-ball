import pygame


def change_mode(value):
    global mode
    mode = value


level_map = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXX                XX                                                                        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXX    P           XX2                                                   X    X              XXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXX    1 XXXXX     XXXX    XXXK                                         X   X  K   X           XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXX  XXXXXXXXX   XXX       XXXXXX          X   X                       X       X               XXXXXXXXXXXXXXXXXXXXXX',
    'XXXXX  XXX   XXX   XXXKKKK   XXXXXX       X          X                  X             X          XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX  XXX S XXX   XXXXXXX   X        X                  X             X        c                XXXXXXXXXXXXXXXXXXX                          ',
    'XXXXX  XXXXX XXX             X XXX                              KK    X         X        KK      XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX        XXX      2      XsXXXXJJX                        XXXXXXXXXXXXXXX        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXJJXXXXXXXXXJJJXXXX XXXJJXXXXXXXXX                             XXXXXXXXXX        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

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

tile_size = 64
screen_width = 1200
screen_height = len(homescreen_map) * tile_size
jump_speed = -15
screen = pygame.display.set_mode((screen_width, screen_height))
mode = 'home'
