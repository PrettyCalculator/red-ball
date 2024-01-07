import pygame


def change_mode(value):
    global mode
    mode = value


def change_num(value):
    global num
    num = value


level_map1 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXX            M   XX                                                                        XXXXXXXXXXXXXXXXXXXX',
    'XXXXX    P           XX2                                                   XK XX               XXXXXXXXXXXXXXXXXXXX',
    'XXXXX    1 XXXXX     XXXX    XXXK                                         XXX X  K   X         XXXXXXXXXXXXXXXXXXXX',
    'XXXXX  XXXXXXXXX   XXX       XXXXXX          X   X                       XXXX    X             XXXXXXXXXXXXXXXXXXXX',
    'XXXXX  XXX   XXX   XXXKKKK   XXXXXX       X          X                  XXXXX        X         XXXXXXXXXXXXXXXXXXXX',
    'XXXXX  XXXS  XXX   XXXXXXX   Xc       X                  X             XXXXXX     X                   XXXXXXXXXXXXX',
    'XXXXX  XXXXX XXX             XXXX                                  XXXXXXXMM   XX    K       K                DXXXX',
    'XXXXX        XXX             X     XXXXJJX                       KKXXXXXXXXXXXXXXX   X  s  XXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXJJXXXXXXXXXJJJXXXXXXXXJJXXXXXXXXXXXXX                       XXXXXXXXXXXXXXX        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
level_map2 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXX           XXXXXXs                                                          XXXXXXXXXXX',
    'XXXXXP          XXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXX                                          2 XXXXXXXXX',
    'XXXXXXXXXXXXXX  XXXXXXXXXX   XXXX     XXXXXXXXXXXXXXXXXXXXXXX                              XKXXKXXKX XXXXXXXXXXXXX',
    'XXXXXXXX        K S   XXXXX  XXXXX    XXXXXXXXXXXXXXXXXXXXXXX              111111        XXXXXXXXXXX XXXXXXXXXXXXX',
    'XXXXXXXX  XXXXXXXXXX  XXXX   XXXXXX   XXXXXXXXXXXXXXXXXXXXXXX             XXXXXXXXXX XXXXXXXXXXXXXXX XXXXXXXXXXXXX',
    'XXXXXXXX  XXXXXXXXXXX  XX  XXXXXXXX                                       XXXXXXXXXX XXXXXXXXXXXXXXX   XXXXXXXXXXX',
    'XXXXXXXX  XXXXXXXXXXXX    XXXXXXXXX                                       XXXXXXXXXX  XXXXXXXXXXXXXX   XXXXXXXXXXX',
    'XXXXXXXX                 XXXXXXXXXXD               K   K      XJJX   XJJX XXXXXXXXXXc XXXXXXXXXXXXXX           DX',
    'XXXXXXXXJJXXXXXXXXXXXXXXXXXXXXXXXXXXX  X X X X XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXJJXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
level_map3 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXX      M  M  M          XXXXX            XXXXXXXXXXX                                       XXXXXXXXXXX',
    'XXXXXP                    XXXXX          S XXXXXXXXXXXXXXXXXXXXXXXXXXX                                XXXXXXXXX',
    'XXXXX                                 XXXXXXXXXXX XXXXXXXXXXXXX',
    'XXXXXXXXXXLLXXXXXXX  XXXX   XXXXXX   XXXXXXXXXXXXXXXXXXXXXXX             XXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXX  XX  XXXXXXXX     s                                  XXXXXXXXXXXXXXXX',
    'XXXXX                             c      XXXXXXXX   XXXXXXXXXXX',
    'XXXXXm            X                                                                                     DXXXXXXXXXX',
    'XXXXXXXXJJXXXXXXXXXXXXXXXXXXXXXXXXXXX  X X X X XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXJJXXXXXXXXXXXXXXXXXXXXXXXXXXXX']


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
levels = [level_map1, level_map2, level_map3]
pygame.font.init()
tile_size = 64
screen_width = 1200
screen_height = len(homescreen_map) * tile_size
jump_speed = -15
screen = pygame.display.set_mode((screen_width, screen_height))
mode = 'home'
font = pygame.font.Font(None, 50)
volume = 1
num = 0
