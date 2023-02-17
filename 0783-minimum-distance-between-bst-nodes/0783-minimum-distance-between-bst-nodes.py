# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = []
        heapify(res)
        stack = [root]
        while stack:
            node = stack.pop(0)
            heappush(res, node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        s = float('inf')
        prev = 10000000
        while res:
            a = heappop(res)
            s = min(s, abs(prev - a))
            prev = a
        
        return s