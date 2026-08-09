# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mode = -1
        res = []
        treeCount = Counter()
        self.traverse(root, treeCount)

        # mode = max(treeCount, key=treeCount.get)
        mode = max(treeCount.values())

        for k, v in treeCount.items():
            if mode == v:
                res.append(k)

        return res

    def traverse(self, root, treeCount):
        if root:
            self.traverse(root.left, treeCount)
            treeCount[root.val] += 1
            self.traverse(root.right, treeCount)