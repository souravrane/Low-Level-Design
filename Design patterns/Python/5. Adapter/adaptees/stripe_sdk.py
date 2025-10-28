class StripeSDK:
    def make_charge(self, amount_in_cents: int, currency_code: str = "usd") -> dict:
        print(f"[Stripe] Charging ${amount_in_cents/100:.2f} {currency_code.upper()}")
        return {"paid": True, "amount": amount_in_cents, "currency": currency_code}