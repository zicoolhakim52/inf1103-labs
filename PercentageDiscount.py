from DiscountStrategy import DiscountStrategy
class PercentageDiscount(DiscountStrategy):
    def __init__(self,percentage):
        self._percentage = percentage
        
    def apply(self, total: float) -> float:
        return total * self._percentage