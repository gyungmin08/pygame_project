# Path : __init__.py

import pygame
import os

import menu

pygame.init()  # Initialize pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"  # Center the window
pygame.display.set_caption("TITLE")  # Set the window title

# Project Hermes
# Space Simulator
# Rocket Simulator
# Ares (or Mars)

if __name__ == "__main__":  # If this is the main file
    menu.init()  # Run the startup menu
