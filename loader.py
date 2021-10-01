import pygame
from pygame.locals import *

from dataClass.windowManagerClass import WindowManagerClass
from common.static import *

wmc = {}


def mainMenuScreen():
    global screen

    wmc.setBackgroundImage("/media/main_menu_bg.png")
    # wmc.setButton("/media/GUI/mainMenu/section.png",
    #              "Lorem Ipsum", CFG_MAIN_MENU_BUTTON_WIDTH, CFG_MAIN_MENU_BUTTON_HEIGHT, 100, 100, True, False)

    canLoop = True

    while canLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                canLoop = False
           # elif event.type == MOUSEMOTION:
                # wmc.checkMouseCollitions()

        wmc.updateScreen()

    wmc.quitGame()


def loadingScreen():
    global wmc

    wmc = WindowManagerClass()
    wmc.setBackgroundImage("/media/first_loading.png")
    wmc.updateScreen()
    mainMenuScreen()


loadingScreen()
