import math

class GeometryCalculator:
    @staticmethod
    def rectangle_area(l: float, w: float) -> float: return l * w
    @staticmethod
    def rectangle_perimeter(l: float, w: float) -> float: return 2 * (l + w)
    @staticmethod
    def circle_area(r: float) -> float: return math.pi * r ** 2
    @staticmethod
    def circle_circumference(r: float) -> float: return 2 * math.pi * r
    @staticmethod
    def triangle_area(b: float, h: float) -> float: return 0.5 * b * h
    @staticmethod
    def triangle_type(a: float, b: float, c: float) -> str:
        if a + b <= c or a + c <= b or b + c <= a: return "Invalid"
        if a == b == c: return "Equilateral"
        if a == b or b == c or a == c: return "Isosceles"
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2: 
            return "Right-angled"
        return "Scalene"