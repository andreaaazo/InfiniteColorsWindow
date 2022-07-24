from .infinite_loop import InfiniteLoop
from kivy.app import App


class InfiniteWindowApp(App):
    def build(self):
        return InfiniteLoop()
