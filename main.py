"""
Andrei Florea
Started on 8/28/2022
Life Simulator created using PyGame
"""
import pygame as pg
import movements as mv
import critters
import random

# Initializing pygame
pg.init()
pg.font.init()

# Defining colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (251, 255, 0)

# List of colors
colors = [YELLOW, BLUE, RED, GREEN]

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

# Initializing first time set up variable
first_time_setup = True

# Initializing amount of critters and a list for them to be in, along with list of random speeds
critter_dict_list = []
critter_rect_list = []
dead_critter_rect_list = []
AMOUNT_OF_CRITTERS = 50  # How many critters can spawn in the game

while game_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_running = False

    screen.fill(WHITE)

    if first_time_setup:
        for c in range(AMOUNT_OF_CRITTERS):  # Creating each critter object
            x_limit, y_limit = random.randrange(50, x - 50), random.randrange(50, y - 50)
            Critter = pg.Rect(x_limit, y_limit, 50, 50)  # Creates a critter object at a random location

            x_rect_speed = random.randrange(LOWER, UPPER)
            if x_rect_speed == 0:  # Ensures that the x_rect_speed won't be equal to 0
                print(f'X speed is {x_rect_speed}, resetting it.')
                while x_rect_speed == 0:
                    x_rect_speed = random.randrange(LOWER, UPPER)

            y_rect_speed = random.randrange(LOWER, UPPER)
            if y_rect_speed == 0:  # Ensures that the y_rect_speed won't be equal to 0
                print(f'Y speed is {x_rect_speed}, resetting it.')
                while y_rect_speed == 0:
                    y_rect_speed = random.randrange(LOWER, UPPER)

            current_critter = critters.create_critter_dict(Critter, y_rect_speed, x_rect_speed,
                                                           colors[random.randrange(0, 4)], True)
            critter_dict_list.append(current_critter)  # Stores the critter dictionary reference
            critter_rect_list.append(current_critter['critter'])  # Stores the raw critter Rect object

        first_time_setup = False

    for critter in critter_dict_list:

        if critter['alive']:
            pg.draw.rect(screen, critter['color'], critter['critter'])
            critter['critter'].move_ip(critter['x_speed'], critter['y_speed'])

        for c in critter_rect_list:  # Checks for any collision and if the colors of the critters aren't the same
            if critters.check_critter_collision(critter['critter'], c):
                if critters.check_critter_color(critter['color'], c, critter_dict_list):
                    critters.remove_critter(critter_dict_list[critter_dict_list.index(critter)])

                # dead_critter_rect_list.append(c)
                # critter_rect_list.remove(c)

        # Checks if the critter objects hit any of the borders, then switches their speed
        if critter['critter'].left < 0:
            critter['x_speed'] *= -1

        if critter['critter'].right > x:
            critter['x_speed'] *= -1

        if critter['critter'].top < 0:
            critter['y_speed'] *= -1

        if critter['critter'].bottom > y:
            critter['y_speed'] *= -1

    pg.display.flip()
    clock.tick(60)


pg.quit()
