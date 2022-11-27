# Path : play.py

import pygame
import sys
import sympy
import math

import tools.button as button
import tools.config as config
import menu, build, simulation

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
        "total": {
            "image": "src/image/falcon9_total.png",
            "seconds": 0,  # s
            "angle": 90,  # deg
            "thrust": 16947000,  # N
            "original mass": 521970,  # kg
            "mass": 521970,  # kg
            "length": 59,  # m
            "diameter": 5.2,  # m
            "isp": 311,  # s
            "propellant": 488370,  # kg
            "enthalpy": 1,  # J
            "h": 0,  # m
            "y": 0,  # m
            "burn time": 559,  # s
            "engine_status": True,

            "altitude": 0,
            "velocity": 0,
            "acceleration": 0
        }
    }

    simulation_screen()


def calculate(h_, y_):  # 윤서
    global rocket

    R = 8.31446261815324
    F = rocket["total"]["thrust"]
    original_M = rocket["total"]["original mass"]
    L = rocket["total"]["propellant"]
    angle = rocket["total"]["angle"]
    burn_time = rocket["total"]["burn time"]
    time = rocket["total"]["seconds"]

    q = L / burn_time
    m = original_M - time*q

    if m < original_M - L:
        m = original_M - L

    acceleration = -9.8 + (F - 0)/m
    velocity = acceleration * time

    h__ = ((-9.8 + (F - 0)/m) *math.cos(math.radians(math.sin(angle)))*600) 

    y__ = ((-9.8 + (F - 0)/m) *sympy.cos(angle)/60)
    y_ += y__ * time

    t, theta = sympy.symbols('t theta')

    if time >= burn_time:
        rocket["total"]["engine_status"] = False

    rocket["total"]["altitude"] = round(h_ + h__ - 13671.123978070842, 2)
    rocket["total"]["velocity"] = round(velocity, 2)
    rocket["total"]["acceleration"] = round(acceleration, 2)
    rocket["total"]["mass"] = round(m, 2)
    rocket["total"]["seconds"] = round(time, 2)
    rocket["total"]["angle"] = round(angle, 2)


def draw_rocket(part, rot):
    rocket_image = pygame.image.load(rocket[part]["image"])
    rocket_image = pygame.transform.scale(rocket_image, (int(rocket[part]["diameter"] * 5), int(rocket[part]["length"] * 5)))
    rocket_image = pygame.transform.rotate(rocket_image, rot)
    screen.blit(rocket_image, ((config.screen_w-rocket[part]["diameter"]*5)/2, (config.screen_h-rocket[part]["length"]*5)/2))


def draw_info():
    for i in rocket["total"].keys():
        if i != "image":
            text = pygame.font.Font("src/font/Montserrat-Regular.ttf", 20).render(f"{i} : {rocket['total'][i]}", True, config.BLACK)
            screen.blit(text, (10, 40 + 20 * list(rocket["total"].keys()).index(i)))


def simulation_screen():    
    while True:
        screen.fill(config.WHITE)
        rocket['total']["seconds"] = (pygame.time.get_ticks()-0) / 1000
        calculate(rocket['total']["h"], rocket['total']["y"])
        
        back_button.draw()
        draw_rocket("total", rocket["total"]["angle"]-90)
        draw_info()
        event_main()
        config.clock.tick(config.FPS)
        pygame.display.update()


def event_main():  # 민재
    x, y = 0, 0

    for event in pygame.event.get():
        back_button.event_handler(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        keys=pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            x += 1
        if keys[pygame.K_LEFT]:
            x -= 1

        rocket["total"]["angle"] += x
