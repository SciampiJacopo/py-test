import pygame

from pygame.sprite import *


class GenericMouseLocation(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 1, 1)


class GenericUIObjectClass:
    def __init__(self, object, realPosX, realPosY, actionName, offsetX, offsetY, text):
        self.image = object
        self.rect = object.get_rect(topleft=(realPosX, realPosY))
        self.posX = realPosX
        self.posY = realPosY
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.text = text
        self.actionName = actionName
