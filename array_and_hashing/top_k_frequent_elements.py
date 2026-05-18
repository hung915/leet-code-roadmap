import heapq
import secrets
from collections import Counter


def top_k_frequent_heap(nums: list[int], k: int) -> list[int]:
    # 1. Build hash map: character and how often it appears
    # O(N) time
    count = Counter(nums)
    if k >= len(count):
        return list(count.keys())
    # 2-3. Build heap of top k frequent elements and
    # convert it into an output array
    # O(N log k) time
    return heapq.nlargest(k, count.keys(), key=count.get)


def top_k_frequent_quickselect(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    unique = list(count.keys())
    n = len(unique)

    if k >= n:
        return unique

    def _partition(left: int, right: int, pivot_index: int) -> int:
        pivot_freq = count[unique[pivot_index]]
        unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

        store_index = left
        for i in range(left, right):
            if count[unique[i]] < pivot_freq:  # tần suất thấp hơn → đẩy sang trái
                unique[i], unique[store_index] = unique[store_index], unique[i]
                store_index += 1
        unique[right], unique[store_index] = unique[store_index], unique[right]
        return store_index

    def _quickselect(left: int, right: int, k_smallest: int) -> None:
        pivot_index = secrets.randbelow(right - left + 1) + left

        pivot_index = _partition(left, right, pivot_index)

        if pivot_index == k_smallest:
            return
        elif pivot_index > k_smallest:
            # go left
            _quickselect(left, pivot_index - 1, k_smallest)
        else:
            # go right
            _quickselect(pivot_index + 1, right, k_smallest)

    _quickselect(0, n - 1, n - k)

    return unique[n - k :]
