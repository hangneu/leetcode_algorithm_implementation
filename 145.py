# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root: return res
        self.dfs(root, res)
        return res
    def dfs(self,root, res):
        if root:
            self.dfs(root.left,res)
            self.dfs(root.right,res)
            res.append(root.val)
