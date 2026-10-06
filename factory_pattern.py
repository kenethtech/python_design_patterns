
class Stripe:
    def pay(self, amount):
        return f"Paying: {amount} to User via Stripe"

class Paypal:
    def pay(self, amount):
        return f"Paying: {amount} to User via Paypal"

class Crypto:
    def pay(self, amount):
        return f"Paying: {amount} to User via Crypto"

class Mpesa:
    def pay(self, amount):
        return f"Paying: {amount} via M-Pesa"

Payment_Registry= {
    "stripe": Stripe,
    "paypal": Paypal,
    "crypto": Crypto
}

class PaymentFactory:
    @staticmethod
    def create(provider):
        payment_class = Payment_Registry.get(provider)
        if payment_class:
            return payment_class()
        raise ValueError(f"Unknown {provider}")

if __name__ == "__main__":
    stripe = PaymentFactory.create("stripe").pay(50)
    paypal = PaymentFactory.create("paypal").pay(70)
    crypto = PaymentFactory.create("crypto").pay(40)

    Payment_Registry["mpesa"] = Mpesa

    mpesa = PaymentFactory.create("mpesa").pay(100)

    print(stripe)
    print(paypal)
    print(crypto)
    print(mpesa)

   
