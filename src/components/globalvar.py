import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255,192,203)
LIGHTPINK = (255, 182, 193)
PALEPINK = (250, 218, 221)
# GAME_FONT = pygame.font.Font('freesansbold.ttf', 115)
scene_types = {"NORMAL": 0, "CHOICES": 1, "CUTSCENE": 2}
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

