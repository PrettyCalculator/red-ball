from functions import *
from settings import *
from sound import Sound
import sqlite3


# файл для Pause и всех наследующихся от него классов
class Pause(pygame.sprite.Sprite):  # этот класс рисует кнопку паузы, которая находится в правом верхнем углу
    initialization()

    # размеры и позиция кнопок
    POS_SMALL = screen_width - 70, 10
    POS_BIG = screen_width - 90, 10

    SIZE_SMALL = 60, 60
    SIZE_BIG = 80, 80

    img = load_image('pause9.png')
    small = pygame.transform.scale(img, SIZE_SMALL)
    big = pygame.transform.scale(img, SIZE_BIG)

    def __init__(self):
        self.image = Pause.small
        self.size = Pause.SIZE_SMALL
        self.pos = Pause.POS_SMALL
        self.rect = self.image.get_rect(topleft=self.pos)
        self.focused = False  # True - на паузу наведена мышка, False - нет

    def change(self):  # функция для увеличения изображения кнопки при наведении, и наоборот
        if self.focused:
            self.image = Pause.big
            self.pos = Pause.POS_BIG
        else:
            self.image = Pause.small
            self.pos = Pause.POS_SMALL

    def get_focused(self, pos):  # функция для отслеживания коллайда курсора с кнопкой
        if self.rect.collidepoint(pos) and not self.focused:
            self.focused = True
            self.change()
        elif not self.rect.collidepoint(pos) and self.focused:
            self.focused = False
            self.change()

    def get_clicked(self):  # функция для того, чтобы поставить игру на паузу
        if self.focused:
            self.focused = False
            self.change()
            change_mode('pause')  # меняем game mode на 'pause'

    def update(self, screen):  # функция, которая рисует саму кнопку на экране
        screen.blit(self.image, self.pos)


