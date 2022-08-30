import pygame as pg


def create_critter_dict(critter, x_speed, y_speed, color, alive):
    """Creates a dictionary about a critter object, then returns it"""
    critter_dict = {
        'critter': critter,
        'y_speed': y_speed,
        'x_speed': x_speed,
        'color': color,
        'alive': alive,
        }
    return critter_dict


def check_critter_collision(critter1, critter2):
    """Checks if two critters collide"""
    if critter1.colliderect(critter2) and critter1 != critter2:
        print("Critters have collided")
        return True


def remove_critter(critter):
    """If two critters collide, one of them gets removed"""

    critter['y_speed'] = 0
    critter['x_speed'] = 0
    critter['alive'] = False
    critter['critter'].update(10_000, 10_000, 1, 1)

    print("Done removing critter!")


def check_critter_color(critter1_color, critter2, list):
    """Checks to see if two critters are the same colors, returns True if they are"""
    for critter in list:
        if critter['critter'] == critter2:
            if critter['color'] != critter1_color:
                #  print("Colors don't match")
                return True

    return False
