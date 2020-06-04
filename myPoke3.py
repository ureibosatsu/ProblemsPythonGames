# Poke The Dots Version 1
# This is a graphical game where two dots move around
# the screen, bouncing off the edges.

from uagame import Window
from pygame import QUIT, MOUSEBUTTONUP, Color
from pygame.time import Clock, get_ticks
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle
from random import randint

# User-defined functions


def main():
    window = create_window()
    game = create_game(window)
    play_game(game)
    window.close()


def create_window():
    # Create a window for the game, open it, and return it.

    window = Window('Poke the Dots', 500, 400)
    window.set_bg_color('black')
    window.set_font_color('white')
    window.set_font_name('calibri')
    window.set_font_size(64)
    return window


def create_game(window):
    game = Game(window, 90, False, Clock(), create_dot("red", 30, [50, 75], [1, 2], window),
                create_dot("blue", 40, [200, 100], [2, 1], window), 0)

    randomize_dot(game.small_dot)
    randomize_dot(game.big_dot)
    return game


def create_dot(color, radius, center, velocity, window):
    dot = Dot(color, radius, center, velocity, window)
    return dot


def play_game(game):
    while not game.close_selected:
        # play frame
        handle_events(game)
        draw_game(game)
        update_game(game)


def handle_events(game):
    # Handle the current game events. Return True if the player
    # clicked the close icon and False otherwise.
    event_list = get_events()
    for event in event_list:
        # handle one event
        if event.type == QUIT:
            game.close_selected = True
        elif event.type == MOUSEBUTTONUP:
            handle_mouse_up(game)


def handle_mouse_up(game):
    randomize_dot(game.small_dot)
    randomize_dot(game.big_dot)


def randomize_dot(dot):
    size = (dot.window.get_width(), dot.window.get_height())
    for index in range(0, 2):
        dot.center[index] = (randint(dot.radius, size[index] - dot.radius))


def draw_game(game):
    game.window.clear()
    draw_score(game)
    draw_dot(game.small_dot)
    draw_dot(game.big_dot)
    game.window.update()


def draw_score(game):
    string = "Score: " + str(game.score)
    game.window.draw_string(string, 0, 0)


def update_game(game):
    move_dot(game.small_dot)
    move_dot(game.big_dot)
    game.clock.tick(game.frame_rate)
    game.score = get_ticks() // 1000


def draw_dot(dot):
    surface = dot.window.get_surface()
    color = Color(dot.color)
    draw_circle(surface, color, dot.center, dot.radius)


def move_dot(dot):
    # Change the location and the velocity of the dot so it
    # remains on the surface by bouncing from its edges.

    size = (dot.window.get_width(), dot.window.get_height())
    for index in range(0, 2):
        # update center at coordinate
        dot.center[index] = dot.center[index] + dot.velocity[index]
        # dot edge outside window?
        if (dot.center[index] <= dot.radius) or (dot.center[index] + dot.radius >= size[index]):
            # change direction
            dot.velocity[index] = - dot.velocity[index]


class Game:
    #   an object in this class represents a complete game
    def __init__(self, window, frame_rate, close_selected, clock, small_dot, big_dot, score):
        self.window = window
        self.frame_rate = frame_rate
        self.close_selected = close_selected
        self.clock = clock
        self.small_dot = small_dot
        self.big_dot = big_dot
        self.score = score


class Dot:
    #   an object in this class represents a dot
    def __init__(self, color, radius, center, velocity, window):
        self.color = color
        self.radius = radius
        self.center = center
        self.velocity = velocity
        self.window = window


main()
