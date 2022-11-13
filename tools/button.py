# Path : tools/button.py

import pygame
import sys

import tools.config as config
import menu, build, simulation


class Button():
    def __init__(self, action, size, position, ac, ic, img, afc, ifc, text, font):
        self.screen = config.screen
        self.b_img = [pygame.Surface(size), pygame.Surface(size)]
        self.b_img[0].fill((ic))
        self.b_img[1].fill((ac))
        self.rect = pygame.Rect(position, size)
        self.index = 0

        self.image = img
        if img is not None:  # If there is an image
            self.image = pygame.image.load(img).convert_alpha()
            self.center_image = (self.image.get_rect()).center
            self.center_b_img = (self.rect.center[0]-self.center_image[0]), (self.rect.center[1]-self.center_image[1])

        self.text = text
        self.font = pygame.font.Font(font, 20)
        if text is not None:  # If there is text
            self.active_text = [(self.font.render(self.text, 1, ifc)), (self.font.render(self.text, 1, afc))]
            self.center_text = (self.active_text[0].get_rect()).center
            self.center_b_text = (self.rect.center[0]-self.center_text[0]), (self.rect.center[1]-self.center_text[1])
            
        self.action = action

    def draw(self):
        self.screen.blit(self.b_img[self.index], self.rect)
        if self.image is not None:
            self.screen.blit(self.image, (self.center_b_img))
        if self.text is not None:
            self.screen.blit(self.active_text[self.index], (self.center_b_text))

    def event_handler(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.index = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.action is not None:
                    exec(self.action)
        else: self.index = 0
