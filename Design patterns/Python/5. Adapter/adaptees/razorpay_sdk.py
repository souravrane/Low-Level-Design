class RazorpaySDK:
    def initiate_payment(self, amount_in_paise: int, currency: str = "INR") -> dict:
        # Simulate API call
        print(f"[Razorpay] Initiating payment of ₹{amount_in_paise/100:.2f} {currency}")
        return {"status": "captured", "amount": amount_in_paise, "currency": currency}