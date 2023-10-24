from typing import List
from decimal import *


class Solution:
    def find_length(self, nums, k):
        left = curr = ans = 0
        for right in range(len(nums)):
            curr += nums[right]
            while curr > k:
                curr -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)

        return ans

    def find_length(self, s: str) -> int:
        left = current = ans = 0
        for right in range(len(s)):
            if s[right] == "0":
                current += 1

            while current > 1:
                if s[left] == "0":
                    current -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = left = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1

        return ans

    def find_best_subarray(nums, k):
        curr = 0
        for i in range(k):
            curr += nums[i]

        ans = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr)

        return ans

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        for i in range(k):
            curr += nums[i]

        ans = curr / k
        for i in range(k, len(nums)):
            curr += (nums[i] - nums[i - k])
            ans = max(ans, curr / k)

        return ans

    def longestOnes(self, nums: List[int], k: int) -> int:
        left = ans = current = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                current += 1

            while current > k:
                if nums[left] == 0:
                    current -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans


print(Solution().longestOnes([0,0,0,0,0],0))
# print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))
