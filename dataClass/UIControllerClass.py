import pygame


class UIControllerClass:
    global UI_TEXT_LIST

    global _screen

    def __init__(self, screen):
        self.UI_TEXT_LIST = []
        self._screen = screen

        info = pygame.display.Info()
        self.screenW, self.screenH = info.current_w, info.current_h

    def update(self):
        pygame.display.update()
