import pygame
from pygame.locals import *

from Vector import Vector


# statuses
STOP = 0
MOVE = 1
TURN_LEFT = 2
TURN_RIGHT = 3


class Game_Object:
    def __init__(self, coords=(0, 0), speed=(0, 0)):
        self.coords = Vector(coords)
        self.speed = Vector(speed)
        self.color = (250, 0, 0)
        self.acsel = Vector((0, 0))
        self.status = MOVE
        self.angle_speed = 0.1

    def event(self, event):
        """
        Обработка событий объектом
        """
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.status = TURN_LEFT
            elif event.key == K_RIGHT:
                self.status = TURN_RIGHT
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                self.status = MOVE
            elif event.key == K_RIGHT:
                self.status = MOVE

    def move(self):
        self.coords += self.speed

    def update(self):
        """
        Обновление состояния объкта (вызывается каждый кадр)
        """
        if self.status == TURN_LEFT:
            self.speed.rotate(self.angle_speed)
        elif self.status == TURN_RIGHT:
            self.speed.rotate(-self.angle_speed)
        self.move()

    def render(self, screen):
        pygame.draw.line(screen, self.color, (self.coords.as_point()), (self.coords + self.speed).as_point())


if __name__ == "__main__":
    from temp.PyMain import PyManMain

    mainWindow = PyManMain(800, 600)
    mainWindow.add_render_object(Game_Object((200, 120), (2, 2)))
    mainWindow.MainLoop()
