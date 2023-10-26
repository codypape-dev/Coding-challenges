from collections import deque, defaultdict
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

    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                count += 1
                nums[i] = 200
        nums.sort()
        return len(nums) - count

    def removeDuplicates2(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        print(nums)
        return j

    def remove2Duplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return len(nums)
        count = 0
        left = 0
        current = 1

        for right in range(2, len(nums)):
            if nums[left] == nums[right] == nums[current]:
                count += 1
                nums[left] = 1000000
            left += 1
            current += 1
        nums.sort()
        print(nums)
        return len(nums) - count

print(Solution().remove2Duplicates([0,0,1,1,1,1,2,3,3]))

#print(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
