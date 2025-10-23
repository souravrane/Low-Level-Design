
# 🧬 Prototype Registry Pattern (Python)

## 🧩 Overview

The **Prototype Pattern** is a *creational design pattern* that creates new objects by **cloning existing ones** (called *prototypes*) rather than instantiating classes directly.

The **Prototype Registry** extends this by maintaining a **catalog of prototypes** that can be cloned on demand.

---

## 🚀 Why It’s Used

* ✅ **Performance** — avoids expensive object creation or initialization
* ✅ **Flexibility** — allows runtime object duplication and modification
* ✅ **Decoupling** — separates object creation logic from client code
* ✅ **Extensibility** — registry makes it easy to add new prototype types dynamically

---

## 🧱 Core Components

| Component                 | Responsibility                                                      |
| ------------------------- | ------------------------------------------------------------------- |
| **Prototype (Interface)** | Defines a `clone()` method                                          |
| **Concrete Prototypes**   | Implement the `clone()` method (e.g., `Car`, `Bike`)                |
| **Prototype Registry**    | Stores and manages prototype instances for reuse                    |
| **Client**                | Requests clones from the registry, optionally overriding attributes |

---

## 🧠 UML / Flow

```
     +--------------+      clone()       +--------------+
     |   Prototype  |<------------------ |   Registry   |
     +--------------+                    +--------------+
             ^                                   |
             |                                   |
   +-------------------+                 register(key, obj)
   | ConcretePrototype |                 clone(key, **attrs)
   +-------------------+                         |
             ^                                   |
             |                                   v
         +---------+                     +---------------+
         |  Client |-------------------->|  New Instance  |
         +---------+                     +---------------+
```

---

## ⚙️ Implementation Highlights

### 🔹 Cloneable Protocol

```python
@runtime_checkable
class Cloneable(Protocol):
    def clone(self) -> Any: ...
```

➡️ Allows **any class with a `.clone()` method** (not necessarily inheriting from a base) to qualify as “cloneable.”
This is **structural typing** in Python — *duck typing with type hints.*

---

### 🔹 Registry Logic

```python
def clone(self, key: str, **overrides) -> Any:
    proto = self._prototypes.get(key)
    if proto is None:
        raise KeyError(f"No prototype registered for {key}")
    obj = proto.clone()

    # Prefer dataclasses.replace() for immutable-safe updates
    if is_dataclass(obj):
        try:
            return replace(obj, **overrides)
        except TypeError:
            # fallback to setattr for extra fields
            for k, v in overrides.items():
                setattr(obj, k, v)
            return obj

    # generic fallback
    for k, v in overrides.items():
        setattr(obj, k, v)
    return obj
```

### 🔹 Why both `replace()` and `setattr()`?

| Method                  | When Used                                 | Why                                             |
| ----------------------- | ----------------------------------------- | ----------------------------------------------- |
| `dataclasses.replace()` | When the object is a `@dataclass`         | Type-safe, immutable-friendly, validates fields |
| `setattr()`             | When not a dataclass or `replace()` fails | Generic fallback, works on any Python object    |

---

## 🧬 Shallow vs Deep Copy

| Copy Type         | Description  | Effect on Mutable Fields             |
| ----------------- | ------------ | ------------------------------------ |
| `copy.copy()`     | Shallow copy | Shares nested objects (dangerous)    |
| `copy.deepcopy()` | Deep copy    | Recursively copies everything (safe) |

👉 Always prefer **deep copy** for prototypes to avoid side effects.

---

## 🧰 Example Summary

### Car & Bike Classes

```python
@dataclass
class Car:
    type: str
    color: str
    engine: str
    transmission: str
    features: List[str]
    def clone(self): return copy.deepcopy(self)
```

```python
@dataclass
class Bike:
    model: str
    color: str
    gears: int
    accessories: List[str]
    def clone(self): return copy.deepcopy(self)
```

### Registry Usage

```python
registry = PrototypeRegistry()
registry.register("family_suv", Car(...))
registry.register("city_bike", Bike(...))

clone1 = registry.clone("family_suv", color="Blue", features=["360 Camera"])
clone2 = registry.clone("city_bike", gears=8)
```

✅ Each call returns a **fresh, deep-copied object**, leaving prototypes untouched.

---

## ⚖️ Prototype vs Factory

| Aspect          | Prototype                     | Factory                               |
| --------------- | ----------------------------- | ------------------------------------- |
| Object creation | Clone existing object         | Create new object from scratch        |
| Performance     | Faster (no reinit)            | Slower (full creation)                |
| Configuration   | Based on an existing template | Based on parameters / class hierarchy |
| Flexibility     | Runtime dynamic               | Compile-time or parameter-driven      |

---

## 🧪 Key Test Cases

| Test                                 | What It Verifies                                         |
| ------------------------------------ | -------------------------------------------------------- |
| `test_clone_returns_distinct_object` | Cloned object has different identity but same content    |
| `test_deepcopy_independence`         | Mutating clone’s mutable fields doesn’t affect prototype |
| `test_overrides_apply`               | Registry applies field overrides correctly               |
| `test_registry_mixed_types`          | Handles different classes uniformly                      |
| `test_clone_unknown_key`             | Raises `KeyError` for unregistered prototype             |
| `test_unregister_removes_prototype`  | Unregister prevents further cloning                      |

---

## 🧠 Common Interview Questions

| Question                                                                      | Strong Answer                                                                                       |
| ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Q1:** Why use Prototype instead of Factory?                                 | When object creation is expensive or complex, cloning a pre-built prototype is faster and cleaner.  |
| **Q2:** Why use a Registry?                                                   | It centralizes and reuses prototype definitions; clients don’t need to know about concrete classes. |
| **Q3:** How do you ensure cloned objects don’t share mutable state?           | Use `copy.deepcopy()` in the `.clone()` implementation.                                             |
| **Q4:** Why `replace()` and `setattr()`?                                      | `replace()` for dataclasses (safe immutable updates), `setattr()` for generic objects.              |
| **Q5:** What’s the difference between shallow and deep copy?                  | Shallow shares references; deep recursively clones nested objects.                                  |
| **Q6:** How does `Cloneable` work?                                            | It’s a `Protocol` — any object with `.clone()` qualifies (structural typing).                       |
| **Q7:** What happens if you return the prototype directly instead of cloning? | All callers share the same instance — mutations leak between objects (breaks pattern).              |

---

## 🏁 TL;DR Summary

> The **Prototype Registry Pattern** in Python is a **hybrid** between caching and cloning —
> it lets you **register ready-to-clone templates** and **generate new objects** dynamically, safely, and efficiently.

### ✅ Key Takeaways

* Use `copy.deepcopy()` inside `.clone()`
* Keep a **registry of base prototypes**
* Use `dataclasses.replace()` for immutability
* Fall back to `setattr()` for generality
* Never return the prototype itself — always clone
* Registry decouples clients from concrete classes

