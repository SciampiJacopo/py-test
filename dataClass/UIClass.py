import sys
import pygame

from pygame.sprite import *
from common.static import *

import tkinter


class Sprite_Mouse_Location(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 1, 1)


class UiBlock:
    def __init__(self, image, id, type, attachEvent, posX, posY, width, height, imagePath, text):
        self.image = image
        self.rect = image.get_rect(topleft=(posX, posY))
        self.id = id
        self.type = type
        self.attachEvent = attachEvent
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.imagePath = imagePath
        self.text = text


class UIClass:
    _mainFont = {}
    _objectList = []
    _screen = {}

    _hasCollidedBefore = False

    def __init__(self, screen):
        self._screen = screen

        self._mainFont = pygame.font.Font(
            sys.path[0] + "/media/fonts/ancient.ttf", 35)

        info = pygame.display.Info()
        self.screenWidth, self.screenHeight = info.current_w, info.current_h

    def setImage(self, imagePath, width, height, posX, posY, screen):
        image = pygame.image.load(sys.path[0] + imagePath)
        image = pygame.transform.smoothscale(image, (width, height))

        self._objectList.append(
            UiBlock(image, len(self._objectList), "image", False, posX, posY, width, height, imagePath, ""))
        screen.blit(self._objectList[len(
            self._objectList) - 1].image, (posX, posY))

    def _restoreButtonThatAreOnOver(self):
        for item in self._objectList:
            if item.imagePath.endswith('-over.png'):
                newPath = item.imagePath.replace('-over.png', '.png')
                self.setButton(newPath, item.text, item.width, item.height,
                               item.posX, item.posY, self._screen, True)

                item = ""
                print("XD")
        self._objectList = [x for x in self._objectList if x]
        print(len(self._objectList))

    def _onButtonOver(self, item):
        newPath = item.imagePath.replace('.png', '-over.png')

        if not newPath.endswith('-over-over.png'):
            self.setButton(newPath, item.text, item.width, item.height,
                           item.posX, item.posY, self._screen, True)
            idx = [x.id for x in self._objectList].index(item.id)
            self._objectList.pop(idx)

    def checkCollitions(self):
        x, y = pygame.mouse.get_pos()
        mouse = Sprite_Mouse_Location(x, y)

        hasCollided = False

        for item in self._objectList:
            if pygame.sprite.collide_rect(item, mouse) and item.attachEvent and item.type == "text_button" and not self._hasCollidedBefore:
                self._hasCollidedBefore = True
                hasCollided = True

                self._onButtonOver(item)

        if (hasCollided == False):
            self._hasCollidedBefore = False
            self._restoreButtonThatAreOnOver()

    def setButton(self, imagePath, textString, width, height, posX, posY, screen, horizzontalCenter):
        # Add Text translation here
        text = self._mainFont.render(textString, 1, (255, 255, 255))
        text_rect = text.get_rect()

        if horizzontalCenter == True:
            posX = (self.screenWidth / 2) - (width / 2)
            posTextX = (self.screenWidth / 2) - (text_rect.width / 2)
        else:
            posTextX = posX + ((width / 2) - (text_rect.width / 2))

        posTextY = posY + ((height / 2) - (text_rect.height / 2)) - 25

        image = pygame.image.load(sys.path[0] + imagePath)
        image = pygame.transform.smoothscale(image, (width, height))

        self._objectList.append(
            UiBlock(image, len(self._objectList), "image", False, posX, posY, width, height, imagePath, textString))

        screen.blit(self._objectList[len(
            self._objectList) - 1].image, (posX, posY))

        self._objectList.append(
            UiBlock(text, len(self._objectList), "text_button", True, posX, posY, width, height, imagePath, textString))
        screen.blit(self._objectList[len(
            self._objectList) - 1].image, (posTextX, posTextY))
