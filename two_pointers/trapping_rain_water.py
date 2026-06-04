def trap_brute_force(height: list[int]) -> int:
    n, total = len(height), 0

    for i in range(n):
        max_left = 0
        for j in range(i, -1, -1):
            max_left = max(max_left, height[j])

        max_right = 0
        for k in range(i, n):
            max_right = max(max_right, height[k])

        water = min(max_left, max_right) - height[i]
        total += water

    return total


def trap_dynamic_programming(height: list[int]) -> int:
    n, total = len(height), 0

    for i in range(n):
        max_left = 0
        for j in range(i, -1, -1):
            max_left = max(max_left, height[j])

        max_right = 0
        for k in range(i, n):
            max_right = max(max_right, height[k])

        water = min(max_left, max_right) - height[i]
        total += water

    return total
