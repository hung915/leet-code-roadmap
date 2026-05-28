def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        # Calculate width and height
        width = right - left
        current_height = min(height[left], height[right])

        # Update maximum area
        max_area = max(max_area, width * current_height)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
