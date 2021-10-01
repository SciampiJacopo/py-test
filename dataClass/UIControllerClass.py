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
        self.indexToDelete = False

        self._mainFont = pygame.font.Font(
            sys.path[0] + "/media/fonts/ancient.ttf", 45)

        self._UI_textController = UITextClass(self._mainFont)
        self._UI_ImageController = UIImageClass()
        self._MouseController = MouseControllerClass()

        info = pygame.display.Info()
        self.screenW, self.screenH = info.current_w, info.current_h

    def update(self):
        for item in self.UI_IMAGE_LIST:
            self._screen.blit(item.image, (item.posX, item.posY))

        for item in self.UI_TEXT_LIST:
            self._screen.blit(item.image, (item.posX, item.posY))

        pygame.display.update()

    def checkMouseClick(self):
        if self.itemCollided:
            self._MouseController.onMouseClicked(self.itemCollided)

    def checkCollision(self):
        x, y = pygame.mouse.get_pos()
        mouse = GenericMouseLocation(x, y)

        index = 0
        searchFinished = False
        self.itemCollided = False
        self.itemCollidedIndex = -1

        while not searchFinished:
            if pygame.sprite.collide_rect(self.UI_TEXT_LIST[index], mouse):
                self.itemCollided = self.UI_TEXT_LIST[index]
                self.itemCollidedIndex = index
                searchFinished = True
            else:
                index += 1

                if index > len(self.UI_TEXT_LIST) - 1:
                    searchFinished = True

        if not self.itemCollided and self.indexToDelete:
            self.UI_TEXT_LIST.pop(self.indexToDelete)

            item = self.prevStateObjectOvered
            self.drawText(item.text, item.actionName,
                          item.offsetX, item.offsetY, "primary")

            self.indexToDelete = False
            self.itemCollided = False
            self.prevStateObjectOvered = False

        elif self.itemCollided and not self.indexToDelete:
            self.prevStateObjectOvered = self.UI_TEXT_LIST[index]
            item = self.prevStateObjectOvered

            self.UI_TEXT_LIST.pop(index)

            self.drawText(item.text, item.actionName,
                          item.offsetX, item.offsetY, "over")

            self.indexToDelete = len(self.UI_TEXT_LIST) - 1

    def setBackgroundImage(self, imagePath):
        imageObject = self._UI_ImageController.createBackgroundImage(imagePath)
        self.UI_IMAGE_LIST.append(
            GenericUIObjectClass(imageObject, 0, 0, False, 0, 0, False))

        self._screen.blit(
            self.UI_IMAGE_LIST[len(self.UI_IMAGE_LIST) - 1].image, (0, 0))

    def drawText(self, text, action, offsetX, offsetY, color):
        textObject = self._UI_textController.createTextObject(text, color)
        posX, posY = self._UI_textController.getTextRealPosition(
            textObject, offsetX, offsetY)

        self.UI_TEXT_LIST.append(GenericUIObjectClass(
            textObject, posX, posY, action, offsetX, offsetY, text))
        self._screen.blit(
            self.UI_TEXT_LIST[len(self.UI_TEXT_LIST) - 1].image, (posX, posY))
