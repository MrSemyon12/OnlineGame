import pygame


class Player:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.circle = ((x, y), radius)
        self.step = 3

    def draw(self, window):
        pygame.draw.circle(window, self.color, *self.circle)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.step

        if keys[pygame.K_RIGHT]:
            self.x += self.step

        if keys[pygame.K_UP]:
            self.y -= self.step

        if keys[pygame.K_DOWN]:
            self.y += self.step

        self.update()

    def update(self):
        self.circle = ((self.x, self.y), self.radius)
