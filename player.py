import pygame
from functions import load_image


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = load_image('img2.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 6
        self.gravity = 0.8
        self.jump_speed = -15
        self.is_jump = False
        self.is_double_jump = False

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pygame.K_UP] and not self.is_jump:
            self.is_jump = True
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
