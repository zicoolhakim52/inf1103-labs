from DiscountStrategy import DiscountStrategy
class BulkDiscount(DiscountStrategy):
    def __init__(self):
        self._threshold=200
        self._amount=20
    def apply(self, total: float) -> float:
        if total >= self._threshold:
            return total - self._amount
        else:
            return total
    def print_self(self)-> str:
        return("Bulk Discount")