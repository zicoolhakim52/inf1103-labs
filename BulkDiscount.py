from DiscountStrategy import DiscountStrategy
class BulkDiscount(DiscountStrategy):
    def __init__(self,threshold,amount):
        self._threshold=threshold
        self._amount=amount
    def apply(self, total: float) -> float:
        if total >= self._threshold:
            return total - self._amount
        else:
            return total