
# 🏭 Factory Patterns — Interview Revision

## 🔹 Overview

**Factory Patterns** are *creational design patterns* that deal with **object creation logic** —
they hide the “new” keyword and centralize how objects are created.

### 🎯 Goal

> Encapsulate the creation of objects so the client code depends only on interfaces, not on concrete implementations.

---

## 🧩 1. Simple Factory Pattern

### 🧠 Concept

A **Simple Factory** centralizes object creation inside a single method (e.g., `create_product(type)`).

```python
class CarFactory:
    @staticmethod
    def create_car(car_type: str) -> Car:
        if car_type == "SUV":
            return SUV()
        elif car_type == "Sedan":
            return Sedan()
        elif car_type == "Coupe":
            return Coupe()
        else:
            raise ValueError("Unknown car type")
```

✅ **Advantages**

* Centralizes object creation
* Simple to implement
* Keeps client code clean

❌ **Drawbacks**

* Violates *Open/Closed Principle* (you must modify the factory for every new product)
* Grows large and hard to maintain
* Tightly coupled to all concrete classes

---

### 🧱 UML Diagram

```
        +---------------------+
        |     CarFactory      |
        +---------------------+
        | + create_car(type)  |
        +---------------------+
                 |
    +------------+-------------+
    |            |             |
+---------+  +---------+  +---------+
|   SUV   |  |  Sedan  |  |  Coupe  |
+---------+  +---------+  +---------+
```

---

## 🧩 2. Factory Method Pattern

### 🧠 Concept

> Define an **interface** for object creation but let **subclasses decide** which class to instantiate.

Each subclass (factory) overrides the `create_product()` method to produce a specific product.

```python
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def specs(self): pass

class SUV(Car):
    def specs(self): return "SUV - Hybrid, Automatic"

class Sedan(Car):
    def specs(self): return "Sedan - Petrol, Automatic"

class CarFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car: pass

class SUVFactory(CarFactory):
    def create_car(self): return SUV()

class SedanFactory(CarFactory):
    def create_car(self): return Sedan()
```

✅ **Advantages**

* Adheres to Open/Closed Principle
* Promotes polymorphism
* Client code doesn’t depend on concrete classes

❌ **Drawbacks**

* One product per factory subclass
* Explosion of small factory classes
* Doesn’t coordinate multiple related objects

---

### 🧱 UML Diagram

```
          +---------------------+
          |    CarFactory (ABC) |
          +---------------------+
          | + create_car()      |
          +---------------------+
                  ^
                  |
      +-----------+------------+
      |                        |
+---------------+       +---------------+
|  SUVFactory   |       | SedanFactory  |
+---------------+       +---------------+
| + create_car()|       | + create_car()|
      |                        |
      v                        v
  +--------+              +---------+
  |  SUV   |              |  Sedan  |
  +--------+              +---------+
```

---

## 🧩 3. Abstract Factory Pattern

### 🧠 Concept

> Provides an interface to create **families of related or dependent objects**
> without specifying their concrete classes.

Each factory creates **multiple related objects** that belong to one “theme” or “family.”

```python
from abc import ABC, abstractmethod

class Car(ABC): @abstractmethod
def specs(self): pass
class Bike(ABC): @abstractmethod
def specs(self): pass

class EconomyCar(Car): def specs(self): return "Economy Car 1.2L"
class EconomyBike(Bike): def specs(self): return "Economy Bike 100cc"
class SportsCar(Car): def specs(self): return "Sports Car V8"
class SportsBike(Bike): def specs(self): return "Sports Bike 600cc"

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self): pass
    @abstractmethod
    def create_bike(self): pass

class EconomyVehicleFactory(VehicleFactory):
    def create_car(self): return EconomyCar()
    def create_bike(self): return EconomyBike()

class SportsVehicleFactory(VehicleFactory):
    def create_car(self): return SportsCar()
    def create_bike(self): return SportsBike()
```

✅ **Advantages**

* Produces **consistent families** of related objects
* Guarantees compatibility across product families
* Adheres to Open/Closed Principle
* Hides complex creation logic

❌ **Drawbacks**

* Adds abstraction & boilerplate
* Harder to add new product *types* (you must edit every factory)

---

### 🧱 UML Diagram

```
        +--------------------------+
        |   VehicleFactory (ABC)   |
        +--------------------------+
        | + create_car()           |
        | + create_bike()          |
        +--------------------------+
                 ^             ^
                 |             |
   +-------------+---+     +---+-------------+
   | EconomyVehicle  |     | SportsVehicle  |
   |   Factory        |     |   Factory      |
   +------------------+     +----------------+
   | + create_car()   |     | + create_car() |
   | + create_bike()  |     | + create_bike()|
   +------------------+     +----------------+
        |     |                    |     |
        v     v                    v     v
 +--------------+           +--------------+
 | EconomyCar   |           | SportsCar    |
 +--------------+           +--------------+
 | EconomyBike  |           | SportsBike   |
 +--------------+           +--------------+
```

---

## 🧩 4. Comparison Table

| Feature                   | Simple Factory                 | Factory Method              | Abstract Factory                                  |
| ------------------------- | ------------------------------ | --------------------------- | ------------------------------------------------- |
| **Creates**               | Single product                 | Single product per subclass | Families of related products                      |
| **Extensibility**         | Poor                           | Good                        | Excellent                                         |
| **Open/Closed Principle** | ❌                              | ✅                           | ✅                                                 |
| **Complexity**            | Low                            | Medium                      | High                                              |
| **Example**               | `CarFactory.create_car("SUV")` | `SUVFactory().create_car()` | `SportsFactory().create_car()` + `.create_bike()` |

---

## 🧩 5. Real-World Analogy

