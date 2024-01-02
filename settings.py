import pygame


def change_mode(value):
    global mode
    mode = value


level_map = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXX                XX                                                                        XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX    P           XX2                                                   XK  X               XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX    1 XXXXX     XXXX    XXXK                                         XXX X  K   X         XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX  XXXXXXXXX   XXX       XXXXXX          X   X                       XXXX    X   K         XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX  XXX   XXX   XXXKKKK   XXXXXX       X          X                  XXXXX        X         XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX  XXX S XXX   XXXXXXX   X        X                  X             XXXXXX     X                   XXXXXXXXXXXXXX',
    'XXXXX  XXXXX XXX             X XXX                              KK    XXXXXXX   c  X   KK     KK      XXXXXXXXXXXXXX',
    'XXXXX        XXX             XsXXXXJJX                        XXXXXXXXXXXXXXX   X    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXJJXXXXXXXXXJJJXXXXXXXXJJXXXXXXXXX                        XXXXXXXXXXXXXXX        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

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
