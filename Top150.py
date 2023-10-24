from collections import deque
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        while n > 0:
            if m > 0 and nums2[n - 1] < nums1[m - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        print(nums1)

    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        if val in nums:
            for i, num in enumerate(nums):
                if num == val:
                    count += 1
                    nums[i] = -1
            nums.sort(reverse=True)

        return len(nums) - count





print(Solution().removeDuplicates([2,2,3]))

#print(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
