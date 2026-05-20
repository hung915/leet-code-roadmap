def product_except_self_left_right_product_lists(nums: list[int]) -> list[int]:
    length = len(nums)

    left_product_list = [1] * length
    right_product_list = [1] * length
    result = []

    for i in range(1, length):
        left_product_list[i] = left_product_list[i - 1] * nums[i - 1]

    for i in range(length - 2, -1, -1):
        right_product_list[i] = right_product_list[i + 1] * nums[i + 1]

    for i in range(length):
        result.append(left_product_list[i] * right_product_list[i])

    return result


def product_except_self_left_right_product_lists_o1_space(nums: list[int]) -> list[int]:
    length = len(nums)

    result = [1] * length

    for i in range(1, length):
        result[i] = result[i - 1] * nums[i - 1]

    right = 1
    for i in range(length - 1, -1, -1):
        result[i] *= right
        right *= nums[i]
    return result
