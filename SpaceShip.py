import pygame
import sys
from Vector import Vector
from settings import *


NORMAL = 0
TURN_LEFT = 1
TURN_RIGHT = 2
SPEED_UP = 3
SPEED_DOWN = 4
ROTATION_ANGLE = 100


class SpaceShip:
    def __init__(self, coords):
        self.coords = Vector(coords)
        self.image = pygame.Surface((50, 40), pygame.SRCALPHA)
        self.speed = Vector((10, 0))
        self.boost = 1
        self.direction = self.speed
        self.state = NORMAL
        self.draw()

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.state = TURN_LEFT
            if event.key == pygame.K_RIGHT:
                self.state = TURN_RIGHT
            if event.key == pygame.K_UP:
                self.state = SPEED_UP
            if event.key == pygame.K_DOWN:
                self.state = SPEED_DOWN
        if event.type == pygame.KEYUP:
            self.state = NORMAL

    def update(self, delta_time):
        # Анализ состояния корабля
        if self.state == TURN_LEFT:
            self.speed.rotate(-ROTATION_ANGLE * (delta_time / 1000))
            if self.speed.len != 0:
                self.direction = self.speed
        if self.state == TURN_RIGHT:
            self.speed.rotate(ROTATION_ANGLE * (delta_time / 1000))
            if self.speed.len != 0:
                self.direction = self.speed
        if self.state == SPEED_UP:
            if self.speed.len != 0:
                self.direction = self.speed
                self.speed += self.speed.normalize() * self.boost
            else:
                self.speed = self.direction
        if self.state == SPEED_DOWN:
            if self.speed.len != 0:
                self.direction = self.speed
            self.speed -= self.speed.normalize() * self.boost
            if self.speed.len < self.boost:
                self.speed = Vector((0, 0))

        # Пересечение экрана
        if self.coords.x > RES_X:
            self.coords.x = -50
        if self.coords.y > RES_Y:
            self.coords.y = -50
        if self.coords.x < -50:
            self.coords.x = RES_X
        if self.coords.y < -50:
            self.coords.y = RES_Y

        self.coords += self.speed * (delta_time / 1000)

    def draw(self):
        pygame.draw.circle(self.image, (200, 0, 0), (20, 20), 20)
        pygame.draw.circle(self.image, (200, 150, 0), (40, 20), 10)
        # pygame.draw.rect(self.image, (0, 200, 0), self.image.get_rect(), 1)

    def render(self, screen):
        rotate_image = pygame.transform.rotate(self.image, self.direction.angle)
        rect = rotate_image.get_rect(center=self.image.get_rect().center)
        rect.move_ip(self.coords.as_point())
        screen.blit(rotate_image, rect)
        dv = Vector(self.image.get_rect().center)
        pygame.draw.line(screen, (0, 255, 0), (self.coords + dv).as_point(), (self.coords + self.speed + dv).as_point())


if __name__ == "__main__":
    pygame.init()
    display = pygame.display.set_mode((RES_X, RES_Y))
    screen = pygame.display.get_surface()

    ship = SpaceShip((120, 120))
    clock = pygame.time.Clock()

    while True:
        for e in pygame.event.get():
            ship.events(e)
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    sys.exit()

        delta_time = clock.tick(FPS)
        ship.update(delta_time)
        screen.fill(BACKGROUND_COLOR)
        ship.render(screen)
        pygame.display.flip()