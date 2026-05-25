def three_sum_two_pointers(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    for i, num in enumerate(nums):
        # Skip the same value to avoid duplicate triplets
        if i > 0 and num == nums[i - 1]:
            continue

        # Use two pointers for the remaining part of the array
        left, right = i + 1, len(nums) - 1
        while left < right:
            three_sum = num + nums[left] + nums[right]
            if three_sum > 0:
                right -= 1  # Sum too large, move right pointer left
            elif three_sum < 0:
                left += 1  # Sum too small, move left pointer right
            else:
                res.append([num, nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicates for the left pointer
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return res


def three_sum_hashset(nums: list[int]) -> list[list[int]]:
    res = set()
    nums.sort()  # Sorting helps in handling duplicates easily

    for i in range(len(nums)):
        # Optimization: If the current number is > 0, no triplet can sum to 0
        if nums[i] > 0:
            break
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        seen = set()
        for j in range(i + 1, len(nums)):
            complement = -nums[i] - nums[j]
            if complement in seen:
                # Found a triplet! Use a tuple so it can be added to the result set
                res.add((nums[i], complement, nums[j]))

                # To avoid duplicates in the inner loop, skip same values
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])

    return [list(triplet) for triplet in res]


def three_sum_hashset_no_sort(nums: list[int]) -> list[list[int]]:
    res = set()
    seen = set()

    for i in range(len(nums)):
        if nums[i] in seen:
            continue
        seen.add(nums[i])

        # Find Two Sum for the remainder of the array
        target = -nums[i]
        visited = set()

        for j in range(i + 1, len(nums)):
            complement = target - nums[j]
            if complement in visited:
                triplet = tuple(sorted([nums[i], nums[j], complement]))
                res.add(triplet)
            visited.add(nums[j])

    return [list(t) for t in res]
