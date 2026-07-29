from codex1.shapes import (
    Point,
    Square,
    Rectangle,
    Equilateral,
    Isosceles,
    Scalene,
    TriRectangle,
)

def print_shape_info(shape):
    print(f"{name}")
    print(f"Perimetro: {shape.compute_perimeter()}")
    print(f"Area: {shape.compute_area()}")
    print(f"Angulos internos: {shape.compute_inner_angles()}")
    print(f"Es regular: {shape.get_is_regular()}")

def main():
    square = Square([Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4)])
    print_shape_info("Square", square)   
    rectangle = Rectangle([Point(0, 0), Point(4, 0), Point(4, 2), Point(0, 2)])
    print_shape_info("Rectangle", rectangle)
    equilateral = Equilateral([Point(0, 0), Point(4, 0), Point(2, 3.464)])
    print_shape_info("Equilateral", equilateral)
    isosceles = Isosceles([Point(0, 0), Point(4, 0), Point(2, 3)])
    print_shape_info("Isosceles", isosceles)
    scalene = Scalene([Point(0, 0), Point(5, 0), Point(1, 2)])
    print_shape_info("Scalene", scalene)
    tri_rectangle = TriRectangle([Point(0, 0), Point(4, 0), Point(0, 3)])
    print_shape_info("TriRectangle", tri_rectangle)

if __name__ == "__main__":
    main()
