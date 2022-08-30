import pygame as pg

pg.font.init()

BLACK = (0, 0, 0)
GRAY = (88, 88, 88)
WHITE = (255, 255, 255)

X_POS_TEXT = 915

left_outline_line = pg.Rect(900, 0, 10, 800)
gui_background = pg.Rect(910, 0, 190, 800)

font = pg.font.SysFont('Comic Sans MS', 12)


def draw_gui(screen):
    pg.draw.rect(screen, BLACK, left_outline_line)
    pg.draw.rect(screen, GRAY, gui_background)


def initialize_green_crit_count_text(green_critter_count):
    """Initializes the text and returns it, will be used in draw_text()"""
    green_critters_left_text = font.render(f'# of Green Critters: {green_critter_count}', True, WHITE)
    return green_critters_left_text


def initialize_blue_crit_count_text(blue_critter_count):
    """Initializes the text and returns it, will be used in draw_text()"""
    blue_critters_left_text = font.render(f'# of Blue Critters: {blue_critter_count}', True, WHITE)
    return blue_critters_left_text


def initialize_red_crit_count_text(red_critter_count):
    """Initializes the text and returns it, will be used in draw_text()"""
    red_critters_left_text = font.render(f'# of Red Critters: {red_critter_count}', True, WHITE)
    return red_critters_left_text


def initialize_yellow_crit_count_text(yellow_critter_count):
    """Initializes the text and returns it, will be used in draw_text()"""
    yellow_critters_left_text = font.render(f'# of Yellow Critters: {yellow_critter_count}', True, WHITE)
    return yellow_critters_left_text


def draw_text(screen, green_critters_left_text,
              blue_critters_left_text, red_critters_left_text,
              yellow_critters_left_text):
    """Draws text on screen for the GUI"""
    screen.blit(green_critters_left_text, (X_POS_TEXT, 25))
    screen.blit(blue_critters_left_text, (X_POS_TEXT, 75))
    screen.blit(red_critters_left_text, (X_POS_TEXT, 125))
    screen.blit(yellow_critters_left_text, (X_POS_TEXT, 175))


def display_amount_percentages():
    pass
