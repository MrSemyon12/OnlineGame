import pygame

win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("client")

clientNumber = 0


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

        self.circle = ((self.x, self.y), self.radius)


def redraw_window(window, player):
    window.fill((255, 255, 255))
    player.draw(window)
    pygame.display.update()


def main():
    run = True
    p = Player(50, 50, 50, (0, 255, 0))
    clock = pygame.time.Clock()

    while run:

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redraw_window(win, p)


main()
