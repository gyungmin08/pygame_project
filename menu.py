# Path : menu.py

import pygame
import sys

import tools.button as button
import tools.config as config
import menu, build, simulation

def init():
    global screen, button_position_x, button_position_y, build_button, play_button, quit_button
    pygame.init()
    screen = config.screen
    button_position_x = config.screen_w * 0.4
    button_position_y = [config.screen_h * 0.30, config.screen_h * 0.50, config.screen_h * 0.70]

    build_button = button.Button(
        action="build.init()",
        size=(140, 40),
        position=(button_position_x, button_position_y[0]),
        ac=config.GRAY,
        ic=config.BLACK,
        img=None,
        afc=config.WHITE,
        ifc=config.WHITE,
        text="Build",
        font="src/font/Montserrat-Regular.ttf")

    play_button = button.Button(
        action="simulation.init()",
        size=(140, 40),
        position=(button_position_x, button_position_y[1]),
        ac=config.GRAY,
        ic=config.BLACK,
        img=None,
        afc=config.WHITE,
        ifc=config.WHITE,
        text="Play",
        font="src/font/Montserrat-Regular.ttf")

    quit_button = button.Button(
        action="pygame.quit(), sys.exit()",
        size=(140, 40),
        position=(button_position_x, button_position_y[2]),
        ac=config.GRAY,
        ic=config.BLACK,
        img=None,
        afc=config.WHITE,
        ifc=config.WHITE,
        text="Quit",
        font="src/font/Montserrat-Regular.ttf")

    menu_screen()

def menu_screen():
    screen.fill(config.WHITE)
    while True:
        build_button.draw()
        play_button.draw()
        quit_button.draw()
        event_main()
        config.clock.tick(config.FPS)
        pygame.display.update()

def event_main():
    for event in pygame.event.get():
        build_button.event_handler(event)
        play_button.event_handler(event)
        quit_button.event_handler(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
