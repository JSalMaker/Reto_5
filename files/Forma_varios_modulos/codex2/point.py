class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def set_x(self, value):
        self._x = value
    def set_y(self, value):
        self._y = value
    def compute_distance(self, other):
        return ((self._x - other.get_x())**2 + (self._y - other.get_y())**2)**0.5