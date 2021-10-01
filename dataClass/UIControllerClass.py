import sys
import pygame

from pygame.sprite import *

from dataClass.UI.UITextClass import UITextClass
from dataClass.UI.UIImageClass import UIImageClass


class Sprite_Mouse_Location(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 1, 1)


class GenericUIObjectClass:
    def __init__(self, object, realPosX, realPosY):
        self.image = object
        self.rect = object.get_rect(topleft=(realPosX, realPosY))


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

    def checkCollision(self):
        x, y = pygame.mouse.get_pos()
        mouse = Sprite_Mouse_Location(x, y)

        index = 0
        searchFinished = False
        itemCollided = False  # set Later as the item collided

        while not searchFinished:
            if pygame.sprite.collide_rect(self.UI_TEXT_LIST[index], mouse):
                itemCollided = self.UI_TEXT_LIST[index]
                searchFinished = True
            else:
                index += 1

                if index > len(self.UI_TEXT_LIST) - 1:
                    searchFinished = True

        if itemCollided:
            print(itemCollided)

    def setBackgroundImage(self, imagePath):
        imageObject = self._UI_ImageController.createBackgroundImage(imagePath)
        self.UI_IMAGE_LIST.append(GenericUIObjectClass(imageObject, 0, 0))

        self._screen.blit(
            self.UI_IMAGE_LIST[len(self.UI_IMAGE_LIST) - 1].image, (0, 0))

    def drawText(self, text, action, offsetX, offsetY):
        textObject = self._UI_textController.createTextObject(text)
        posX, posY = self._UI_textController.getTextRealPosition(
            textObject, offsetX, offsetY)

        self.UI_TEXT_LIST.append(GenericUIObjectClass(textObject, posX, posY))
        self._screen.blit(
            self.UI_TEXT_LIST[len(self.UI_TEXT_LIST) - 1].image, (posX, posY))
