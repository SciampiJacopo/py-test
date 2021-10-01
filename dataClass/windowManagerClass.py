import os
import pygame

from pygame.locals import *

from dataClass.settingsClass import GameSettingsClass
from dataClass.UIControllerClass import UIControllerClass


class WindowManagerClass:
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

        self.UI_ControllerClass = UIControllerClass(_screen)

    ### functions ###

    def updateScreen(self):
        self.UI_ControllerClass.update()

    def quitGame(self):
        pygame.quit()

    def checkMouseClick(self):
        self.UI_ControllerClass.checkMouseClick()

    def checkMouseCollitions(self):
        self.UI_ControllerClass.checkCollision()

    # def setButton(self, imagePath, text, w, h, posX, posY, horizzontalCenter, restored):
    #    _UiClass.setButton(imagePath, text, w, h, posX,
    #                       posY, _screen, horizzontalCenter, restored)
