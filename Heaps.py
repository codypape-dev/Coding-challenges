import heapq
from collections import Counter
from collections import deque
from math import floor
from typing import List


class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (self.min_heap[0] - self.max_heap[0]) / 2


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Stones[i] is the weight of the ith stone
        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))

            if first != second:
                heapq.heappush(stones, -abs(first - second))

        # return the weight of the last remaining stone
        return -stones[0] if stones else 0

    def halveArray(self, nums: List[int]) -> int:
        # reduce the sum by at least half, halving any number on the list
        heap = [- num for num in nums]
        target = sum(nums) / 2
        heapq.heapify(heap)

        ans = 0
        while target > 0:
            ans += 1
            x = heapq.heappop(heap)
            target += x / 2
            heapq.heappush(heap, x / 2)
        return ans

    def minStoneSum(self, piles: List[int], k: int) -> int:
        def remove_stones():
            for i in range(k):
                # apply removal k times to heap[0] (max number of stones)
                new_amount = heapq.heappop(heap)
                new_amount = floor(new_amount / 2)
                heapq.heappush(heap, new_amount)

        # piles[i] number of stones in the ith pile
        # numer of times to remove floor(piles[i] / 2) in any chosen pile
        # return minimum possible number of stones remaining after k removals
        # I have to remove the maximum amount of stones from the piles in k removals
        # I have to keep track of the pile with maximum number of stones and remove from it
        # create a heap to track max
        heap = [- num for num in piles]
        heapq.heapify(heap)
        remove_stones()
        return - sum(heap)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []

        for key, val in counts.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [pair[1] for pair in heap]

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for num in arr:
            distance = abs(x - num)
            heapq.heappush(heap, (-distance, -num))
            if len(heap) > k:
                heapq.heappop(heap)

        return sorted([-pair[1] for pair in heap])

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)

        return heapq.nlargest(k, nums)[-1]


print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.k_largest = nums
        heapq.heapify(self.k_largest)
        while len(self.k_largest) > self.k:
            heapq.heappop(self.k_largest)

    def add(self, val: int) -> int:

        if len(self.k_largest) < self.k:
            heapq.heappush(self.k_largest, val)
            return self.k_largest[0]

        if val > self.k_largest[0]:
            heapq.heappushpop(self.k_largest, val)

        return self.k_largest[0]

    # Your KthLargest object will be instantiated and called as such:


"""
kthLargest = KthLargest(3, [5, -1])
print(kthLargest.add(2))
print(kthLargest.add(1))
print(kthLargest.add(-1))
print(kthLargest.add(3))
print(kthLargest.add(4))
"""
