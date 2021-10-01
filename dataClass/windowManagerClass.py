import os
import pygame

from pygame.locals import *
from dataClass.settingsClass import GameSettingsClass
from dataClass.UIClass import UIClass


class WindowManagerClass:
    _screen = {}
    _settings = {}
    _UiClass = {}

    def __init__(self):
        global _screen
        global _settings
        global _UiClass

        os.environ['SDL_VIDEO_CENTERED'] = '1'
        _settings = GameSettingsClass().getSettings()

        pygame.init()
        info = pygame.display.Info()
        maxScreenWidthForNoFrame, maxScreenHeightForNoFrame = info.current_w, info.current_h

        CLIENT_SCREEN_MODE = pygame.FULLSCREEN

        if _settings["CLIENT_TYPE"] == "NOFRAME":
            CLIENT_SCREEN_MODE = pygame.NOFRAME
            _settings["CLIENT_WIDTH"] = maxScreenWidthForNoFrame
            _settings["CLIENT_HEIGHT"] = maxScreenHeightForNoFrame

        _screen = pygame.display.set_mode(
            (_settings["CLIENT_WIDTH"], _settings["CLIENT_HEIGHT"]), CLIENT_SCREEN_MODE)

        _UiClass = UIClass(_screen)

    ### functions ###
    def getScreen(self):
        return _screen

    def updateScreen(self):
        pygame.display.update(_UiClass._objectList)

    def quitGame(self):
        pygame.quit()

    def checkMouseCollitions(self):
        _UiClass.checkCollitions()

    def setButton(self, imagePath, text, w, h, posX, posY, horizzontalCenter):
        _UiClass.setButton(imagePath, text, w, h, posX,
                           posY, _screen, horizzontalCenter)

    def setBackgroundImage(self, imagePath):
        _UiClass.setImage(
            imagePath, _settings["CLIENT_WIDTH"], _settings["CLIENT_HEIGHT"], 0, 0, _screen)
