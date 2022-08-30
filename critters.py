GREEN = (0, 255, 0)
YELLOW = (251, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0 ,255)


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


def check_critter_color(critter1_color, critter2, critter_dict_list):
    """Checks to see if two critters are the same colors, returns True if they aren't"""
    for critter in critter_dict_list:
        if critter['critter'] == critter2:
            if critter['color'] != critter1_color:
                print(critter['color'])
                #  print("Colors don't match")
                return True

    return False


def get_amount_of_critters(critter_dict_list):
    green_count = 0
    blue_count = 0
    red_count = 0
    yellow_count = 0

    for crit in critter_dict_list:
        if crit['color'] == GREEN and crit['alive']:
            green_count += 1

        elif crit['color'] == BLUE and crit['alive']:
            blue_count += 1

        elif crit['color'] == RED and crit['alive']:
            red_count += 1

        elif crit['color'] == YELLOW and crit['alive']:
            yellow_count += 1

    return [green_count, blue_count, red_count, yellow_count]

