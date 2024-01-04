import pygame


def change_mode(value):
    global mode
    mode = value


level_map1 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXX                XX                                                                        XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX    P   D        XX2                                                   XK XX               XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX    1 XXXXX     XXXX    XXXK                                         XXX X  K   X         XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX  XXXXXXXXX   XXX       XXXXXX          X   X                       XXXX    X   K         XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX  XXX   XXX   XXXKKKK   XXXXXX       X          X                  XXXXX        X         XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX  XXX S XXX   XXXXXXX   X        X                  X             XXXXXX     X                   XXXXXXXXXXXXXX',
    'XXXXX  XXXXX XXX             X XXX                              KK    XXXXXXX   c XX   KK    KK                XXXX',
    'XXXXX        XXX             XsXXXXJJX                        XXXXXXXXXXXXXXX   X    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXJJXXXXXXXXXJJJXXXXXXXXJJXXXXXXXXX                        XXXXXXXXXXXXXXX        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
level_map2 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXXXXs                                                          XXXXXXXXXXX',
    'XXXXXP     D    XXXXXXXXXX   XX   XXXXXXXXXXXXXXXXXXXXXXXXXXX                                         2  XXXXXXXXX',
    'XXXXXXXXXXXXXX  XXXXXXXXXX  XXXX    XXXXXXXXXXXXXXXXXXXXXXXXX                              XKXXKXXKX XXXXXXXXXXXXX',
    'XXXXXXXX        K S   XXXXX  XXXXX    XXXXXXXXXXXXXXXXXXXXXXX              111111        XXXXXXXXXXX XXXXXXXXXXXXX',
    'XXXXXXXX  XXXXXXXXXX  XXXX   XXXXXX   XXXXXXXXXXXXXXXXXXXXXXX             XXXXXXXXXX XXXXXXXXXXXXXXX XXXXXXXXXXXXX',
    'XXXXXXXX  XXXXXXXXXXX  XX  XXXXXXXX                                       XXXXXXXXXX XXXXXXXXXXXXXXX   XXXXXXXXXXX',
    'XXXXXXXX  XXXXXXXXXXXX    XXXXXXXXX                                       XXXXXXXXXX  XXXXXXXXXXXXXX   XXXXXXXXXXX',
    'XXXXXXXX                 XXXXXXXXXX               K   K       XJJX   XJJX XXXXXXXXXXc XXXXXXXXXXXXXX            X',
    'XXXXXXXXJJXXXXXXXXXXXXXXXXXXXXXXXXXXX  X X X X XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXJJXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map3 = [
    '',
    '  P',
    '',
    '',
    '',
    '',
    '',
    '',
    '     D',
    'XXXXXXXXXXXXXXXXXXX']

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
levels = [level_map1, level_map2    ]
pygame.font.init()
tile_size = 64
screen_width = 1200
screen_height = len(homescreen_map) * tile_size
jump_speed = -15
screen = pygame.display.set_mode((screen_width, screen_height))
mode = 'home'
font = pygame.font.Font(None, 50)
volume = 1
