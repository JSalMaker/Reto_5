from .shape import Shape

class Rectangle(Shape):
    def __init__(self, vertices: list):
        super().__init__(vertices, is_regular=False)
    def compute_area(self):
        return self._edges[0].get_length() * self._edges[1].get_length()
    def compute_inner_angles(self):
        return [90, 90, 90, 90]