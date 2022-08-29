"""
Andrei Florea
Started on 8/28/2022
Life Simulator created using PyGame
"""
import pygame as pg
import movements as mv
import random

# Initializing pygame
pg.init()
pg.font.init()

# Defining colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initializing screen
x, y = 1000, 800
SIZE = (x, y)
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Life Simulator by Andrei Florea")

game_running = True  # Main game loop variable
clock = pg.time.Clock()

# Initializing rect objects
Critter1 = pg.Rect(100, 100, 50, 50)
Critter2 = pg.Rect(200, 200, 50, 50)

# Initializing possible beginning speed of rect objects
LOWER = -2
UPPER = 2

# Initializing x, y movements for speed of rect objects
x_rect_speed, y_rect_speed = random.randrange(LOWER, UPPER), random.randrange(LOWER, UPPER)

while game_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_running = False

    screen.fill(WHITE)

    pg.draw.rect(screen, BLUE, Critter1)
    pg.draw.rect(screen, RED, Critter2)

    Critter1.move_ip(x_rect_speed, y_rect_speed)
    Critter2.move_ip(x_rect_speed, y_rect_speed)

    if Critter1.left < 0:
        x_rect_speed *= -1

    if Critter1.right > x:
        x_rect_speed *= -1

    if Critter1.top < 0:
        y_rect_speed *= -1

    if Critter1.bottom > y:
        y_rect_speed *= -1

    pg.display.flip()
    clock.tick(60)


pg.quit()
