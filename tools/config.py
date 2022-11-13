# Path : tools/config.py

import pygame

screen_w = 800  # Screen width
screen_h = 600  # Screen height
screen = pygame.display.set_mode((screen_w, screen_h))

clock = pygame.time.Clock()

FPS = 60

WHITE = (255, 255, 255)  # (R, G, B)  # https://www.w3schools.com/colors/colors_picker.asp
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
L_BLUE = (0, 255, 255)
L_GREEN = (0, 255, 0)
L_RED = (255, 0, 0)
L_YELLOW = (255, 255, 0)
