from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Iterable, List, Tuple, Any
import time
import math

@dataclass
class OpCounter:
    compares: int = 0

class Comparable:
    __slots__ = ("value", "counter")
    def __init__(self, value: int, counter: OpCounter):
        self.value = value
        self.counter = counter
    # Comparaisons
    def _bump(self):
        self.counter.compares += 1
    def __lt__(self, other: "Comparable"):
        self._bump()
        return self.value < other.value
    def __le__(self, other: "Comparable"):
        self._bump()
        return self.value <= other.value
    def __gt__(self, other: "Comparable"):
        self._bump()
        return self.value > other.value
    def __ge__(self, other: "Comparable"):
        self._bump()
        return self.value >= other.value
    def __eq__(self, other: object):
        # Compte seulement si c'est une vraie comparaison
        if isinstance(other, Comparable):
            self._bump()
            return self.value == other.value
        return False
    def __repr__(self):
        return f"Comparable({self.value})"

def wrap_with_counter(lst: Iterable[int], counter: OpCounter) -> list[Comparable]:
    return [Comparable(x, counter) for x in lst]

def unwrap(lst: Iterable[Comparable]) -> list[int]:
    return [x.value for x in lst]

def time_call(fn: Callable, *args, repeats: int = 5, warmup: int = 1) -> float:
    # chauffe
    for _ in range(warmup):
        fn(*args)
    best = math.inf
    for _ in range(repeats):
        t0 = time.perf_counter()
        fn(*args)
        dt = time.perf_counter() - t0
        if dt < best:
            best = dt
    return best

def bench_sort(fn: Callable[[list[Any]], list[Any]], data: list[int], repeats: int = 5) -> tuple[float, int]:
    counter = OpCounter()
    wrapped = wrap_with_counter(data, counter)
    def run():
        res = fn(wrapped)
        # s'assurer que l'algo retourne bien une liste sortable
        return res
    elapsed = time_call(run, repeats=repeats)
    return elapsed, counter.compares
