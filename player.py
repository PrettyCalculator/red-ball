from functions import load_image
from settings import *


# отдельный файл для класса игрока
class Player(pygame.sprite.Sprite):
    frames_small, frames_big = [], []
    c = 0
    for i in range(25):  # который создает два списка с раскадровкой анимации мяча
        image = load_image(f's1 ({c}).png')
        image = pygame.transform.scale(image, (50, 50))
        frames_small.append(image)
        image = pygame.transform.scale(image, (80, 80))
        frames_big.append(image)
        c += 1

    def __init__(self, pos):
        super().__init__()
        self.delay = 0
        self.cur_frame = 0  # текущий кадр анимации
        self.frames = Player.frames_small  # список кадров
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)  # направление мяча в пространстве
        self.speed = 6
        self.gravity = 0.8
        self.jump_speed = -15
        self.is_jump = True
        self.is_double_jump = False
        self.is_big = False
        self.right_collide = False
        self.jump_key = False
        self.left_collide = False

    def get_input(self):  # функция, которая управляет мячом вследствие нажатия игроком на кнопки
        self.jump_key = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            if not self.right_collide:
                self.anim()
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            if not self.left_collide:
                self.anim()
        else:
            self.direction.x = 0
        if keys[pygame.K_UP] and not self.is_jump:
            if self.is_double_jump:
                self.jump_speed -= 2
            self.is_jump = True
            self.jump_key = True
        elif keys[pygame.K_UP]:
            self.jump_key = True

    def bunnyhop(self):  # функицая, которая делает еще несколько отскоков мяча после прыжка
        if self.jump_key:
            if self.is_double_jump:
                if self.jump_speed > -15:
                    self.jump_speed = -15
                self.jump_speed -= 2
                self.direction.y = self.jump_speed
            elif self.is_jump:
                self.jump_speed = -15
                self.direction.y = self.jump_speed
        elif self.is_jump:
            if self.jump_speed >= 0:
                self.direction.y = 0
                self.is_jump = False
                self.jump_speed = -15
            else:
                self.jump_speed += 5
                self.direction.y = self.jump_speed
        elif not self.is_jump:
            self.direction.y = 0

    def apply_gravity(self):  # добавление гравитации
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):  # прыжок
        self.jump_speed = -15
        self.direction.y = self.jump_speed

    def anim(self):  # функция, которая перемещает кадры в соответствии с направлением движения мяча
        if self.cur_frame == 24 and self.direction.x > 0:
            self.cur_frame = 0
        elif self.cur_frame == 0 and self.direction.x < 0:
            self.cur_frame = 24
        else:
            self.cur_frame += int(self.direction.x)
        if self.is_big:
            self.image = self.frames[self.cur_frame]
        else:
            self.image = self.frames[self.cur_frame]

    def change_size(self, value):  # функция, которая изменяет размер мяча
        x = self.rect.x
        y = self.rect.y
        if value:
            self.is_big = True
            self.frames = Player.frames_big
            self.rect = self.frames[0].get_rect()
            self.rect.x += x - 30
            self.rect.y += y - 30
            self.anim()
        else:
            self.is_big = False
            self.frames = Player.frames_small
            self.rect = self.frames[0].get_rect()
            self.rect.x += x + 30
            self.rect.y += y + 30
            self.anim()

    def update(self):  # обновление (вызывается в классе Level)
        self.get_input()
