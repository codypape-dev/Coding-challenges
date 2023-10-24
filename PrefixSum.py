from typing import List


class Solution:

    def answer_queries(self, nums, queries, limit):
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        ans = []
        for x, y in queries:
            curr = prefix[y] - prefix[x] + nums[x]
            ans.append(curr < limit)

        return ans

    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])

        ans = 0
        for i in range(n - 1):
            left_section = prefix[i]
            right_section = prefix[-1] - prefix[i]
            if left_section >= right_section:
                ans += 1

        return ans

    def waysToSplitArrayInt(self, nums: List[int]) -> int:
        ans = left_section = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left_section += nums[i]
            right_section = total - left_section
            if left_section >= right_section:
                ans += 1

        return ans

    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        sum = nums[0]

        for i in range(1, len(nums)):
            sum += nums[i]
            ans.append(sum)

        return ans

    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1 if nums[0] > 0 else abs(nums[0]) + 1
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] + nums[i])

        for i in range(0, len(prefix)):

            while prefix[i] + startValue < 1:
                startValue += 1

        return startValue

    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avgs = [-1] * len(nums)
        prefixSum = [nums[0]]

        for i in range(1, len(nums)):
            prefixSum.append(nums[i] + prefixSum[i - 1])

        total = (k * 2 + 1)
        curr = k

        while curr < len(nums) - k:
            if curr - k > 0:
                avgs[curr] = (prefixSum[curr + k] - prefixSum[curr + k - total]) // total
            else:
                avgs[k] = prefixSum[k * 2] // total

            curr += 1

        return avgs


print(Solution().getAverages([8], 1000))
# print(Solution().minStartValue([2,3,5,-5,-1]))
# print(Solution().runningSum([1,1,1,1,1]))
