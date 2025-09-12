from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class Node:
    value: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None

def exemple_arbre() -> Node:
    d = Node("D")
    e = Node("E")
    f = Node("F")
    b = Node("B", d, e)
    c = Node("C", None, f)
    a = Node("A", b, c)
    return a
