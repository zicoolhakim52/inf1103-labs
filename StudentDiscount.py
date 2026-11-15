from DiscountStrategy import DiscountStrategy
class PercentageDiscount(DiscountStrategy):
    def __init__(self):
        self._percentage = 0.8
        
    def apply(self, total: float) -> float:
        return total * self._percentage