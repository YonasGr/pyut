class UnitConverter:
    @staticmethod
    def celsius_to_fahrenheit(c: float) -> float: return (c * 9/5) + 32
    @staticmethod
    def fahrenheit_to_celsius(f: float) -> float: return (f - 32) * 5/9
    @staticmethod
    def km_to_miles(km: float) -> float: return km * 0.621371
    @staticmethod
    def miles_to_km(miles: float) -> float: return miles * 1.60934