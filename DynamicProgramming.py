from typing import List


class Solution:
    def minCostClimbingStairsTopDown(self, cost: List[int]) -> int:
        # 1. A function that returns the answer
        def dp(i):
            if i <= 1:
                # 3. Base cases
                return 0

            if i in memo:
                return memo[i]

            # 2. Recurrence relation
            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            return memo[i]

        memo = {}
        return dp(len(cost))

    def minCostClimbingStairsBottomUp(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            # 2. Recurrence relation
            dp[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])

        return dp(n)

    def longestCommonSubsequenceTopDown(self, text1: str, text2: str) -> int:
        @cache
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1)

            return max(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)

    def longestCommonSubsequenceBottomUp(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]

    def climbStairsTopBottom(self, n: int) -> int:
        def dp(i):
            if i in memo:
                return memo[i]
            if i == 0:
                return 0
            if i == 1:
                return 1
            elif i == 2:
                return 2

            memo[i] = dp(i - 2) + dp(i - 1)
            return memo[i]

        memo = {}
        return dp(n)

    def climbingStairsBottomUp(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n - 1]

    def minCostClimbingStairsTopDown(self, cost: List[int]) -> int:
        def dp(i):
            if i in memo:
                return memo[i]
            if i <= 1:
                return 0

            down_one = cost[i - 1] + dp(i - 1)
            down_two = cost[i - 2] + dp(i - 2)
            memo[i] = min(down_one, down_two)
            return memo[i]

        memo = {}
        return dp(len(cost))

print(Solution().minCostClimbingStairsTopDown([10,15,20]))