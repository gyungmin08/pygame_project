# Path: cal.py

import sympy
import tools.config as config


def calculate(t, thrust, mass, load, enthalpy, angle):
    global M, q, F, theta, sangwoo

    a, b = sympy.symbols('a b')
    R=8.31446261815324
    x = sympy.symbols('x')

    F = sympy.symbols('F')
    F = thrust
    q = sympy.symbols('q')
    M = sympy.symbols('M')
    M = mass
    L = sympy.symbols('L')
    L = load
    H = sympy.symbols('H')
    H = enthalpy
    theta = angle
    q = (F*R*M*L) / H
    
    sangwoo = [y(t, theta), h(t, theta), m(t), acceleration(t)]

    if t >= None:  # 정의해주기
        sangwoo.clear()

    return sangwoo


def m(t):
    return M - t*q

def acceleration(t):
    resistance = 0  # 임의의 값으로 설정
    return -9.8 + (F-resistance)/m(t)

def h(t, theta):
    if theta == 0:
        return sympy.Integral(acceleration(t) * t)
    return sympy.Integral(acceleration(t) *sympy.cos(theta)*t**(2))

def y(t, theta):
    if theta == 0:
        return sympy.Integral(acceleration(t) * t**(2))
    return sympy.Integral(acceleration(t) *sympy.sin(theta)*t**(2))