class PauseMenu:  # класс, который рисует меню паузы(где можно изменить звук, выйти или продолжить игру)
    initialization()

    # все позиции (в наведенном и ненаведенном состоянии) и картинки кнопок
    surface_size = 600, screen_height // 2
    surface_pos = 300, (screen_height - (screen_height // 2)) // 2
    surface_image = pygame.transform.scale(load_image('pause_surface.jpg'), surface_size)

    exit_size = 50, 50  # кнопка выхода (которая с крестиком)
    exit_pos = 840, 170
    exit_pos_big = 820, 170
    exit_image = pygame.transform.scale(load_image('pause_exit.jpg'), exit_size)
    exit_image_big = pygame.transform.scale(exit_image, (exit_size[0] + 20, exit_size[1] + 20))

    resume_size = 300, 60  # кнопка 'resume' (возвращение в начало уровня)
    resume_pos = 450, 200
    resume_pos_big = 440, 190
    resume_image = pygame.transform.scale(load_image('resume.png'), resume_size)
    resume_image_big = pygame.transform.scale(load_image('resume.png'),
                                              (resume_size[0] + 20, resume_size[1] + 20))

    options_size = 300, 60  # кнопка 'options' (настройки)
    options_pos = 450, 280
    options_pos_big = 440, 270
    options_image = pygame.transform.scale(load_image('options.png'), options_size)
    options_image_big = pygame.transform.scale(load_image('options.png'),
                                               (options_size[0] + 20, options_size[1] + 20))

    exit2_size = 300, 60  # кнопка 'exit' (для выхода в главное меню)
    exit2_pos = 450, 360
    exit2_pos_big = 440, 350
    exit2_image = pygame.transform.scale(load_image('exit.png'), exit2_size)
    exit2_image_big = pygame.transform.scale(load_image('exit.png'), (exit2_size[0] + 20, exit2_size[1] + 20))

    value_image_0 = font.render("0%", True, pygame.Color('black'))  # текст для изменения звука
    value_image_35 = font.render("35%", True, pygame.Color('black'))
    value_image_75 = font.render("75%", True, pygame.Color('black'))
    value_image_100 = font.render("100%", True, pygame.Color('black'))

    def __init__(self):
        self.options = False  # False - меню с выбором действий (где 'resume', 'options' и т.д.), True - пользователь в настройках

        self.surface_size = PauseMenu.surface_size
        self.surface_pos = PauseMenu.surface_pos
        self.surface_image = PauseMenu.surface_image
        self.exit_image_rect = self.surface_image.get_rect(topleft=self.surface_pos)

        self.exit_size = PauseMenu.exit_size
        self.exit_pos = PauseMenu.exit_pos
        self.exit_image = PauseMenu.exit_image
        self.exit_image_rect = self.exit_image.get_rect(topleft=self.exit_pos)

        self.resume_size = PauseMenu.resume_size
        self.resume_pos = PauseMenu.resume_pos
        self.resume_image = PauseMenu.resume_image
        self.resume_image_rect = self.resume_image.get_rect(topleft=self.resume_pos)

        self.options_size = PauseMenu.options_size
        self.options_pos = PauseMenu.options_pos
        self.options_image = PauseMenu.options_image
        self.options_image_rect = self.resume_image.get_rect(topleft=self.options_pos)

        self.exit2_size = PauseMenu.exit2_size
        self.exit2_pos = PauseMenu.exit2_pos
        self.exit2_image = PauseMenu.exit2_image
        self.exit2_image_rect = self.resume_image.get_rect(topleft=self.exit2_pos)

        self.check_surface1_size = 70, 70
        self.check_surface1_pos = 370, 370
        self.check_surface1_image = pygame.transform.scale(load_image('check_surface.jpg'), self.check_surface1_size)
        self.check_surface1_image_rect = self.check_surface1_image.get_rect(topleft=self.check_surface1_pos)

        self.check_surface2_size = 70, 70
        self.check_surface2_pos = 493, 370
        self.check_surface2_image = pygame.transform.scale(load_image('check_surface.jpg'), self.check_surface2_size)
        self.check_surface2_image_rect = self.check_surface2_image.get_rect(topleft=self.check_surface2_pos)

        self.check_surface3_size = 70, 70
        self.check_surface3_pos = 636, 370
        self.check_surface3_image = pygame.transform.scale(load_image('check_surface.jpg'), self.check_surface3_size)
        self.check_surface3_image_rect = self.check_surface3_image.get_rect(topleft=self.check_surface3_pos)

        self.check_surface4_size = 70, 70
        self.check_surface4_pos = 759, 370
        self.check_surface4_image = pygame.transform.scale(load_image('check_surface.jpg'), self.check_surface4_size)
        self.check_surface4_image_rect = self.check_surface4_image.get_rect(topleft=self.check_surface4_pos)

        self.check_size = 70, 70
        self.check_pos = self.get_check_pos()
        self.check_image = pygame.transform.scale(load_image('check_mark.png', -1), self.check_size)
        self.check_image_rect = self.check_image.get_rect(topleft=self.check_pos)

        self.text_pos1 = 440, 270
        self.text_pos2 = 500, 370
        self.text_image = font.render("Громкость: ", True, pygame.Color('black'))

        self.value_pos1 = 640, 272
        self.value_pos2 = 770, 370
        self.value_image = self.get_value_image()

    def get_check_pos(self):  # функция, которая возвращает значение громкости из базы данных для постановки галочки в корректную ячейку
        con = sqlite3.connect('data/db/database.sqlite')
        value = con.cursor().execute('SELECT value FROM music').fetchall()[0][0]
        con.close()
        if value == 0:
            return self.check_surface1_pos
        if value == 0.35:
            return self.check_surface2_pos
        if value == 0.75:
            return self.check_surface3_pos
        if value == 1:
            return self.check_surface4_pos

    def get_value_image(self):  # функция для сопоставления громкости звука с надписью
        con = sqlite3.connect('data/db/database.sqlite')
        value = con.cursor().execute('SELECT value FROM music').fetchall()[0][0]
        con.close()
        if value == 0:
            return PauseMenu.value_image_0
        if value == 0.35:
            return PauseMenu.value_image_35
        if value == 0.75:
            return PauseMenu.value_image_75
        if value == 1:
            return PauseMenu.value_image_100

    def get_clicked(self, pos):  # функция для отслеживания кликов на различные кнопки
        if self.exit_image_rect.collidepoint(pos):
            change_mode('game')  # выходим обратно в игру, если пользователь нажал 'resume' или крестик в углу
            self.options = False
        elif self.resume_image_rect.collidepoint(pos):
            change_mode('game')
            return 'resume'
        elif self.options:  # если пользователь в настройках
            if self.check_surface1_image_rect.collidepoint(pos):  # установка громкости звука в соответствии с выбором пользователя
                self.check_pos = self.check_surface1_pos
                self.value_image = PauseMenu.value_image_0
                self.update_database(0.00)
                return 'volume'
            if self.check_surface2_image_rect.collidepoint(pos):
                self.check_pos = self.check_surface2_pos
                self.value_image = PauseMenu.value_image_35
                self.update_database(0.35)
                return 'volume'
            if self.check_surface3_image_rect.collidepoint(pos):
                self.check_pos = self.check_surface3_pos
                self.value_image = PauseMenu.value_image_75
                self.update_database(0.75)
                return 'volume'
            if self.check_surface4_image_rect.collidepoint(pos):
                self.check_pos = self.check_surface4_pos
                self.value_image = PauseMenu.value_image_100
                self.update_database(1.0)
                return 'volume'
        elif self.exit2_image_rect.collidepoint(pos):  # выход на главный экран
            change_mode('home')
            self.options = False
            return 'exit'
        else:
            self.options_image_rect.collidepoint(pos)  # если пользователь нажал на 'options'
            self.options = True

    def get_focused(self, pos):  # функция для изменения размера кнопок при наведении на них
        if self.exit_image_rect.collidepoint(pos):
            self.exit_image = PauseMenu.exit_image_big
            self.exit_pos = PauseMenu.exit_pos_big
        else:
            self.exit_image = PauseMenu.exit_image
            self.exit_pos = PauseMenu.exit_pos
        if self.resume_image_rect.collidepoint(pos):
            self.resume_image = PauseMenu.resume_image_big
            self.resume_pos = PauseMenu.resume_pos_big
        else:
            self.resume_image = PauseMenu.resume_image
            self.resume_pos = PauseMenu.resume_pos
        if self.options_image_rect.collidepoint(pos):
            self.options_image = PauseMenu.options_image_big
            self.options_pos = PauseMenu.options_pos_big
        else:
            self.options_image = PauseMenu.options_image
            self.options_pos = PauseMenu.options_pos
        if self.exit2_image_rect.collidepoint(pos):
            self.exit2_image = PauseMenu.exit2_image_big
            self.exit2_pos = PauseMenu.exit2_pos_big
        else:
            self.exit2_image = PauseMenu.exit2_image
            self.exit2_pos = PauseMenu.exit2_pos

    def update_database(self, value):  # функция обновления базы данных
        con = sqlite3.connect('data/db/database.sqlite')
        con.cursor().execute(f"UPDATE music SET value = {value}")
        con.commit()
        con.close()

    def update(self, screen):  # основная функция, которая рисует кнопки
        screen.blit(self.surface_image, self.surface_pos)
        screen.blit(self.exit_image, self.exit_pos)
        if not self.options:
            screen.blit(self.resume_image, self.resume_pos)
            screen.blit(self.options_image, self.options_pos)
            screen.blit(self.exit2_image, self.exit2_pos)
        else:
            screen.blit(self.check_surface1_image, self.check_surface1_pos)
            screen.blit(self.check_surface2_image, self.check_surface2_pos)
            screen.blit(self.check_surface3_image, self.check_surface3_pos)
            screen.blit(self.check_surface4_image, self.check_surface4_pos)
            screen.blit(self.check_image, self.check_pos)
            screen.blit(self.text_image, (self.text_pos1, self.text_pos2))
            screen.blit(self.value_image, (self.value_pos1, self.value_pos2))


# класс, который рисует меню между уровнями (когда игрок зашел в дверь)
class TransitionMenu(PauseMenu):
    resume_size = 300, 60
    resume_pos = 450, 280
    resume_pos_big = 440, 260
    resume_image = pygame.transform.scale(load_image('resume.png'), resume_size)
    resume_image_big = pygame.transform.scale(load_image('resume.png'),
                                              (resume_size[0] + 20, resume_size[1] + 20))

    def __init__(self):
        super().__init__()
        self.resume_pos = TransitionMenu.resume_pos  # позиция кнопки 'resume'
        self.resume_image = TransitionMenu.resume_image
        self.resume_image_rect = self.resume_image.get_rect(topleft=self.resume_pos)

        self.star_size = 80, 80  # позиция и картинки звезд
        self.star_white_image = pygame.transform.scale(load_image('star_white.png', -1), self.star_size)
        self.star_yellow_image = pygame.transform.scale(load_image('star.png', -1), self.star_size)
        self.star_pos = 450, 180

    def get_clicked(self, pos):  # функция, которая отслеживает клики на кнопки
        if self.resume_image_rect.collidepoint(pos):
            change_mode('game')
            return 'resume'
        elif self.exit2_image_rect.collidepoint(pos):
            change_mode('home')
            return 'exit'

    def get_focused(self, pos):  # функция, которая отслеживает наведение курсора на кнопки
        if self.resume_image_rect.collidepoint(pos):
            self.resume_image = TransitionMenu.resume_image_big
            self.resume_pos = TransitionMenu.resume_pos_big
        else:
            self.resume_image = TransitionMenu.resume_image
            self.resume_pos = TransitionMenu.resume_pos
        if self.exit2_image_rect.collidepoint(pos):
            self.exit2_image = PauseMenu.exit2_image_big
            self.exit2_pos = PauseMenu.exit2_pos_big
        else:
            self.exit2_image = PauseMenu.exit2_image
            self.exit2_pos = PauseMenu.exit2_pos

    def update(self, screen, count):  # основная функция, которая рисует все кнопки и собранные звезды
        screen.blit(self.surface_image, self.surface_pos)
        screen.blit(self.resume_image, self.resume_pos)
        screen.blit(self.exit2_image, self.exit2_pos)
        c = count
        step = 110
        for i in range(3):
            if c > 0:
                screen.blit(self.star_yellow_image, (self.star_pos[0] + step * i, self.star_pos[1]))
            else:
                screen.blit(self.star_white_image, (self.star_pos[0] + step * i, self.star_pos[1]))
            c -= 1


class PassedMenu(TransitionMenu):  # класс меню, который появляется при полном прохождении игры (при прохождении 6 уровня)
    def __init__(self):
        super().__init__()
        self.text_pos1 = 466, 290
        self.text_image = font.render("Игра пройдена! ", True, pygame.Color('black'))

    def get_clicked(self, pos):  # функция, которая отслеживает клики
        if self.exit2_image_rect.collidepoint(pos):
            change_mode('home')
            return 'exit'

    def get_focused(self, pos):  # функция, которая отслеживает наведения курора на кнопки и увеличивает или уменьшает их
        if self.exit2_image_rect.collidepoint(pos):
            self.exit2_image = PauseMenu.exit2_image_big
            self.exit2_pos = PauseMenu.exit2_pos_big
        else:
            self.exit2_image = PauseMenu.exit2_image
            self.exit2_pos = PauseMenu.exit2_pos

    def update(self, screen, count):  # основная функция, которая рисует все кнопки
        screen.blit(self.surface_image, self.surface_pos)
        screen.blit(self.exit2_image, self.exit2_pos)
        screen.blit(self.text_image, self.text_pos1)
        c = count
        step = 110
        for i in range(3):
            if c > 0:
                screen.blit(self.star_yellow_image, (self.star_pos[0] + step * i, self.star_pos[1]))
            else:
                screen.blit(self.star_white_image, (self.star_pos[0] + step * i, self.star_pos[1]))
            c -= 1
