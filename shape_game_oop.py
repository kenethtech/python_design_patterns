
import pygame as pg

class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pg.Rect(self.x, self.y, 50, 50)
        

    def draw(self, screen):
        raise NotImplementedError()

    def move(self, direction):
        if direction == "up":
            self.rect.y -= 30
        if direction == "down":
            self.rect.y += 30
        if direction == "left":
            self.rect.x -= 30
        if direction == "right":
            self.rect.x += 30

class Square(Shape):
    def draw(self, screen):
        pg.draw.rect(screen, (100, 150, 170), self.rect)

class Circle(Shape):
    def draw(self, screen):
        pg.draw.circle(screen, (0, 255, 0), self.rect.center, 25)


if __name__ == "__main__":
    window_dimensions = (800, 600)
    screen = pg.display.set_mode(window_dimensions)
    square = Square(100, 100)
    circle = Circle(250, 250)

    screen_rect = screen.get_rect()

    player_quits = False
    while not player_quits:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                player_quits = True

            pressed_square = pg.key.get_pressed()
            if pressed_square[pg.K_UP]:
                square.move("up") or circle.move("up")
            if pressed_square[pg.K_DOWN]:
                square.move("down") or circle.move("down")
            if pressed_square[pg.K_LEFT]:
                square.move("left") or circle.move("left")
            if pressed_square[pg.K_RIGHT]:
                square.move("right") or circle.move("right")

            square.rect.clamp_ip(screen_rect)
            circle.rect.clamp_ip(screen_rect)

            screen.fill((0, 0, 0))
            if pressed_square[pg.K_c]:
                circle.draw(screen)
            if pressed_square[pg.K_s]:
                square.draw(screen)

        pg.display.flip()
