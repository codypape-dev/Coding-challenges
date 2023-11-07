from collections import defaultdict
from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, i):
            if i > len(nums):
                return

            ans.append(curr[:])
            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(curr, j + 1)
                curr.pop()

        ans = []
        backtrack([], 0)
        return ans

    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, i):
            if len(curr) == k:
                ans.append(curr[:])
                return

            for num in range(i, n + 1):
                curr.append(num)
                backtrack(curr, num + 1)
                curr.pop()

        ans = []
        backtrack([], 1)
        return ans

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(curr, i):
            if i == target:
                ans.append(curr[:])
                return

            for j in graph[i]:
                curr.append(j)
                backtrack(curr, j)
                curr.pop()

        target = len(graph) - 1
        ans = []
        backtrack([0], 0)
        return ans

    def letterCombinations(self, digits: str) -> List[str]:
        letters_dict = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        ans = []

        def backtrack(curr, i):
            if i == len(digits):
                ans.append(curr)
                return

            for letter in letters_dict[digits[i]]:
                backtrack(curr + letter, i + 1)

        if digits: backtrack("", 0)
        return ans

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(path, start, curr):
            if curr == target:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                if curr + num <= target:
                    path.append(num)
                    backtrack(path, i, curr + num)
                    path.pop

        ans = []
        backtrack([], 0, 0)
        return ans

    def generateParenthesis1(self, n: int) -> List[str]:
        def backtrack(curr, i):
            if i == n:
                ans.add(curr)
                return

            backtrack('(' + curr + ')', i + 1)
            backtrack('()' + curr, i + 1)
            backtrack(curr + '()', i + 1)

        ans = set()
        if n: backtrack('', 0)
        return ans

    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def backtracking(cur_string, left_count, right_count):
            if len(cur_string) == 2 * n:
                answer.append("".join(cur_string))
                return
            if left_count < n:
                cur_string.append("(")
                backtracking(cur_string, left_count + 1, right_count)
                cur_string.pop()
            if right_count < left_count:
                cur_string.append(")")
                backtracking(cur_string, left_count, right_count + 1)
                cur_string.pop()

        backtracking([], 0, 0)
        return answer

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = set()

        def dfs(curr):
            if len(curr) == n and int(curr) not in ans:
                ans.add(int(curr))
                return

            add_k = int(curr[-1]) + k
            subs_k = int(curr[-1]) - k

            if 0 <= add_k < 10:
                dfs(curr + str(add_k))
            if 0 <= subs_k < 10:
                dfs(curr + str(subs_k))

        for i in range(1, 10):
            dfs(str(i))

        return list(ans)

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        directions = {(0, 1), (1, 0), (-1, 0), (0, -1)}
        ans = False
        def valid_cell(x, y):
            return 0 <= x < m and 0 <= y < n

        def explore_edges(x, y, k, seen: set):
            print(x,y,k)
            if k == len(word):
                return True
            if word[k] == board[x][y]:

                seen.add((x, y))
                for i, j in directions:
                    new_x = x + i
                    new_y = y + j

                    if valid_cell(new_x, new_y) and (new_x, new_y) not in seen:
                        return explore_edges(new_x, new_y, k + 1, seen)

        print (explore_edges(1,3,0,set()))

        return ans


print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
