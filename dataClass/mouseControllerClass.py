import pygame


import sys
import pygame


class MouseControllerClass:
    global buttonClickSound

    def __init__(self):
        pygame.mixer.init()

        self.buttonClickSound = pygame.mixer.Sound(
            sys.path[0] + "/media/audio/main_menu/button_click.mp3")

    def onMouseClicked(self, item):
        print(item.actionName)
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(self.buttonClickSound)

        if item.actionName == "main_menu_sp_clicked":
            exit
            # see pygame.display.flip
            # Possible thing to do is to clear all texts and images and setup the right for the SP pre-game-menu
            # I need to create - in case - a folder for that and a common folder for the AI logic (future)
            # Note: SP and MP pre-game-menu are actualy the same, it just change what data pass to the server
            # SP: -> local server? So the logic will be the same even for MP, it just change what other ppl will do
            # Need an idea on what to display here
