# 🧲 Adapter Design Pattern — Interview Revision (Python)

---

## 🎯 1. Concept Overview

> The **Adapter Pattern** allows incompatible interfaces to work together by acting as a *bridge* between them.

It wraps an existing class (the **Adaptee**) with a new interface (the **Target**) that the **Client** expects — converting method names, parameter formats, or data types.

---

### 🧱 When to Use

✅ Integrate **legacy or third-party** APIs with mismatched method names or signatures
✅ Avoid rewriting working code just to fit a new interface
✅ Unify **multiple vendor SDKs** under one standard interface
✅ Switch between APIs (e.g., Razorpay ↔ Stripe) without changing client code

---

## 🧩 2. UML Diagram (Object Adapter via Composition)

```
Client ---> Target (expected interface)
              ^
              |
        +-----+------+
        |   Adapter  |----> Adaptee (existing incompatible class)
        +-------------+
        | adaptee     |
        | request()   |--> translates --> adaptee.specific_request()
        +-------------+
```

---

## 🧠 3. Types of Adapters

| Type               | Mechanism            | Description                                | Preferred?                                     |
| ------------------ | -------------------- | ------------------------------------------ | ---------------------------------------------- |
| **Object Adapter** | Composition          | Adapter *has* an instance of Adaptee       | ✅ Yes (flexible, composable)                   |
| **Class Adapter**  | Multiple inheritance | Adapter *inherits* from Adaptee and Target | ⚠️ Only if MI is acceptable (Python allows it) |

---

## 💳 4. Real-World Example — Unified Payment Gateway (Razorpay + Stripe)

### 🎯 `target.py` — Standard interface

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount_in_rupees: float) -> str:
        """Process payment and return transaction status"""
        pass
```

---

### 🪝 Adaptees (3rd-party SDKs)

```python
# adaptees/razorpay_sdk.py
class RazorpaySDK:
    def initiate_payment(self, amount_in_paise: int, currency="INR"):
        print(f"[Razorpay] Paying ₹{amount_in_paise/100:.2f}")
        return {"status": "captured"}

# adaptees/stripe_sdk.py
class StripeSDK:
    def make_charge(self, amount_in_cents: int, currency_code="usd"):
        print(f"[Stripe] Charging ${amount_in_cents/100:.2f} {currency_code.upper()}")
        return {"paid": True}
```

---

### 🔌 Adapters

```python
# adapters/razorpay_adapter.py
from target import PaymentGateway
from adaptees.razorpay_sdk import RazorpaySDK

class RazorpayAdapter(PaymentGateway):
    def __init__(self, sdk: RazorpaySDK):
        self.sdk = sdk

    def pay(self, amount_in_rupees: float) -> str:
        paise = int(amount_in_rupees * 100)
        result = self.sdk.initiate_payment(paise, "INR")
        return "SUCCESS" if result.get("status") == "captured" else "FAILED"
```

```python
# adapters/stripe_adapter.py
from target import PaymentGateway
from adaptees.stripe_sdk import StripeSDK

class StripeAdapter(PaymentGateway):
    def __init__(self, sdk: StripeSDK):
        self.sdk = sdk

    def pay(self, amount_in_rupees: float) -> str:
        usd_cents = int((amount_in_rupees / 83) * 100)  # conversion
        result = self.sdk.make_charge(usd_cents, "usd")
        return "SUCCESS" if result.get("paid") else "FAILED"
```

---

### 🧠 Client Code

```python
from adaptees.razorpay_sdk import RazorpaySDK
from adaptees.stripe_sdk import StripeSDK
from adapters.razorpay_adapter import RazorpayAdapter
from adapters.stripe_adapter import StripeAdapter

def main():
    amount = 499.99
    razorpay = RazorpayAdapter(RazorpaySDK())
    stripe = StripeAdapter(StripeSDK())

    print("\nUsing Razorpay:")
    print("Transaction:", razorpay.pay(amount))

    print("\nUsing Stripe:")
    print("Transaction:", stripe.pay(amount))

if __name__ == "__main__":
    main()
```

✅ **Output:**

```
Using Razorpay:
[Razorpay] Paying ₹499.99
Transaction: SUCCESS

Using Stripe:
[Stripe] Charging $6.02 USD
Transaction: SUCCESS
```

---

## 🧪 5. Test Example

```python
import unittest
from adaptees.razorpay_sdk import RazorpaySDK
from adapters.razorpay_adapter import RazorpayAdapter

class TestPaymentAdapter(unittest.TestCase):
    def test_successful_payment(self):
        sdk = RazorpaySDK()
        gw = RazorpayAdapter(sdk)
        self.assertEqual(gw.pay(100.0), "SUCCESS")

if __name__ == "__main__":
    unittest.main()
```

---

## ⚙️ 6. Class Adapter (via multiple inheritance)

> Less flexible — used only when one adaptee must be extended directly.

```python
from target import PaymentGateway
from adaptees.razorpay_sdk import RazorpaySDK

class RazorpayClassAdapter(RazorpaySDK, PaymentGateway):
    def pay(self, amount_in_rupees: float) -> str:
        paise = int(amount_in_rupees * 100)
        result = self.initiate_payment(paise, "INR")
        return "SUCCESS" if result.get("status") == "captured" else "FAILED"
