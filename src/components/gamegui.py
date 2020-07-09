import pygame
from . import globalvar


class Character:

    def __init__(self, screen, sprite, position):
        self.sprite = sprite
        self.screen = screen
        self.position = position

    def draw(self):
        self.screen.blit(pygame.image.load(self.sprite), self.position)


class DialogueBox:

    def __init__(self, screen, name, text, position="BOTTOM"):
        self.name = name
        self.text = text
        self.position = position
        self.height = 100
        self.name_height = 20
        self.name_width = 200
        self.screen = screen

    def draw(self):
        w, h = pygame.display.get_surface().get_size()
        h_text_start = h - self.height
        h_name_start = h_text_start - self.name_height
        pygame.draw.rect(self.screen, globalvar.LIGHTPINK, (0, h_text_start, w, self.height))
        pygame.draw.rect(self.screen, globalvar.PINK, (0, h_name_start, self.name_width, self.name_height))
        try:
            text = str(self.text)
            font = pygame.font.Font(pygame.font.get_default_font(), 16)
            text = font.render(text, True, globalvar.WHITE)
            self.screen.blit(text, (50, h - self.height + 10))

            text = str(self.name)
            font = pygame.font.Font(pygame.font.get_default_font(), 16)
            text = font.render(text, True, globalvar.WHITE)
            self.screen.blit(text, (10, h - self.height - self.name_height))
        except Exception as e:
            print(e)


class ChoiceBox:

    def __init__(self, screen, choices):
        self.choices = choices
        self.selected_choice = 0
        self.screen = screen

    def draw(self):
        w, h = self.screen.get_size()
        num_choices = len(self.choices)
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        for i, choice in enumerate(self.choices):
            pygame.draw.rect(self.screen, globalvar.PINK, (w / 2 - 50, i * (h / num_choices / 2) + 50, 100, 50))
            text = str(choice)
            text = font.render(text, True, globalvar.WHITE)
            self.screen.blit(text, (w / 2 - 50, i * (h / num_choices / 2) + 50))

        select_box_x = w / 2 - 50
        select_box_y = self.selected_choice * (h / num_choices / 2) + 50
        select_box_width = 100
        select_box_height = 50

        pygame.draw.rect(
            self.screen, globalvar.WHITE,
            (select_box_x, select_box_y, select_box_width, select_box_height), 5
        )
