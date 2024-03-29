import pygame


def change_mode(value):  # функция, которая изменяет mode игры
    global mode
    mode = value


def change_num(value):  # изменяет индекс уровня
    global num
    num = value

# карты уровней
level_map1 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXX             XXXXXX                                                             XXXXXXXXXXXX',
    'XXXXXP          XXXXXXXXXX             XXXXXX      s                                                    2 XXXXXXXXXXXX',
    'XXXXXXXXXXXXXX  XXXXXXXXXX     XXX     XXXXXXXXXLXXXXLXXXXLXXX                              XKXXKXXKX  XXXXXXXXXXXXXXX',
    'XXXXXXXX        K S    XXX     XXXX    XXXXXXXXXXXXXXXXXXXXXXX              111111        XXXXXXXXXXX  XXXXXXXXXXXXXXX',
    'XXXXXXXX  XXXXXXXXXX   XXX     XXXXX   XXXXXXXXXXXXXXXXXXXXXXX             XXXXXXXXXX XXXXXXXXXXXXXXX  XXXXXXXXXXXXXXX',
    'XXXXXXXX  XXXXXXXXXXX       XJJXXXXX                                       XXXXXXXXXX XXXXXXXXXXXXXXX  XXXXXXXXXXXXXXX',
    'XXXXXXXX  XXXXXXXXXXXX     XXXXXXXXX                                       XXXXXXXXX   XXXXXXXXXXXXXX  XXXXXXXXXXXXXXX',
    'XXXXXXXX                  XXXXXXXXXX                K   K      XJJX K XJJX XXXXXXXXX c XXXXXXXXXXXXXX           DXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  X X X X XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXJJJXXXXXXXXXXXXXXJJXXXXXXXXXXXXXXX']

level_map2 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXX                XX                                                                        XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX                XX2                                                   XX XX               XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX  X PXXXXXX   M XXXX    XXXK                                         XXX XX K   X         XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX  X11XXXXXX   XXX       XXXXXX          X   X                       XXXX    X   s         XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX  XXXX  XXX   XXXKKKK   XXXXXX       X          X                  XXXXX        X         XXXXXXXXXXXXXXXXXXXXX',
    'XXXXX  XXXS  XXX   XXXXXXX   Xc                          X             XXXXXX     X     X            XXXXXXXXXXXXXXX',
    'XXXXX  XXXXX XXX             XXXX                             X    XXXXXXXXXX        K       K                DXXXXX',
    'XXXXX        XXX             X     XXXXJJX                       KKXXXXXXXXXXJJX     X     XXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXJJXXXXXXXXXJJJXXXXXXXXJJXXXXXXXXXXXXX                       XXXXXXXXXXXXXXX           XXXXXXXXXXXXXXXXXXXXXXXXX']

level_map3 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXX                     XXXXXXXX                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX        XXXXXXXXXX',
    'XXXXXP  M    M   M   M    XXXXXXXX                XXXXXXXXXXs               XXXXXXXXXXXXXXXXXXXXXXX      2 XXXXXXXXXX',
    'XXXXX                       XXXXXX     K  K   K   XXXXXXXXXXXXXXX                                       XXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXX  XXXX c XXXXXX   XXXXXXXXXXX  XXXXXXXXX                                             XXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXX   X    m              XX   K       K     111   K    K    K    K        XXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXX                  XXXXXXXXXXXXXXXXXX  XXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXJJXX  XXXXXXXXXXX',
    'XXXXX             X                  XS                             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  XXXXXXXXXXX',
    "XXXXXXXXXXXXXXXXXXXJJXXXLLXXXXLLXXJJXXXXXXXXXXXX         XXXXXXXXJJJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX       DXXXXX",
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX X X X X XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map4 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXX  P  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXX     XXXXXX               mXXX   M       XX    M    XX           XXX        XX                 XXXD XXXXXXXXXX',
    'XXXXX     XXXXXX                XXX                      XX            XX        XX             S   XXX  XXXXXXXXXX',
    'XXXXX     XXXXXX                XXX           s          XX            XX        XX                 XXX  XXXXXXXXXX',
    'XXXXX     XXXXXX   XXXXXX       XXX  XXXXXX  XXXX  XXX   XX       c    XX   XX   XX   XX       XX   XXX  XXXXXXXXXX',
    'XXXXX     XXXXXX   XXXXXX            XXXX     XX     X                 XX   XX        XX    XXKXX    XX  XXXXXXXXXX',
    'XXXXX              XXXXXX  K    K    XXXX  K         X          K  K        XX        XX    XXXXX            mXXXXX',
    "XXXXXK   K         XXXXXXXXXXXXXXXXJJXXXXXXXXXXXXJJXXXXXXXXXXXXXXXXXXXXXXXJJXXXXXXXXJJXXXXXXXXXXXXXXXXXJJXXXXXXXXXX",
    'XXXXXXXXXXXXXXXXXJJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map5 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXP     XXS  XXs        M             XXXXXXXXXLLLLLLLLLLLLLLLLLXXXX        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXX      XX   XX                       XXXXXXXXX                             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXX      XX   XX                       XXXXXXXXX                 mXXXX       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXX      XX   XX     M       M         XXXXXXXXXcm                XXXX    2  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXX      XX   XXJJXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXX      XX                                                                                        XXXXXXXXXXXXX',
    'XXXX                                                                        M      M       M        XXXXXXXXXXXXX',
    'XXXX                   111                                                                           DXXXXXXXXXXX',
    "XXXXXXXXXXXXJJJXXXXXXXXXXXXXXXXXXXXXJJJX   X   X   X   XX   X   XXXXXXXJJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    'XXXXXXXXJJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map6 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXP                  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXK  XX           XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXX  XXXXXXXXX    XXXXXXX     XXXXXXXXXXXXX                                                  XXXXXXXXXXXXXXX',
    'XXXXXXX  JXXXXXXXXX    XXX     M M     XXs        M    M                                          XXXXXXXXXXXXXXX',
    'XXXXXXX  XXXXXXXXXX    XXX             XX                   XX  XXXXXm                           mXXXXXXXXXXXXXXX',
    'XXXXXXX   XXXXXXXXX    XXX    XXXXX    XXX       XXX  XXX       XXXXXm                   m            M  XXXXXXXX',
    'XXXXXXX    XXXXXXXX    XXX    XXXXX                          K  XXXXX  XX    XX    XX    XX    XX        XXXXXXXX',
    'XXXXXXXJK SXXXXXXXX           XXXXX         JJ              XX  XXXXXc XX    XX    XX    XX    XXKK      DXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXJJJJXXXXXXXXXXXX  XX                  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

# карта главного экрана
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
levels = [level_map1, level_map2, level_map3, level_map4, level_map5, level_map6]  # список всех уровней
pygame.font.init()
tile_size = 64  # размер одного тайла
screen_width = 1200
screen_height = len(homescreen_map) * tile_size
jump_speed = -15
screen = pygame.display.set_mode((screen_width, screen_height))
mode = 'home'  # mode игры
font = pygame.font.Font(None, 50)  # шрифт
volume = 1
num = 0
