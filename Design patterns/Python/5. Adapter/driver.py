from adapters.razorpay_adapter import RazorpayAdapter
from adapters.stripe_adapter import StripeAdapter
from adaptees.razorpay_sdk import RazorpaySDK
from adaptees.stripe_sdk import StripeSDK


def main():
    amount = 499.99

    razorpay_gateway = RazorpayAdapter(RazorpaySDK())
    print("\nUsing Razorpay:")
    print("Transaction:", razorpay_gateway.pay(amount))

    stripe_gateway = StripeAdapter(StripeSDK())
    print("\nUsing Stripe")
    print("Transaction:", stripe_gateway.pay(amount))

main()