import sqlite3
import os
from settings import *


def load_image(name, colorkey=None):
    initialization()
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def initialization():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))


def get_volume():
    con = sqlite3.connect('data/db/database.sqlite')
    value = con.cursor().execute(f"SELECT value FROM music").fetchall()[0][0]
    con.close()
    return value
