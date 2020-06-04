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
    game = Game()
    game.play_game()


class Game:
    #   an object in this class represents a complete game
    def __init__(self):
        self._window = Window('Poke the Dots', 500, 400)
        self._adjust_window()
        self._frame_rate = 90
        self._close_selected = False
        self._clock = Clock()
        self._small_dot = Dot('red', 30, [50, 75], [1, 2], self._window)
        self._big_dot = Dot('blue', 40, [200, 100], [2, 1], self._window)
        self._small_dot.randomize_dot()
        self._big_dot.randomize_dot()
        self._score = 0

    def _adjust_window(self):
        self._window.set_bg_color('black')
        self._window.set_font_color('white')
        self._window.set_font_name('calibri')
        self._window.set_font_size(64)

    def draw_game(self):
        self._window.clear()
        self.draw_score()
        self._small_dot.draw_dot()
        self._big_dot.draw_dot()
        self._window.update()

    def play_game(self):
        while not self._close_selected:
            # play frame
            self.handle_events()
            self.draw_game()
            self.update_game()
        self._window.close()

    def update_game(self):
        self._small_dot.move_dot()
        self._big_dot.move_dot()
        self._clock.tick(self._frame_rate)
        self._score = get_ticks() // 1000

    def draw_score(self):
        string = "Score: " + str(self._score)
        self._window.draw_string(string, 0, 0)

    def handle_mouse_up(self):
        self._small_dot.randomize_dot()
        self._big_dot.randomize_dot()

    def handle_events(self):
        # Handle the current game events. Return True if the player
        # clicked the close icon and False otherwise.
        event_list = get_events()
        for event in event_list:
            # handle one event
            self.handle_one_event(event)

    def handle_one_event(self, event):
        if event.type == QUIT:
            self._close_selected = True
        elif event.type == MOUSEBUTTONUP:
            self.handle_mouse_up()


class Dot:
    #   an object in this class represents a dot
    def __init__(self, color, radius, center, velocity, window):
        self._color = color
        self._radius = radius
        self._center = center
        self._velocity = velocity
        self._window = window

    def draw_dot(self):
        surface = self._window.get_surface()
        color = Color(self._color)
        draw_circle(surface, color, self._center, self._radius)

    def move_dot(self):
        # Change the location and the velocity of the dot so it
        # remains on the surface by bouncing from its edges.

        size = (self._window.get_width(), self._window.get_height())
        for index in range(0, 2):
            # update center at coordinate
            self._center[index] = self._center[index] + self._velocity[index]
            # dot edge outside window?
            if (self._center[index] <= self._radius) or (self._center[index] + self._radius >= size[index]):
                # change direction
                self._velocity[index] = - self._velocity[index]

    def randomize_dot(self):
        size = (self._window.get_width(), self._window.get_height())
        for index in range(0, 2):
            self._center[index] = (randint(self._radius, size[index] - self._radius))


main()
