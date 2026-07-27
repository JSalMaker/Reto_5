from .shape import Shape

class Triangle(Shape):
    def __init__(self, vertices: list):
        super().__init__(vertices, is_regular=False)
    def compute_area(self):
        s = self.compute_perimeter() / 2
        a, b, c = [e.get_length() for e in self._edges]
        return (s * (s - a) * (s - b) * (s - c))**0.5
    def compute_inner_angles(self):  # ayuda para el calculo de angulos internos
        s1 = self._edges[0].get_length()
        s2 = self._edges[1].get_length()
        s3 = self._edges[2].get_length()
        try:
            cos_A = (s2**2 + s3**2 - s1**2) / (2 * s2 * s3)
            cos_B = (s1**2 + s3**2 - s2**2) / (2 * s1 * s3)
            cos_C = (s1**2 + s2**2 - s3**2) / (2 * s1 * s2)
            return [cos_A, cos_B, cos_C]
        except ZeroDivisionError:
            return [0, 0, 0]
