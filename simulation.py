# Path : play.py

import pygame
import sympy as sy
import sys

import tools.button as button
import tools.config as config
import menu, build, simulation, cal

def init():
    global screen, back_button, rocket
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

    rocket = {
        "name": "Falcon 9",
        "stage": 2,
        "seconds": 0,

        "stage1": {
            "image": "src/image/falcon9_stage1.png",
            "thrust": 7607000,  # N
            "mass": 421300,  # kg
            "length": 41.2,  # m
            "diameter": 3.7,  # m
            "isp": 282,  # s
            "propellant": 395700,  # kg
            "burn time": 162,  # s
            "engine_status": False
        },
        "stage2": {
            "image": "src/image/falcon9_stage2.png",
            "thrust": 9340000,  # N
            "mass": 96570,  # kg
            "length": 13.8,  # m
            "diameter": 3.7,  # m
            "isp": 311,  # s
            "propellant": 92670,  # kg
            "burn time": 397,  # s
            "engine_status": False
        },
        "payload": {
            "image": "src/image/falcon9_payload.png",
            "mass": 22800,  # kg
            "length": 4.2,  # m
            "diameter": 5.2  # m
        },
        "total": {  # 로켓 정보 저장 (김경민)
            "image": "src/image/falcon9_total.png",
            "angle": 0,  # deg
            "thrust": 16947000,  # N
            "mass": 521970,  # kg
            "length": 59,  # m
            "diameter": 5.2,  # m
            "isp": 311,  # s
            "propellant": 488370,  # kg
            "enthalpy": 1,  # J
            "burn time": 559,  # s
            "engine_status": True,

            "altitude": 0,
            "velocity": 0,
            "acceleration": 0
        }
    }

    simulation_screen()


def draw_rocket(part, rot):
    rocket_image = pygame.image.load(rocket[part]["image"])
    rocket_image = pygame.transform.scale(rocket_image, ( int(rocket[part]["diameter"] * 5), int(rocket[part]["length"] * 5)))
    rocket_image = pygame.transform.rotate(rocket_image, rot)
    screen.blit(rocket_image, ((config.screen_w-rocket[part]["diameter"]*5)/2, (config.screen_h-rocket[part]["length"]*5)/2))


def draw_info():
    text = f" \
    seconds: {rocket['seconds']}s \n \
    altitude: {rocket['total']['altitude']}m \n \
    angle: {rocket['total']['angle']}deg \n \
    acceleration: {rocket['total']['acceleration']}m/s^2 \n \
    mass: {rocket['total']['mass']}kg"

    text = pygame.font.Font("src/font/Montserrat-Regular.ttf", 20).render(text, True, config.BLACK)
    screen.blit(text, (0, 0))


def simulation_screen():
    while True:
        screen.fill(config.WHITE)
        
        rocket["seconds"] = (pygame.time.get_ticks()-0) / 1000
        calculated = cal.calculate(rocket["seconds"], rocket["total"]["thrust"], rocket["total"]["mass"], rocket["total"]["propellant"], rocket["total"]["enthalpy"], rocket["total"]["angle"])

        rocket["total"]["altitude"] = calculated[1]
        rocket["total"]["mass"] = calculated[2]
        rocket["total"]["acceleration"] = calculated[3]
        
        back_button.draw()
        draw_rocket("total", 0)
        draw_info()
        event_main()
        config.clock.tick(config.FPS)
        pygame.display.update()


def event_main():
    for event in pygame.event.get():
        back_button.event_handler(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
