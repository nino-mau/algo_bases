import time
from typing import Any, Callable, Tuple
from ex03_fonctions_algo.src.exercices import (
    print_hello_world,
    reverse_string,
    to_uppercase,
    count_substring,
    list_length,
    max_in_list,
    pgcd,
    fibonacci,
    crible_eratosthene,
    is_prime,
    is_palindrome,
    binary_search,
    gcd_recursive,
    fibonacci_recursive,
    is_palindrome_recursive,
    is_prime_recursive,
    factorial_recursive,
)


def measure_time(func: Callable, *args, **kwargs) -> Tuple[Any, float]:
    """
    Mesure le temps d'exécution d'une fonction.

    Args:
        func (Callable): La fonction à exécuter.
        *args: Les arguments positionnels pour la fonction.
        **kwargs: Les arguments nommés pour la fonction.

    Returns:
        Tuple contenant :
            - le résultat de la fonction
            - le temps d'exécution en secondes (float)
    """
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    elapsed = end - start
    print(result, elapsed)
    return result, elapsed


print("fibonacci_recursive:")
measure_time(fibonacci_recursive, 10)
print()
print("fibonacci:")
measure_time(fibonacci, 10)
print()
print("is_prime_recursive:")
measure_time(is_prime_recursive, 10)
print()
print("is_prime:")
measure_time(is_prime, 10)
print("")
