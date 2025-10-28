from target import PaymentGateway
from adaptees.stripe_sdk import StripeSDK

class StripeAdapter(PaymentGateway):
    def __init__(self, sdk: StripeSDK):
        self.sdk = sdk
    
    def pay(self, amount_in_rupees: float) -> str:
        usd_cents = int((amount_in_rupees / 83) * 100)
        result = self.sdk.make_charge(usd_cents, "usd")
        return "SUCCESS" if result.get("paid") else "FAILED"