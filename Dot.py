import random
import pygame
from math import atan2, sin, cos

class Dot:
    def __init__(self, width, height):
        self.radius = 10 #20
        self.pos_x = random.randint(self.radius, width - self.radius)
        self.pos_y = random.randint(self.radius, height - self.radius)
        angle = random.randrange(360)
        self.speed_x = cos(angle) * 3
        self.speed_y = sin(angle) * 3
        #self.speed_x = 3
        #self.speed_y = 3

    def move(self, width, height):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        # Rebotar en los bordes
        if self.pos_x - self.radius <= 0 or self.pos_x + self.radius >= width:
            self.speed_x = -self.speed_x
        if self.pos_y - self.radius <= 0 or self.pos_y + self.radius >= height:
            self.speed_y = -self.speed_y

    def check_collision(self, other_dot):
        dx = other_dot.pos_x - self.pos_x
        dy = other_dot.pos_y - self.pos_y
        distance = ((dx) ** 2 + (dy) ** 2) ** 0.5
        if 0 < distance <= self.radius + other_dot.radius:
            overlap = (self.radius + other_dot.radius) - distance
            angle = atan2(dy, dx)

        # Mover los puntos para evitar la superposición
            self.pos_x -= overlap * cos(angle) * 0.5
            self.pos_y -= overlap * sin(angle) * 0.5
            other_dot.pos_x += overlap * cos(angle) * 0.5
            other_dot.pos_y += overlap * sin(angle) * 0.5

        # Calcular las nuevas velocidades
            new_speed_self = ((self.speed_x * cos(angle) + self.speed_y * sin(angle)),
                          (self.speed_y * cos(angle) - self.speed_x * sin(angle)))
            new_speed_other = ((other_dot.speed_x * cos(angle) + other_dot.speed_y * sin(angle)),
                           (other_dot.speed_y * cos(angle) - other_dot.speed_x * sin(angle)))

            self.speed_x, self.speed_y = new_speed_other
            other_dot.speed_x, other_dot.speed_y = new_speed_self

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.pos_x, self.pos_y), self.radius)