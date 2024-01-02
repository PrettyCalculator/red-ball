import pygame

pygame.mixer.init()


class Sound:
    def __init__(self):
        self.click_sound = pygame.mixer.Sound('data/sounds/click.wav')
        self.background_sound = pygame.mixer.Sound('data/sounds/aria_math.wav')

    def click(self):
        self.click_sound.play()

    def background(self):
        self.background_sound.play(-1)