```

---

## 🔍 7. Adapter vs Other Patterns

| Pattern       | Goal                                     | Difference                         |
| ------------- | ---------------------------------------- | ---------------------------------- |
| **Adapter**   | Make incompatible APIs work together     | Converts interface                 |
| **Decorator** | Add responsibilities dynamically         | Keeps same interface               |
| **Facade**    | Simplify a complex subsystem             | Offers simpler API, not conversion |
| **Bridge**    | Separate abstraction from implementation | For scalability, not compatibility |

---

## 🧠 8. Advantages & Disadvantages

| ✅ Advantages                         | ❌ Disadvantages                 |
| ------------------------------------ | ------------------------------- |
| Reuse existing incompatible classes  | Extra abstraction layer         |
| Decouples client from SDK specifics  | Too many adapters to maintain   |
| Promotes flexibility and testability | Harder debugging through layers |

---

## 🧩 9. Common Interview Q&A

### 🧾 Conceptual

**Q1. Why do we need an Adapter when we can modify the 3rd-party code?**

> Because 3rd-party or legacy code is often closed-source, shared, or risky to edit. The adapter adds flexibility without altering the source.

---

**Q2. Difference between Adapter and Facade?**

> Adapter converts **incompatible APIs**; Facade **simplifies** a complex one.
> Adapter = “Translator”, Facade = “Receptionist”.

---

**Q3. Which type of adapter is better — class or object?**

> Object Adapter (composition) → flexible, supports many adaptees, avoids multiple inheritance pitfalls.

---

**Q4. Can Adapter and Factory patterns work together?**

> Yes. A **Factory** can return the right Adapter dynamically:
> `PaymentFactory.get_gateway("stripe") → StripeAdapter()`.

---

**Q5. What if Adaptee returns data in different units (e.g., USD vs INR)?**

> The Adapter’s job is to handle such conversions transparently.

---

**Q6. Is Adapter pattern runtime or compile-time binding?**

> Runtime. It works by delegation — dynamic dispatch.

---

**Q7. Why does Adapter promote the Open/Closed Principle?**

> You can add new adapters (new vendor integrations) **without modifying** client code.

---

### ⚙️ Technical

**Q8. Can you chain multiple adapters?**

> Yes — a *double adapter* is possible when you must go through multiple incompatible layers (e.g., `LegacyAdapter` → `RESTAdapter` → `PaymentGatewayAdapter`), though it’s best to flatten over time.

---

**Q9. How would you test an Adapter?**

> Mock the Adaptee SDK; assert that `adapter.pay()` calls the correct Adaptee method and transforms data properly.

---

**Q10. Can Adapter be used to unify data shape instead of behavior?**

> Absolutely. Example: wrapping APIs that return JSON or dicts in a uniform `.to_dict()` interface.

---

### ⚡ Tricky Follow-Ups

**Q11. Isn’t Adapter just polymorphism?**

> No — polymorphism expects *common inheritance*. Adapter works when classes have **no shared ancestry**, only behavioral overlap.

---

**Q12. How does Adapter differ from Proxy?**

> Proxy controls **access** (security, caching), Adapter **transforms** interface.
> Think: Proxy guards the door, Adapter translates the language.

---

**Q13. What’s the trade-off between flexibility and performance here?**

> Minor indirection overhead (usually negligible) in exchange for huge design flexibility and maintainability.

---

**Q14. Can you build reversible adapters?**

> Possible but rare. You’d have to maintain two sets of translation functions (one per direction).

---

**Q15. What are “two-way adapters”?**

> An adapter that can make both `Target → Adaptee` and `Adaptee → Target` calls. Used in legacy migration systems.

---

## 🧠 10. Summary Table

| Concept                   | Description                                                                      |
| ------------------------- | -------------------------------------------------------------------------------- |
| **Intent**                | Convert one interface to another                                                 |
| **Key Players**           | Target, Adaptee, Adapter, Client                                                 |
| **Implementation Style**  | Composition (object adapter) or multiple inheritance (class adapter)             |
| **Open/Closed Principle** | Add new adapters without changing clients                                        |
| **Real-World Example**    | PaymentGateway unifying Razorpay, Stripe, PayPal                                 |
| **Testing Strategy**      | Mock Adaptee, test interface translation                                         |
| **Common Pitfall**        | Making adapters too fat — they should only *translate*, not *own business logic* |

---

## 🧩 11. Visual Summary (Text Diagram)

```
          CLIENT
             │
             ▼
         +-----------+
         |  Adapter   |  implements Target
         +-----------+
             │ uses
             ▼
         +-----------+
         |  Adaptee   |
         +-----------+
```

---

## 💡 12. Takeaway One-Liner

> 🗣️ “Adapter translates, Facade simplifies, Decorator augments.”
> The Adapter pattern **bridges incompatibility** — letting old and new systems talk seamlessly.

---

## ✅ TL;DR

| Attribute              | Adapter Pattern                                       |
| ---------------------- | ----------------------------------------------------- |
| **Category**           | Structural                                            |
| **Purpose**            | Interface translation                                 |
| **Best Example**       | Unifying Razorpay, Stripe, PayPal under one interface |
| **Implementation Tip** | Use composition for flexibility                       |
| **Interview Tip**      | Emphasize “works with unmodifiable codebases”         |
| **Common Follow-Up**   | Compare with Facade, Proxy, Bridge                    |

---

> **“Adapters keep your code future-proof — you don’t fix old code; you wrap it.”**

---
