import sys
from typing import Generic
import pygame

from dataClass.UI.UITextClass import UITextClass
from dataClass.UI.UIImageClass import UIImageClass


class GenericUIObjectClass:
    def __init__(self, object):
        self.image = object
        self.rect = object.get_rect()


class UIControllerClass:
    global UI_TEXT_LIST
    global UI_IMAGE_LIST

    global _mainFont

    global _UI_textController
    global _UI_ImageController

    def __init__(self, screen):
        self.UI_TEXT_LIST = []
        self.UI_IMAGE_LIST = []

        self._screen = screen

        self._mainFont = pygame.font.Font(
            sys.path[0] + "/media/fonts/ancient.ttf", 45)

        self._UI_textController = UITextClass(self._mainFont)
        self._UI_ImageController = UIImageClass()

        info = pygame.display.Info()
        self.screenW, self.screenH = info.current_w, info.current_h

    def update(self):
        pygame.display.update(self.UI_IMAGE_LIST)
        pygame.display.update(self.UI_TEXT_LIST)

    def setBackgroundImage(self, imagePath):
        imageObject = self._UI_ImageController.createBackgroundImage(imagePath)
        self.UI_IMAGE_LIST.append(GenericUIObjectClass(imageObject))

        self._screen.blit(
            self.UI_IMAGE_LIST[len(self.UI_IMAGE_LIST) - 1].image, (0, 0))

    def drawText(self, text, action, offsetX, offsetY):
        textObject = self._UI_textController.createTextObject(text)

        self.UI_TEXT_LIST.append(GenericUIObjectClass(textObject))
        self._screen.blit(
            self.UI_TEXT_LIST[len(self.UI_TEXT_LIST) - 1].image, (self._UI_textController.getTextRealPosition(
                textObject, offsetX, offsetY)))
