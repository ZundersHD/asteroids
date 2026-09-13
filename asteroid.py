import random
import pygame
from circleshape import *
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            log_event("asteroid_kill")
            return
        log_event("asteroid_split")
        rand_angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(rand_angle)
        new_vector2 = self.velocity.rotate(rand_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_vector1 * 1.2
        asteroid2.velocity = new_vector2 * 1.2

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt