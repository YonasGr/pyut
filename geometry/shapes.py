class ShapeValidator:
    @staticmethod
    def is_valid_triangle(a: float, b: float, c: float) -> bool:
        """Check if triangle sides are valid"""
        return a + b > c and a + c > b and b + c > a

    @staticmethod
    def is_valid_rectangle(length: float, width: float) -> bool:
        """Check if rectangle dimensions are valid"""
        return length > 0 and width > 0

class ShapeProperties:
    @staticmethod
    def triangle_type(a: float, b: float, c: float) -> str:
        """Classify triangle type"""
        if not ShapeValidator.is_valid_triangle(a, b, c):
            return "Invalid triangle"
        if a == b == c:
            return "Equilateral"
        if a == b or b == c or a == c:
            return "Isosceles"
        return "Scalene"