import pygame, sys
from pygame.locals import *

FPS = 60


class PyManMain:
    """The Main PyMan Class - This class handles the main 
    initialization and creating of the Game."""

    def __init__(self, width=640, height=480):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.render_list = []

    def add_render_object(self, obj):
        self.render_list.append(obj)

    def MainLoop(self):
        """This is the Main Loop of the Game"""
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                for obj in self.render_list:
                    obj.event(event)
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0, 0, 0))
            for render_obj in self.render_list:
                render_obj.render(self.screen)
                render_obj.update()
            clock.tick(FPS)
            pygame.display.flip()


if __name__ == "__main__":
    mainWindow = PyManMain(800, 600)
    mainWindow.MainLoop()
