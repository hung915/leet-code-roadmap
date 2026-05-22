import random
from collections import Counter


def majority_element_hashmap(nums: list[int]) -> int:
    counter = Counter(nums)
    return max(counter, key=counter.get)


def majority_element_boyer_moore(nums: list[int]) -> int:
    candidate, count = None, 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if candidate == num else -1
    return candidate


def majority_element_sort(nums: list[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]


def majority_element_random(nums: list[int]) -> int:
    n = len(nums)

    while True:
        candidate = random.choice(nums)  # noqa: S311

        if nums.count(candidate) > n // 2:
            return candidate


def majority_element_bit_manipulation(nums: list[int]) -> int:
    n = len(nums)
    majority = 0

    for i in range(32):
        bit = 1 << i
        bit_count = 0

        for num in nums:
            if num & bit:
                bit_count += 1

        if bit_count > n // 2:
            majority |= bit

    # Handle negative numbers — convert from unsigned 32-bit to signed
    if majority >= (1 << 31):  # if sign bit is set
        majority -= 1 << 32  # convert to negative
    return majority
