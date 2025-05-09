import math

class MathOperations:
    @staticmethod
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(std_math.sqrt(n)) + 1):  # Use the renamed import
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def add(a: float, b: float) -> float: return a + b
    @staticmethod
    def subtract(a: float, b: float) -> float: return a - b
    @staticmethod
    def multiply(a: float, b: float) -> float: return a * b
    @staticmethod
    def divide(a: float, b: float) -> float: return a / b if b != 0 else float('nan')
    @staticmethod
    def power(a: float, b: float) -> float: return a ** b
    @staticmethod
    def factorial(n: int) -> int:
        if n < 0: raise ValueError("No factorial for negatives")
        return 1 if n <= 1 else n * MathOperations.factorial(n-1)
    @staticmethod
    def is_prime(n: int) -> bool:
        if n <= 1: return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0: return False
        return True