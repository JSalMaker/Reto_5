from .line import Line

class Shape:
    def __init__(self, vertices: list, is_regular: bool):
        self._vertices = vertices
        self._is_regular = is_regular
        self._edges = self._create_edges()
        self._inner_angles = self.compute_inner_angles()
    def _create_edges(self):
        edges = []
        n = len(self._vertices)
        for i in range(n):
            p1 = self._vertices[i]
            p2 = self._vertices[(i + 1) % n]
            edges.append(Line(p1, p2))
        return edges
    def get_vertices(self):
        return self._vertices
    def get_edges(self):
        return self._edges
    def get_is_regular(self):
        return self._is_regular
    def compute_perimeter(self):
        total = 0
        for edge in self._edges:
            total += edge.get_length()
        return total
    def compute_area(self):
        pass
    def compute_inner_angles(self):
        return []