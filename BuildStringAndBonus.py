from typing import List


class Solution:

    def build_string(self, s):
        arr = []
        for c in s:
            arr.append(c)

        return "".join(arr)

    def reverseWords(self, s: str) -> str:
        left = right = whiteSpaceIndex = 0
        arr = []

        while right < len(s):
            if s[right] != " " and right != len(s) - 1:
                right += 1
                continue

            whiteSpaceIndex = right

            if right == len(s) - 1:
                arr.append(" ")

            while right >= left:
                arr.append(s[right])
                right -= 1

            left = right = whiteSpaceIndex + 1

        if len("".join(arr)) == len(s) + 1:
            arr.pop(0)

        return "".join(arr)

    def reverseWordsOneLine(self, s: str) -> str:
        print([word[::-1] for word in s.split(" ")])
        return " ".join([word[::-1] for word in s.split(" ")])

    def reverseOnlyLetters(self, s: str) -> str:
        reversed = [c for c in s if c.isalpha()][::-1]

        for i, c in enumerate(s):
            if c.isalpha():
                continue

            reversed.insert(i, c)

        return "".join(reversed)

    def reverseOnlyLettersTwoPointers(self, s: str) -> str:
        arr = list(s)

        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left].isalpha() and arr[right].isalpha():
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
                left += 1
                right -= 1

            elif not arr[left].isalpha():
                left += 1
            elif not arr[right].isalpha():
                right -= 1

        return "".join(arr)

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        found = 0
        for i, num in enumerate(nums):
            while nums[i] == 0 and found < zero_count:
                nums.pop(i)
                nums.append(0)
                found += 1

        print(nums)

    def moveZeroesTwoPointers(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0

        for right in range(1, len(nums)):
            if nums[left] == 0 and nums != 0:
                nums[left], nums[right] = nums[right], nums[left]

            if nums[left] != 0:
                left += 1

        print(nums)

    def reversePrefixTwoPointers(self, word: str, ch: str) -> str:

        if word.find(ch) > -1:
            right = word.index(ch)
            left = 0
            arr = list(word)

            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

            return "".join(arr)

        return word

    def minSubArrayLenSlidingWindow(self, target: int, nums: List[int]) -> int:
        left = cur_sum = 0
        curr = len(nums) + 1

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target and left <= right:
                cur_sum -= nums[left]
                curr = min(curr, right - left + 1)
                left += 1

        return 0 if curr == len(nums) + 1 else curr

    def maxVowelsSlidingWindows(self, s: str, k: int) -> int:
        vowel_letters = ['a', 'e', 'i', 'o', 'u']
        left = right = vowel_count = max_vowel_count = 0

        while right < len(s):

            if s[right] in vowel_letters:
                vowel_count += 1

            if right - left + 1 > k:
                if s[left] in vowel_letters:
                    vowel_count -= 1
                left += 1

            right += 1
            max_vowel_count = max(max_vowel_count, vowel_count)

        return max_vowel_count

    def equalSubstringSlidingWindows(self, s: str, t: str, maxCost: int) -> int:

        max_length = 0
        left = right = cost = 0

        while right < len(s):

            cost += abs(ord(s[right]) - ord(t[right]))

            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length

    def largestAltitudePrefixSum(self, gain: List[int]) -> int:

        prefix_sum = [gain[0]]
        max_altitude = 0 if gain[0] < 0 else gain[0]

        for i in range(1, len(gain)):
            prefix_sum.append(gain[i] + prefix_sum[i - 1])
            max_altitude = max(max_altitude, prefix_sum[i])

        return max_altitude

    def pivotIndexPrefixSum(self, nums: List[int]) -> int:

        prefix_sum = [nums[0]]
        pivot_index = len(nums)

        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i - 1])

        for i in range(len(nums)):

            sum_left = prefix_sum[i] - nums[i]
            sum_right = prefix_sum[len(nums) - 1] - prefix_sum[i]

            if sum_right == sum_left:
                pivot_index = min(pivot_index, i)

        return pivot_index if pivot_index < len(nums) else -1


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [nums[0]]

        for i in range(1, len(nums)):
            self.prefix_sum.append(nums[i] + self.prefix_sum[i - 1])

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]

        return self.prefix_sum[right] - self.prefix_sum[left - 1]


print(NumArray([-2, 0, 3, -5, 2, -1]).sumRange(0, 5))
print(NumArray([-2, 0, 3, -5, 2, -1]).sumRange(2, 5))
# print(Solution().pivotIndexPrefixSum([2,1,-1]))
# print(Solution().largestAltitudePrefixSum([-5,1,5,0,-7]))
# print(Solution().equalSubstringSlidingWindows("abcd", "bcdf", 3))
# print(Solution().maxVowelsSlidingWindows("abciiidef", 3))
# print(Solution().minSubArrayLenSlidingWindow(7, [2,3,1,2,4,3]))
# print(Solution().reversePrefixTwoPointers("abc", "z"))
# print(Solution().moveZeroesTwoPointers([0, 0, 1]))
# print(Solution().moveZeroes([0, 0, 1]))
# print(Solution().reverseOnlyLettersTwoPointers("a-bC-dEf-ghIj"))
# print(Solution().reverseOnlyLetters("ab-cd"))
# print(Solution().reverseWordsOneLine("Let's take LeetCode contest"))
