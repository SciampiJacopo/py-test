import sys
import pygame


class UIImageClass:
    global _screen

    def __init__(self, screen):
        self._screen = screen

        info = pygame.display.Info()
        self.screenW, self.screenH = info.current_w, info.current_h

    def setBackgroundImage(self, imagePath):
        image = pygame.image.load(sys.path[0] + imagePath)
        image = pygame.transform.smoothscale(
            image, (self.screenW, self.screenH))

        self._screen.blit(image, (0, 0))
