import pygame
from pygame.locals import *

from dataClass.windowManagerClass import WindowManagerClass
from common.static import *

wmc = {}


def mainMenuScreen():
    global screen

    wmc.UI_ControllerClass.setBackgroundImage("/media/main_menu_bg.png")

    wmc.UI_ControllerClass.drawText("Singleplayer", "main_menu_sp_clicked",
                                    CFG_MAIN_MENU_TEXT_START_GAME_SP_POS_X_PERCENT, CFG_MAIN_MENU_TEXT_START_GAME_SP_POS_Y_PERCENT, "primary")
    wmc.UI_ControllerClass.drawText("Multiplayer", "main_menu_mp_clicked",
                                    CFG_MAIN_MENU_TEXT_START_GAME_MP_POS_X_PERCENT, CFG_MAIN_MENU_TEXT_START_GAME_MP_POS_Y_PERCENT, "primary")
    wmc.UI_ControllerClass.drawText("Options", "main_menu_option_clicked",
                                    CFG_MAIN_MENU_TEXT_OPTIONS_POS_X_PERCENT, CFG_MAIN_MENU_TEXT_OPTIONS_POS_Y_PERCENT, "primary")

    canLoop = True

    while canLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                canLoop = False
            elif event.type == MOUSEMOTION:
                wmc.checkMouseCollitions()
            elif event.type == MOUSEBUTTONUP:
                wmc.checkMouseClick()

        wmc.updateScreen()

    wmc.quitGame()


def loadingScreen():
    global wmc

    wmc = WindowManagerClass()
    # wmc.UI_ControllerClass.setBackgroundImage("/media/first_loading.png")
    wmc.updateScreen()
    mainMenuScreen()


loadingScreen()
