from collections import deque
from typing import List


class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        self.queue.append(t)
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size

    def next(self, val: int) -> float:
        sum = 0
        self.queue.append(val)

        while len(self.queue) > self.size:
            self.queue.popleft()

        min_size = min(self.size, len(self.queue))

        for i in self.queue:
            sum += i

        return sum/min_size

class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = []
        queue = deque()

        for i in range(len(nums)):

            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            if queue[0] + k == i:
                queue.popleft()

            if i >= k - 1:
                stack.append(nums[queue[0]])

        return stack

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = deque()
        decreasing = deque()
        left = ans = 0

        for right in range(len(nums)):
            # maintain the monotonic deques
            while increasing and increasing[-1] > nums[right]:
                increasing.pop()
            while decreasing and decreasing[-1] < nums[right]:
                decreasing.pop()

            increasing.append(nums[right])
            decreasing.append(nums[right])

            # maintain window property
            while decreasing[0] - increasing[0] > limit:
                if nums[left] == decreasing[0]:
                    decreasing.popleft()
                if nums[left] == increasing[0]:
                    increasing.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        for i in range(len(nums1)):
            queue = deque()





# Your MovingAverage object will be instantiated and called as such:
'''obj = MovingAverage(3)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))'''

#print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))