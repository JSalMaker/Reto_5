from .point import Point

class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self._start_point = start_point
        self._end_point = end_point
        self._length = self._start_point.compute_distance(self._end_point)
    def get_start_point(self):
        return self._start_point
    def get_end_point(self):
        return self._end_point
    def get_length(self):
        return self._length