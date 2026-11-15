from abc import ABC, abstractmethod
class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass
    @abstractmethod
    def print_self(self)-> None:
        pass