| Pattern              | Analogy                                                                  |
| -------------------- | ------------------------------------------------------------------------ |
| **Simple Factory**   | One chef making every dish (lots of `if/else`)                           |
| **Factory Method**   | Each chef specializes in one dish                                        |
| **Abstract Factory** | Each restaurant (family) offers a full cuisine set (e.g., pasta + pizza) |

---

## 🧩 6. Factory Method → Abstract Factory Evolution

| Factory Method Problem           | Abstract Factory Fix                               |
| -------------------------------- | -------------------------------------------------- |
| Creates only one product         | Creates multiple related products                  |
| Explosion of subclasses          | Fewer, family-based factories                      |
| No coordination between products | Enforces consistency across products               |
| No product families              | Supports themed families (Economy, Sports, Luxury) |

---

## 🧩 7. Factory Selection Problem (Follow-Up Discussion)

### ⚙️ The Issue

Even with Abstract Factory, your **driver code** may still have an `if/else` ladder to decide *which factory family* to use:

```python
if family == "economy":
    factory = EconomyVehicleFactory()
elif family == "sports":
    factory = SportsVehicleFactory()
else:
    raise ValueError("Unknown type")
```

This moves the `if/else` **out of the factory**, but not **out of the system**.

---

### 🧠 Why It’s Acceptable

* The conditional now exists at the **configuration level**, not inside the core creation logic.
* You’re still following the **Open/Closed Principle** — you can add new factories without modifying existing factory classes.
* The driver is merely **selecting which factory to use**, not **how to build the products**.

---

### ⚡ When It Becomes a Problem

If the driver keeps growing with many conditionals, the selection logic itself becomes a bottleneck — just moved to a different layer.

---

### 🧱 Solution 1: **Factory Registry / Provider**

Create a dictionary that maps family names to factory classes:

```python
# factory_provider.py
FACTORY_MAP = {
    "economy": EconomyVehicleFactory,
    "sports": SportsVehicleFactory,
}

def get_factory(name: str):
    try:
        return FACTORY_MAP[name.lower()]()
    except KeyError:
        raise ValueError(f"Unknown factory: {name}")
```

Usage:

```python
factory = get_factory("sports")
car = factory.create_car()
bike = factory.create_bike()
```

✅ No `if/else` in driver
✅ Adding new family = register in map
✅ Open/Closed still satisfied

---

### 🧱 Solution 2: **Config-Driven or Dependency-Injected Factory**

Load the factory name dynamically from configuration or environment:

```python
import importlib

def get_factory_from_config(config):
    module = importlib.import_module(f"factories.{config['factory_name']}_factory")
    factory_class = getattr(module, f"{config['factory_name'].capitalize()}VehicleFactory")
    return factory_class()
```

✅ Fully dynamic — zero hardcoded logic
✅ Used in plugin systems and DI frameworks

---

### 🧩 Design Principle

> “It’s fine to have *selection* logic in the client,
> but not *construction* logic.
> The Abstract Factory ensures the latter is encapsulated.”

---

### 🧱 UML View (Extended)

```
        +---------------------------+
        |  Factory Provider / Map   |
        +---------------------------+
        | "economy" -> EconomyFactory |
        | "sports"  -> SportsFactory  |
        +-------------+-------------+
                      |
                      v
          +------------------------+
          |   VehicleFactory (ABC) |
          +------------------------+
          | + create_car()         |
          | + create_bike()        |
          +------------------------+
```

---

## 🧠 8. Common Interview Questions

| Category       | Question                                                                                              |
| -------------- | ----------------------------------------------------------------------------------------------------- |
| **Concept**    | What problem does the Factory Pattern solve?                                                          |
| **Comparison** | Difference between Simple, Factory Method, and Abstract Factory?                                      |
| **Principle**  | How does Factory Method follow the Open/Closed Principle?                                             |
| **Evolution**  | Why use Abstract Factory over Factory Method?                                                         |
| **Follow-Up**  | What if you still have `if/else` in your driver? (→ Factory Provider)                                 |
| **Real-World** | Give an example of an Abstract Factory in real systems (e.g., GUI toolkits, database connectors).     |
| **Advanced**   | Can you combine Factory and Prototype patterns? (Yes — factories may clone prototypes.)               |
| **Extension**  | What’s the drawback of Abstract Factory? (Adding new product *types* requires editing all factories.) |

---

## 🧩 9. Quick Summary Table

| Pattern          | Level        | Creates                       | Example                                           | Pros        | Cons                  |
| ---------------- | ------------ | ----------------------------- | ------------------------------------------------- | ----------- | --------------------- |
| Simple Factory   | Basic        | One object                    | `CarFactory.create_car("SUV")`                    | Simple      | Not scalable          |
| Factory Method   | Intermediate | One product per subclass      | `SUVFactory().create_car()`                       | Extensible  | Many factories        |
| Abstract Factory | Advanced     | Families of products          | `SportsFactory().create_car()` + `.create_bike()` | Consistency | Boilerplate           |
| Factory Provider | Meta-level   | Returns factories dynamically | `get_factory("sports")`                           | No if/else  | Needs registry/config |

---

## 🧩 10. Final Visual Summary

```
SIMPLE FACTORY
  One class decides all object creation (if/else inside).

FACTORY METHOD
  Abstract creator defines create(); subclasses decide what to create.

ABSTRACT FACTORY
  Each factory creates multiple related objects (families).

FACTORY PROVIDER
  Registry maps string/config to correct factory — eliminates driver if/else.
```

---

## 🧠 Interview Tip

> Always emphasize **decoupling** and **scalability**.
> Show that you understand not just *how* to implement a factory,
> but *why* each evolution (Simple → Method → Abstract → Registry) happens.

---
