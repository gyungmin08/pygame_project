# Path : __init__.py

import pygame
import os

import menu

pygame.init()  # Initialize pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"  # Center the window
pygame.display.set_caption("Project Hermes")  # Set the window title

if __name__ == "__main__":  # If this is the main file
    menu.init()  # Run the startup menu
