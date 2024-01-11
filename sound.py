import pygame
from functions import get_volume

pygame.mixer.init()


class Sound:  # класс для воспроизведения звуков
    def __init__(self):
        self.volume = get_volume()
        self.click_sound = pygame.mixer.Sound('data/sounds/click.wav')  # звук клика
        self.click_sound.set_volume(self.volume)

        self.background_sound = pygame.mixer.Sound('data/sounds/aria_math.wav')  # фоновая музыка
        self.background_sound.set_volume(self.volume)

    def click(self):  # воcпроизводит звук клика
        self.click_sound.play()

    def background(self):  # воcпроизводит фоновую музыку
        self.background_sound.play(-1)

    def update_volume(self):  # обновляет информацию о громкости звука из базы данных
        self.volume = get_volume()
        self.click_sound.set_volume(self.volume)
        self.background_sound.set_volume(self.volume)
