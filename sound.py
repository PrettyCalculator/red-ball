import pygame
from functions import get_volume

pygame.mixer.init()


class Sound:
    def __init__(self):
        self.volume = get_volume()
        self.click_sound = pygame.mixer.Sound('data/sounds/click.wav')
        self.click_sound.set_volume(self.volume)

        self.background_sound = pygame.mixer.Sound('data/sounds/aria_math.wav')
        self.background_sound.set_volume(self.volume)

    def click(self):
        self.click_sound.play()

    def background(self):
        self.background_sound.play(-1)

    def update_volume(self):
        self.volume = get_volume()
        self.click_sound.set_volume(self.volume)
        self.background_sound.set_volume(self.volume)
