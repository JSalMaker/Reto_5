from .triangle import Triangle

class Equilateral(Triangle):
    def __init__(self, vertices: list):
        super().__init__(vertices)
        self._is_regular = True
    def compute_inner_angles(self):
        return [60, 60, 60]