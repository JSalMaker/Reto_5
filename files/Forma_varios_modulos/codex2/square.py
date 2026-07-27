from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, vertices: list):
        super().__init__(vertices)
        self._is_regular = True