import math
from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic:  # This operation is O(1)!
                return [i, dic[complement]]

            dic[num] = i

        return [-1, -1]

    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)

        return " "

    def find_numbers(nums):
        ans = []
        nums = set(nums)

        for num in nums:
            if (num + 1 not in nums) and (num - 1 not in nums):
                ans.append(num)

        return ans

    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        for c in sentence:
            if c in seen:
                continue
            seen.add(c)

        return True if len(seen) == 26 else False

    def missingNumber(self, nums: List[int]) -> int:
        '''
        nums_set = set(nums)

        for i in range(len(nums) + 1):
            if i in nums_set:
                continue
            return i
        '''
        set_num = set(nums)
        full = set(range(0, len(nums) + 1))
        return full.difference(set_num).pop()

    def countElements(self, arr: List[int]) -> int:
        arr_set = set(arr)
        count = 0

        for i in arr:
            if i + 1 in arr_set:
                count += 1

        return count

    def find_longest_substring(s, k):
        counts = defaultdict(int)
        left = ans = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            while len(counts) > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1

            ans = max(ans, right - left + 1)

        return ans

    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        for arr in nums:
            for x in arr:
                counts[x] += 1

        n = len(nums)
        ans = []
        for key in counts:
            if counts[key] == n:
                ans.append(key)

        return sorted(ans)

    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1

        frequencies = counts.values()
        return len(set(frequencies)) == 1

    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1

        return ans

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num % 2
            ans += counts[curr - k]
            counts[curr] += 1

        return ans

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        match_losses = defaultdict(int)
        for match in matches:
            match_losses[match[0]] += 0
            match_losses[match[1]] += 1

        ans = [[], []]
        ans[0] = sorted(player for player, losses in match_losses.items() if losses == 0)
        ans[1] = sorted(player for player, losses in match_losses.items() if losses == 1)

        return ans

    def largestUniqueNumber(self, nums: List[int]) -> int:
        count_dic = {}
        count_dic.update({-1: 1})

        for i in nums:
            curr_value = count_dic.get(i, 0)
            count_dic.update({i: curr_value + 1})

        return max(number for number, value in count_dic.items() if value == 1)

    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_dic = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for c in text:
            if c in balloon_dic:
                curr_value = balloon_dic.get(c, 0)
                balloon_dic.update({c: curr_value + 1})

        balloon_dic['l'] //= 2
        balloon_dic['o'] //= 2

        return min(balloon_dic.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)

        return groups.values()

    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = defaultdict(list)
        for i in range(len(cards)):
            dic[cards[i]].append(i)

        ans = float("inf")
        for key in dic:
            arr = dic[key]
            for i in range(len(arr) - 1):
                ans = min(ans, arr[i + 1] - arr[i] + 1)

        return ans if ans < float("inf") else -1

    def maximumSum(self, nums: List[int]) -> int:

        def digitSum(num: int) -> int:
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10

            return digit_sum

        digit_sum_dic = {}
        ans = 0
        for i in nums:
            curr_sum = digitSum(nums[i])
            if curr_sum in digit_sum_dic:
                ans = max(ans, i + digit_sum_dic[curr_sum])
            digit_sum_dic[curr_sum] = max(digit_sum_dic[curr_sum], i)

        return ans

    def equalPairs(self, grid: List[List[int]]) -> int:
        def convert_to_key(arr):
            return tuple(arr)

        dic = defaultdict(int)
        for row in grid:
            dic[convert_to_key(row)] += 1

        dic2 = defaultdict(int)
        for col in range(len(grid[0])):
            current_col = []
            for row in range(len(grid)):
                current_col.append(grid[row][col])

            dic2[convert_to_key(current_col)] += 1

        ans = 0
        for arr in dic:
            ans += dic[arr] * dic2[arr]

        return ans

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_tuple = tuple(magazine)
        ransom_tuple = tuple(ransomNote)

        for c in set(ransomNote):
            if ransom_tuple.count(c) > magazine_tuple.count(c):
                return False

        return True

    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewels_owned = 0
        for stone in stones:
            if stone in set(jewels):
                jewels_owned += 1

        return jewels_owned

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = left = 0
        substring_dic = {}

        for right in range(len(s)):

            if s[right] in substring_dic:
                left = max(left, substring_dic[s[right]] + 1)

            substring_dic[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length

    def containsDuplicate(self, nums: List[int]) -> bool:

        nums_set = set(nums)

        if len(nums) > len(nums_set):
            return True

        return False

    def destCity(self, paths: List[List[str]]) -> str:

        end_set = set()
        start_set = set()

        for path in paths:
            start_set.add(path[0])
            end_set.add(path[1])

        return end_set.difference(start_set).pop()

    def isPathCrossing(self, path: str) -> bool:
        curr_point = [0, 0]
        path_set = set()
        path_set.add(tuple(curr_point))

        for move in path:
            match move:
                case "N":
                    curr_point[0] += 1
                case "S":
                    curr_point[0] -= 1
                case "E":
                    curr_point[1] += 1
                case "W":
                    curr_point[1] -= 1

            if tuple(curr_point) in path_set:
                return True

            path_set.add(tuple(curr_point))

        return False
    
print(Solution().isPathCrossing("NESWW"))
#print(Solution().destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
# print(Solution().lengthOfLongestSubstring("abba"))
# print(Solution().canConstruct("aac", "aaab"))
# print(Solution().maxNumberOfBalloons("loonbalxballpoon"))
# print(Solution().maxNumberOfBalloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"))
# print(Solution().largestUniqueNumber([5,7,3,9,4,9,8,3,1]))
# print(Solution().largestUniqueNumber([9,9,8,8]))
# print(Solution().findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
# print(Solution().countElements([1, 2, 3]))
# print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))
# print(Solution().checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
