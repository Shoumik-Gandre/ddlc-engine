import pygame
from . import globalvar


class Character:

    def __init__(self, screen, sprite, position=None):
        self.sprite = sprite
        self.screen = screen
        if position:
            self.position = position
        else:
            self.position = (0, screen.get_height())
        self.image = pygame.image.load(self.sprite)
        w, h = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (round(w / 1.5), round(h / 1.5)))

    def draw(self):
        char_pos = (self.position[0], self.position[1] - self.image.get_height())
        self.screen.blit(self.image, char_pos)


class DialogueBox:

    def __init__(self, screen, name, text, position="BOTTOM"):
        self.name = name
        self.text = text
        self.position = position
        self.height = 100
        self.name_height = 30
        self.name_width = 100
        self.screen = screen
        self.dbimg = pygame.image.load('assets/transparent-textbox.png')

    def draw(self):
        w, h = pygame.display.get_surface().get_size()
        h_text_start = h - self.dbimg.get_height()
        w_text_start = w // 2 - self.dbimg.get_width() // 2
        self.screen.blit(self.dbimg, (w_text_start, h_text_start))
        text = str(self.text)
        font = pygame.font.Font(pygame.font.get_default_font(), 18)
        text = font.render(text, True, globalvar.WHITE)
        self.screen.blit(text, (w_text_start + 20, h_text_start + 20))

        if self.name:
            h_name_start = h_text_start - self.name_height
            w_name_start = w_text_start
            pygame.draw.rect(self.screen, globalvar.PINK,
                             (w_name_start, h_name_start, self.name_width, self.name_height))
            text = str(self.name)
            font = pygame.font.Font(pygame.font.get_default_font(), 20)
            text = font.render(text, True, globalvar.WHITE)
            self.screen.blit(text, (w_name_start + 20, h_name_start + 5))


class ChoiceBox:

    def __init__(self, screen, choices):
        self.choices = choices
        self.selected_choice = 0
        self.screen = screen
        self.box_width = 400
        self.box_height = 50
        self.spacing = 50

    def draw(self):
        w, h = self.screen.get_size()
        num_choices = len(self.choices)
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        x_box = (w - self.box_width)//2
        y_box = h // (num_choices * 2)
        for i, choice in enumerate(self.choices):

            pygame.draw.rect(
                self.screen,
                globalvar.PALEPINK,
                (x_box , i * y_box + self.spacing,  self.box_width, self.box_height)
            )
            text = str(choice)
            text_len = len(text)
            text = font.render(text, True, globalvar.BLACK)
            self.screen.blit(text, (x_box + (x_box - text_len*10)//2, i * y_box + self.spacing))

        pygame.draw.rect(
            self.screen, globalvar.PINK,
            (x_box, self.selected_choice * y_box + self.spacing, self.box_width, self.box_height), 3
        )
