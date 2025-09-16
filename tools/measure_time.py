import time
from typing import Any, Callable, Tuple

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
    return result, elapsed
