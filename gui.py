import pygame as pg

pg.font.init()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (251, 255, 0)
BLACK = (0, 0, 0)
GRAY = (88, 88, 88)

X_POS_TEXT = 915

left_outline_line = pg.Rect(900, 0, 10, 800)
gui_background = pg.Rect(910, 0, 190, 800)
gui_main_amount_percent = pg.Rect(950, 450, 100, 300)

font = pg.font.SysFont('Comic Sans MS', 12)


def draw_gui(screen):
    pg.draw.rect(screen, BLACK, left_outline_line)
    pg.draw.rect(screen, GRAY, gui_background)
    pg.draw.rect(screen, BLACK, gui_main_amount_percent)


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


def create_pixel_amount_percentage(color_amount, total_critters_alive, pixels=300):
    """This will return the amount of pixels each color amount should take up"""
    percentage = float(color_amount / total_critters_alive)
    # print(f"percentage is = {percentage}")
    return percentage * pixels


def create_pixel_actual_amount(amount_of_crit, total_crit_alive):
    """This creates and returns the amount of pixels for each bar"""
    green_pixel_amount = int(create_pixel_amount_percentage(amount_of_crit[0],
                                                            total_crit_alive))
    blue_pixel_amount = int(create_pixel_amount_percentage(amount_of_crit[1],
                                                           total_crit_alive))
    red_pixel_amount = int(create_pixel_amount_percentage(amount_of_crit[2],
                                                          total_crit_alive))
    yellow_pixel_amount = int(create_pixel_amount_percentage(amount_of_crit[3],
                                                             total_crit_alive))

    return [green_pixel_amount, blue_pixel_amount, red_pixel_amount, yellow_pixel_amount]


def create_ratio_display_rect(green_pixel_amount, blue_pixel_amount,
                              red_pixel_amount, yellow_pixel_amount):
    """This creates and returns the initial Rect for the ratio display"""
    green_bar = pg.Rect(950, 450, 100, green_pixel_amount)
    blue_bar = pg.Rect(950, 450+green_pixel_amount, 100, blue_pixel_amount)
    red_bar = pg.Rect(950, 450+blue_pixel_amount+green_pixel_amount, 100, red_pixel_amount)
    yellow_bar = pg.Rect(950, 450+red_pixel_amount+blue_pixel_amount+green_pixel_amount, 100, yellow_pixel_amount)

    return [green_bar, blue_bar, red_bar, yellow_bar]


def display_amount_percentages(screen, bar_list):
    """This will draw the ratio bars on screen"""
    pg.draw.rect(screen, GREEN, bar_list[0])
    pg.draw.rect(screen, BLUE, bar_list[1])
    pg.draw.rect(screen, RED, bar_list[2])
    pg.draw.rect(screen, YELLOW, bar_list[3])


def update_amount_percentages(screen, bar_list, color_px_list):
    bar_list[0].update(950, 450, 100, color_px_list[0])
    bar_list[1].update(950, 450+color_px_list[0], 100, color_px_list[1])
    bar_list[2].update(950, 450+color_px_list[0]+color_px_list[1], 100, color_px_list[2])
    bar_list[3].update(950, 450+color_px_list[0]+color_px_list[1]+color_px_list[2], 100, color_px_list[3])


