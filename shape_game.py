import pygame as pg
import sys

window_dimensions = (900, 650)
screen = pg.display.set_mode(window_dimensions)

x = 100
y = 100

player_rect = pg.Rect(x, y, 50, 50)

player_quits = False
screen_rect = screen.get_rect()
while not player_quits:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            player_quits = True

        pressed = pg.key.get_pressed()
        if pressed[pg.K_UP]:
            player_rect.y -= 30
        if pressed[pg.K_DOWN]:
            player_rect.y += 30
        if pressed[pg.K_LEFT]:
            player_rect.x -= 30
        if pressed[pg.K_RIGHT]:
            player_rect.x += 30

        player_rect.clamp_ip(screen_rect)
        screen.fill((0, 0, 0))
        pg.draw.rect(screen, (10, 200, 180), player_rect)

    pg.display.flip()

pg.quit()
sys.exit()