from kivy.uix.widget import Widget
from kivy.graphics.context_instructions import Color
from kivy.properties import Clock
import colorsys
from .special_rectangle import SpecialRectangle


class InfiniteLoop(Widget):
    hue = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.create_circle, 1 / 60)

    def create_circle(self, dt):
        (r, g, b) = colorsys.hsv_to_rgb(self.hue, 1.0, 1.0)
        with self.canvas:
            Color(r, g, b)
            self.rect = SpecialRectangle()
        self.hue += 0.001
