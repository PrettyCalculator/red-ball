import pygame
from functions import load_image


class Player(pygame.sprite.Sprite):
    frames_small, frames_big = [], []
    c = 0
    for i in range(25):
        image = load_image(f's1 ({c}).png')
        image = pygame.transform.scale(image, (50, 50))
        frames_small.append(image)
        c += 1
    c = 0
    for i in range(25):
        image = load_image(f's1 ({c}).png')
        image = pygame.transform.scale(image, (80, 80))
        frames_big.append(image)
        c += 1

    def __init__(self, pos):
        super().__init__()
        self.delay = 0
        self.cur_frame = 0
        self.frames = Player.frames_small
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 6
        self.gravity = 0.8
        self.jump_speed = -15
        self.is_jump = False
        self.is_double_jump = False
        self.is_big = False

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.anim(1)
            self.jump_speed = -15
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.anim(-1)
            self.jump_speed = -15
        else:
            self.direction.x = 0
        if keys[pygame.K_UP] and not self.is_jump:
            if self.is_double_jump:
                self.jump_speed -= 2
            self.is_jump = True
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def anim(self, direction):
        if self.cur_frame == 24 and direction > 0:
            self.cur_frame = 0
        elif self.cur_frame == 0 and direction < 0:
            self.cur_frame = 24
        else:
            self.cur_frame += direction
        if self.is_big:
            self.image = self.frames[self.cur_frame]
        else:
            self.image = self.frames[self.cur_frame]
        self.delay = 0

    def change_size(self, value):
        if value:
            self.is_big = True
            self.frames = Player.frames_big
            x = self.rect.x
            y = self.rect.y
            self.rect = self.frames[0].get_rect()
            self.rect.x += x - 30
            self.rect.y += y - 30

    def update(self):
        self.get_input()
