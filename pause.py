from functions import *
from settings import *
from sound import Sound


class Pause(pygame.sprite.Sprite):
    initialization()

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
        self.focused = False
        self.sound = Sound()

    def change(self):
        if self.focused:
            self.image = Pause.big
            self.pos = Pause.POS_BIG
        else:
            self.image = Pause.small
            self.pos = Pause.POS_SMALL

    def get_focused(self, pos):
        if self.rect.collidepoint(pos) and not self.focused:
            self.focused = True
            self.sound.click()
            self.change()
        elif not self.rect.collidepoint(pos) and self.focused:
            self.sound.click()
            self.focused = False
            self.change()

    def get_clicked(self):
        if self.focused:
            self.focused = False
            self.change()
            self.sound.click()
            change_mode('pause')

    def update(self, screen):
        screen.blit(self.image, self.pos)


class PauseMenu:
    initialization()

    surface_size = 600, screen_height // 2
    surface_pos = 300, (screen_height - (screen_height // 2)) // 2
    surface_image = pygame.transform.scale(load_image('pause_surface.jpg'), surface_size)

    exit_size = 50, 50
    exit_pos = 840, 170
    exit_pos_big = 820, 170
    exit_image = pygame.transform.scale(load_image('pause_exit.jpg'), exit_size)
    exit_image_big = pygame.transform.scale(exit_image, (exit_size[0] + 20, exit_size[1] + 20))

    resume_size = 300, 60
    resume_pos = 450, 200
    resume_pos_big = 440, 190
    resume_image = pygame.transform.scale(load_image('pause_resume.jpg'), resume_size)
    resume_image_big = pygame.transform.scale(load_image('pause_resume.jpg'),
                                              (resume_size[0] + 20, resume_size[1] + 20))

    options_size = 300, 60
    options_pos = 450, 280
    options_pos_big = 440, 270
    options_image = pygame.transform.scale(load_image('pause_options.jpg'), options_size)
    options_image_big = pygame.transform.scale(load_image('pause_options.jpg'),
                                               (options_size[0] + 20, options_size[1] + 20))

    exit2_size = 300, 60
    exit2_pos = 450, 360
    exit2_pos_big = 440, 350
    exit2_image = pygame.transform.scale(load_image('pause_exit2.jpg'), exit2_size)
    exit2_image_big = pygame.transform.scale(load_image('pause_exit2.jpg'), (exit2_size[0] + 20, exit2_size[1] + 20))

    value_image_0 = font.render("0%", True, pygame.Color('black'))
    value_image_25 = font.render("25%", True, pygame.Color('black'))
    value_image_75 = font.render("75%", True, pygame.Color('black'))
    value_image_100 = font.render("100%", True, pygame.Color('black'))

    def __init__(self):
        self.options = False
        self.sound = Sound()

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
        self.check_pos = self.check_surface4_pos
        self.check_image = pygame.transform.scale(load_image('check_mark.png', -1), self.check_size)
        self.check_image_rect = self.check_image.get_rect(topleft=self.check_pos)

        self.text_pos1 = 440, 270
        self.text_pos2 = 500, 370
        self.text_image = font.render("Громкость: ", True, pygame.Color('black'))

        self.value_pos1 = 640, 272
        self.value_pos2 = 770, 370
        self.value_image = PauseMenu.value_image_100

    def get_clicked(self, pos):
        if self.exit_image_rect.collidepoint(pos) or self.resume_image_rect.collidepoint(pos):
            change_mode('game')
            self.options = False
            self.sound.click()
        elif self.options:
            if self.check_surface1_image_rect.collidepoint(pos):
                self.check_pos = self.check_surface1_pos
                self.sound.click()
                self.sound.click_sound.set_volume(0)
                self.value_image = PauseMenu.value_image_0
                return 0.01
            if self.check_surface2_image_rect.collidepoint(pos):
                self.check_pos = self.check_surface2_pos
                self.sound.click()
                self.sound.click_sound.set_volume(0.25)
                self.value_image = PauseMenu.value_image_25
                return 0.25
            if self.check_surface3_image_rect.collidepoint(pos):
                self.check_pos = self.check_surface3_pos
                self.sound.click()
                self.sound.click_sound.set_volume(0.7)
                self.value_image = PauseMenu.value_image_75
                return 0.75
            if self.check_surface4_image_rect.collidepoint(pos):
                self.check_pos = self.check_surface4_pos
                self.sound.click()
                self.sound.click_sound.set_volume(1.0)
                self.value_image = PauseMenu.value_image_100
                return 1
        else:
            if self.exit2_image_rect.collidepoint(pos):
                change_mode('home')
                self.options = False
                self.sound.click()
            elif self.options_image_rect.collidepoint(pos):
                self.options = True
                self.sound.click()

    def get_focused(self, pos):
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

    def update(self, screen):
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
