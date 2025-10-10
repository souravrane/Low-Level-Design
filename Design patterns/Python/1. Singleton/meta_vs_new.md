**call** vs **new** in Singleton Implementations

🧩 Purpose

Both methods control object creation, but at different levels of Python’s class system.

⸻

⚙️ **new** — Instance Creation Hook (Class Level)
• Where it lives: Inside a class or base class.
• When it runs: Before **init**, whenever you do MyClass().
• What it does: Allocates and returns a new instance object.
• Why used in Singleton:
Checks if an instance already exists; if not, creates one and stores it.
Subsequent calls return the cached object.

Example

class SingletonBase:
\_instance = None
def **new**(cls, \*args, \*\*kwargs):
if cls.\_instance is None:
cls.\_instance = super().**new**(cls)
return cls.\_instance

⸻

🧠 **call** — Class Instantiation Hook (Metaclass Level)
• Where it lives: Inside a metaclass.
• When it runs: Every time you “call” a class (e.g. MyClass()), before Python allocates the instance.
• What it does: Wraps the entire creation process (**new** → **init**).
• Why used in Singleton:
Lets you intercept instantiation globally so any class using that metaclass becomes a singleton automatically—no need for a shared base class.

Example

class SingletonMeta(type):
\_instances = {}
def **call**(cls, *args, \*\*kwargs):
if cls not in cls.\_instances:
cls.\_instances[cls] = super().**call**(*args, \*\*kwargs)
return cls.\_instances[cls]

⸻

🔍 Summary

Aspect **new** **call**
Belongs to Class Metaclass
Controls Instance creation Class instantiation process
Runs when MyClass() is invoked MyClass() is invoked (but before **new**)
Scope Per class Affects all classes using that metaclass
Use case Simple or few singletons (via base class) Framework-level or multiple singletons
Analogy Factory method inside a class Factory method for classes themselves

⸻

✅ In short:
• Use **new** when you just want one class (or a few) to be singletons.
• Use **call** in a metaclass when you want any class with that metaclass to automatically enforce singleton behavior.

⸻
