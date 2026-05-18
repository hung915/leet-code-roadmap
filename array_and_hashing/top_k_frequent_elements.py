import heapq
import random
from collections import Counter


def top_k_frequent_heap(nums: list[int], k: int) -> list[int]:
    # 1. Build hash map: character and how often it appears
    # O(N) time
    count = Counter(nums)
    if k > len(count):
        return list(count.keys())
    # 2-3. Build heap of top k frequent elements and
    # convert it into an output array
    # O(N log k) time
    return heapq.nlargest(k, count.keys(), key=count.get)


def top_k_frequent_quickselect(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    unique = list(count.keys())

    if k > len(unique):
        return unique

    def partition(left: int, right: int, pivot_index: int) -> int:
        pivot_frequency = count[unique[pivot_index]]
        # 1. Move the pivot to end
        unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

        # 2. Move all less frequent elements to the left
        store_index = left
        for i in range(left, right):
            if count[unique[i]] < pivot_frequency:
                unique[store_index], unique[i] = unique[i], unique[store_index]
                store_index += 1

        # 3. Move the pivot to its final place
        unique[right], unique[store_index] = unique[store_index], unique[right]

        return store_index

    def quickselect(left: int, right: int, k_smallest: int) -> None:
        """
        Sort a list within left..right till kth less frequent element
        takes its place.
        """
        # base case: the list contains only one element
        if left == right:
            return

        # Select a random pivot_index
        pivot_index = random.randint(left, right)  # noqa: S311

        # Find the pivot position in a sorted list
        pivot_index = partition(left, right, pivot_index)

        # If the pivot is in its final sorted position
        if k_smallest == pivot_index:
            return
        # go left
        elif k_smallest < pivot_index:
            quickselect(left, pivot_index - 1, k_smallest)
        # go right
        else:
            quickselect(pivot_index + 1, right, k_smallest)

    n = len(unique)
    # kth top frequent element is (n - k)th less frequent.
    # Do a partial sort: from less frequent to the most frequent, till (n - k)th less frequent element takes its place (n - k) in a sorted array.
    # All elements on the left are less frequent.
    # All the elements on the right are more frequent.
    quickselect(0, n - 1, n - k)
    # Return top k frequent elements
    return unique[n - k :]


print(top_k_frequent_quickselect([1, 2, 1, 2, 1, 2, 3, 1, 3, 2, 4, 5, 6, 6], 3))
