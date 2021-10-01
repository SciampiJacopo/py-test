import pygame

from common.static import *


class UITextClass:
    global id
    global text
    global action

    def __init__(self, mainFont):
        self._mainFont = mainFont

        info = pygame.display.Info()
        self.screenW, self.screenH = info.current_w, info.current_h

    def createTextObject(self, text):
        return self._mainFont.render(text, 1, (255, 255, 255))

    def getTextRealPosition(self, text, offsetX, offsetY):
        text_rect = text.get_rect()

        factorX = 100 / offsetX
        factorY = 100 / offsetY

        posX = (self.screenW / factorX) - (text_rect.width / 2)
        posY = (self.screenH / factorY) - (text_rect.height / 2)

        return posX, posY
