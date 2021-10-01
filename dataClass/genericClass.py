import pygame

from pygame.sprite import *


class GenericMouseLocation(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 1, 1)


class GenericUIObjectClass:
    def __init__(self, object, realPosX, realPosY, actionName):
        self.image = object
        self.rect = object.get_rect(topleft=(realPosX, realPosY))
        self.actionName = actionName
