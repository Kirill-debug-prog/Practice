from typing import Callable, Any

num = [1, 3, 6, 8, 4]
meaning: Callable[[Any], float | Any] = lambda nums: sum(nums) / len(nums)
print(meaning(num))
