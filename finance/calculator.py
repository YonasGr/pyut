class FinancialCalculator:
    @staticmethod
    def simple_interest(principal: float, rate: float, time: float) -> tuple:
        interest = (principal * rate * time) / 100
        return interest, principal + interest

    @staticmethod
    def compound_interest(principal: float, rate: float, time: float) -> tuple:
        amount = principal * (1 + rate / 100) ** time
        return amount - principal, amount

    @staticmethod
    def calculate_profit_loss(cost_price: float, selling_price: float) -> str:
        if selling_price > cost_price:
            return f"Profit: {selling_price - cost_price}"
        elif selling_price < cost_price:
            return f"Loss: {cost_price - selling_price}"
        return "No profit no loss"