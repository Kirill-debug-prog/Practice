from typing import Callable, Any

even: Callable[[Any], bool] = lambda n: True if n % 2 == 0 else False
print(even(12))
print(even(17))
