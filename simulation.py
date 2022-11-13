# Path : play.py

import pygame
import sys

import tools.button as button
import tools.config as config
import menu, build, simulation

def init():
    global screen, back_button, rocket
    # pygame.init()
    screen = config.screen
    button_font_file = "srconfig/font/Montserrat-Regular.ttf"

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

    rocket = {
        "name": "Falcon 9",
        "stage": 2,
        "stage1": {
            "image": "src/img/rocket/falcon9_stage1.png",
            "thrust": 7607000,  # N
            "mass": 421300,  # kg
            "length": 41.2,  # m
            "diameter": 3.7,  # m
            "isp": 282,  # s
            "propellant": 395700,  # kg
            "burn time": 162  # s
        },
        "stage2": {
            "image": "src/img/rocket/falcon9_stage2.png",
            "thrust": 9340000,  # N
            "mass": 96570,  # kg
            "length": 13.8,  # m
            "diameter": 3.7,  # m
            "isp": 311,  # s
            "propellant": 92670,  # kg
            "burn time": 397  # s
        },
        "payload": {
            "image": "src/img/rocket/falcon9_payload.png",
            "mass": 22800,  # kg
            "length": 4.2,  # m
            "diameter": 5.2  # m
        },
        "total": {
            "image": "src/img/rocket/falcon9_total.png",
            "mass": 521970,  # kg
            "length": 59,  # m
            "diameter": 5.2  # m
        }
    }

    simulation_screen()


def draw_rocket():
    pass


def simulation_screen():
    screen.fill(config.WHITE)
    while True:
        back_button.draw()
        draw_rocket()
        event_main()
        config.clock.tick(config.FPS)
        pygame.display.update()

def event_main():
    for event in pygame.event.get():
        back_button.event_handler(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
