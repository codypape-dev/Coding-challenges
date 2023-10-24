from collections import deque
from typing import Optional, List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def PrintTree(self):
        if not self:
            return []
        queue = deque([self])
        ans = []

        while queue:
            current_length = len(queue)
            row = []

            for _ in range(current_length):
                node = queue.popleft()
                row.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(row)

        return ans


class Solution:

    def max_dfs(self, node: TreeNode, x) -> int:
        if node == None:
            return x

        x += 1
        left = self.max_dfs(node.left, x)
        right = self.max_dfs(node.right, x)
        return max(left, right)

    def min_dfs(self, node: TreeNode) -> int:
        if node is None:
            return 0

        if node.left is None:
            return self.min_dfs(node.right) + 1

        elif node.right is None:
            return self.min_dfs(node.left) + 1

        return min(self.min_dfs(node.left), self.min_dfs(node.right)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.max_dfs(root, 0)

    def minDepth(self, root: Optional[TreeNode]) -> int:

        return self.min_dfs(root)

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        self.result = 0

        def search_limits(node, cur_max, cur_min):
            if node is None:
                return

            self.result = max(self.result, abs(cur_max - node.val),
                              abs(cur_min - node.val))
            # update the max and min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            search_limits(node.left, cur_max, cur_min)
            search_limits(node.right, cur_max, cur_min)

        search_limits(root, root.val, root.val)
        return self.result

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.diameter = 0

        def longest_path(node: Optional[TreeNode]):
            if node is None:
                return 0

            left = longest_path(node.left)
            right = longest_path(node.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1

        longest_path(root)
        return self.diameter

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        ans = []

        while queue:
            current_length = len(queue)
            ans.append(queue[-1].val)

            for _ in range(current_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = deque([root])

        while queue:
            current_length = len(queue)
            curr_max = float("-inf")

            for _ in range(current_length):
                node = queue.popleft()
                curr_max = max(curr_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(curr_max)
        return ans

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return root.val

        curr_sum = 0
        queue = deque([root])

        while queue:
            current_length = len(queue)
            curr_sum = 0
            for _ in range(current_length):
                node = queue.popleft()
                curr_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return curr_sum

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        switch = False
        ans = []

        while queue:
            current_length = len(queue)
            row = []

            for _ in range(current_length):
                node = queue.popleft()
                row.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if switch:
                row.reverse()

            ans.append(row)
            switch = not switch

        return ans

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return

            left = dfs(node.left)
            values.append(node.val)
            right = dfs(node.right)

        values = []
        dfs(root)
        ans = float("inf")
        for i in range(1, len(values)):
            ans = min(ans, values[i] - values[i - 1])

        return ans

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        # inorder traverse the tree
        def dfs(node: TreeNode):
            if not node:
                return

            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        values = []
        dfs(root)

        minDiff = float("inf")
        minValue = 10000000
        for i in range(0, len(values)):
            if minDiff > abs(target - values[i]):
                minDiff = abs(target - values[i])
                minValue = values[i]
            elif minDiff == abs(target - values[i]):
                minValue = min(minValue, values[i])

        return minValue


root = TreeNode(1)
one = None
two = TreeNode(2)
three = TreeNode(1)
four = TreeNode(3)
five = TreeNode(11)
six = TreeNode(13)

# five.right = six
# two.right = five
# one.right = four
# one.left = three
#root.left = one
#root.right = two

#print(Solution().closestValue(root, 3.4))
