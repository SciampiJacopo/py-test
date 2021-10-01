import sys
import pygame


class UIImageClass:
    def __init__(self):
        info = pygame.display.Info()

        self.screenW = info.current_w
        self.screenH = info.current_h

    def createBackgroundImage(self, imagePath):
        image = pygame.image.load(sys.path[0] + imagePath)
        image = pygame.transform.smoothscale(
            image, (self.screenW, self.screenH))

        return image
