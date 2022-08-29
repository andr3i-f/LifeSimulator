def create_critter_dict(critter, x_speed, y_speed, color):
    """Creates a dictionary about a critter object, then returns it"""
    critter_dict = {
        'critter': critter,
        'y_speed': y_speed,
        'x_speed': x_speed,
        'color': color
        }
    return critter_dict

