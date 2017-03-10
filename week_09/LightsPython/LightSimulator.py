"""The lightSimulater program"""
from splashkit import *

class LightBulb(object):
    """Creates a lightbulb."""

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__is_on = False

    def toggle_power(self):
        """Toggles the power of the lightbulb"""
        self.__is_on = not self.__is_on

    def draw(self):
        """Draws the lightbulb"""
        draw_bitmap(self.image, self.x, self.y)

    @property
    def image(self):
        return bitmap_named("On" if self.__is_on else "Off")

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

def run():
    load_resources()
    window = open_window("LightSimulator", 800, 600)
    light_bulb = LightBulb(20, 30)

    while not window_close_requested(window):
        process_events()
        if key_typed(KeyCode.space_key):
            light_bulb.toggle_power()
        clear_screen(color_white())
        light_bulb.draw()
        refresh_screen()

    close_window(window)

def load_resources():
    load_bitmap("On", "medium-on-light.png")
    load_bitmap("Off", "medium-off-light.png")

run()