from target import PaymentGateway
from adaptees.razorpay_sdk import RazorpaySDK

class RazorpayAdapter(PaymentGateway):
    def __init__(self, sdk: RazorpaySDK):
        self.sdk = sdk
    
    def pay(self, amount_in_rupees: float) -> str:
        paise = int(amount_in_rupees * 100)
        result = self.sdk.initiate_payment(paise, "INR")
        return "SUCCESS" if result.get("status") == "captured" else "FAILED"