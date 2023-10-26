# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        ans = []

        while queue:
            current_length = len(queue)
            max_value = float("-inf")
            for _ in range(current_length):
                node = queue.popleft()
                max_value = max(max_value, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(max_value)

        return ans


root = TreeNode(1)
one = TreeNode(3)
two = TreeNode(2)
three = TreeNode(5)
four = TreeNode(3)
five = TreeNode(9)
six = TreeNode(13)

five.right = None
two.right = five
one.right = four
one.left = three
root.left = one
root.right = two

print(Solution().largestValues(root))
