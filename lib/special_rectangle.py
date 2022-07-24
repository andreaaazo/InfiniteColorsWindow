from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import Clock


class SpecialRectangle(Rectangle):
    def __init__(self):
        super().__init__()
        Clock.schedule_interval(self.move_circle, 1 / 60)

    def move_circle(self, dt):
        (x, y) = self.size
        self.size = (x + 1, y + 1)
