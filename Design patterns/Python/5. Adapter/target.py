from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount_in_rupees: float) -> str:
        # process payment and return transaction status
        pass