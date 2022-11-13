# Path : build.py

import pygame
import sys

import tools.button as button
import tools.config as config
import menu, build, simulation

def init():
    global screen, back_button
    # pygame.init()
    screen = config.screen

    back_button = button.Button(
        action="menu.init()",
        size=(40, 40),
        position=(0, 0),
        ac=config.GRAY,
        ic=config.BLACK,
        img=None,
        afc=config.WHITE,
        ifc=config.WHITE,
        text="<",
        font="src/font/Montserrat-Regular.ttf")

    build_screen()

def build_screen():
    screen.fill(config.WHITE)
    while True:
        back_button.draw()
        event_main()
        config.clock.tick(config.FPS)
        pygame.display.update()

def event_main():
    for event in pygame.event.get():
        back_button.event_handler(event)
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
