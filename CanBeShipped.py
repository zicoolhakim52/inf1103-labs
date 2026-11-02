from abc import ABC, abstractmethod
class CanBeShipped(ABC):
    
    def calculate_shipping_cost(self):
        pass