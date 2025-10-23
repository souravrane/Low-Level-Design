from __future__ import annotations
from typing import Dict, Any, Protocol, runtime_checkable
from dataclasses import is_dataclass, replace

@runtime_checkable
class Clonable(Protocol):
    def clone(self) -> Any: ...


class PrototypeRegistry:
    def __init__(self) -> None:
        self._prototypes: Dict[str, Clonable] = {}
    
    def register(self, key: str, prototype: Clonable) -> None:
        self._prototypes[key] = prototype
    
    def unregister(self, key):
        self._prototypes.pop(key, None)
    
    def get(self, key: str, **overrides: Any) -> Any:
        proto = self._prototypes[key]
        if proto is None:
            raise KeyError(f"No prototype registered for key: {key}")
        
        obj = proto.clone()

        # if obj is a dataclass, use replace to override attributes.
        if is_dataclass(obj):
            try:
                return replace(obj, **overrides)
            except TypeError as e:
                for k, v in overrides.items():
                    setattr(obj, k, v)
                return obj
        
        # if generic obj: go with setattr
        for k, v in overrides.items():
            setattr(obj, k, v)
        return obj