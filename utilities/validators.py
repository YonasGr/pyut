class InputValidator:
    @staticmethod
    def is_valid_email(email: str) -> bool:
        return '@' in email and '.' in email.split('@')[-1]
    
    @staticmethod
    def is_positive_number(num: float) -> bool: return num > 0
    @staticmethod
    def is_negative_number(num: float) -> bool: return num < 0