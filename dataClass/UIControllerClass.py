import sys
import pygame

from dataClass.genericClass import *
from dataClass.UI.UITextClass import UITextClass
from dataClass.UI.UIImageClass import UIImageClass
from dataClass.mouseControllerClass import *


class UIControllerClass:
    global UI_TEXT_LIST
    global UI_IMAGE_LIST

    global _mainFont

    global _UI_textController
    global _UI_ImageController
    global _MouseController

    def __init__(self, screen):
        self.UI_TEXT_LIST = []
        self.UI_IMAGE_LIST = []

        self._screen = screen

        self._mainFont = pygame.font.Font(
            sys.path[0] + "/media/fonts/ancient.ttf", 45)

        self._UI_textController = UITextClass(self._mainFont)
        self._UI_ImageController = UIImageClass()
        self._MouseController = MouseControllerClass()

        info = pygame.display.Info()
        self.screenW, self.screenH = info.current_w, info.current_h

    def update(self):
        pygame.display.update(self.UI_IMAGE_LIST)
        pygame.display.update(self.UI_TEXT_LIST)

    def checkMouseClick(self):
        if self.itemCollided:
            self._MouseController.onMouseClicked(self.itemCollided)

    def checkCollision(self):
        x, y = pygame.mouse.get_pos()
        mouse = GenericMouseLocation(x, y)

        index = 0
        searchFinished = False
        self.itemCollided = False  # set Later as the item collided

        while not searchFinished:
            if pygame.sprite.collide_rect(self.UI_TEXT_LIST[index], mouse):
                self.itemCollided = self.UI_TEXT_LIST[index]
                searchFinished = True
            else:
                index += 1

                if index > len(self.UI_TEXT_LIST) - 1:
                    searchFinished = True

        if not self.itemCollided:
            self.itemCollided = False

    def setBackgroundImage(self, imagePath):
        imageObject = self._UI_ImageController.createBackgroundImage(imagePath)
        self.UI_IMAGE_LIST.append(
            GenericUIObjectClass(imageObject, 0, 0, False))

        self._screen.blit(
            self.UI_IMAGE_LIST[len(self.UI_IMAGE_LIST) - 1].image, (0, 0))

    def drawText(self, text, action, offsetX, offsetY):
        textObject = self._UI_textController.createTextObject(text)
        posX, posY = self._UI_textController.getTextRealPosition(
            textObject, offsetX, offsetY)

        self.UI_TEXT_LIST.append(GenericUIObjectClass(
            textObject, posX, posY, action))
        self._screen.blit(
            self.UI_TEXT_LIST[len(self.UI_TEXT_LIST) - 1].image, (posX, posY))
