def contains_duplicate_set(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if nums in seen:
            return True
        seen.add(num)
    return False


def contains_duplicate_sort(nums: list[int]) -> bool:
    nums = nums.sort()

    return any(nums[i] == nums[i - 1] for i in range(1, len(nums)))
