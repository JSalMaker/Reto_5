from .triangle import Triangle

class TriRectangle(Triangle):
    def __init__(self, vertices: list):
        super().__init__(vertices)
    def compute_inner_angles(self):
        return super().compute_inner_angles()