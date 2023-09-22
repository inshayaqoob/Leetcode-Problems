# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_path):
            if not node:
                return 0
            current_path = current_path * 10 + node.val
            if not node.left and not node.right:
                return current_path
            left_sum = dfs(node.left, current_path)
            right_sum = dfs(node.right, current_path)
            return left_sum + right_sum

        return dfs(root, 0)