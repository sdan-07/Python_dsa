# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q = collections.deque()
        q.append(root)
        # flag for right to left
        left_to_right = True

        while q:
            level=[]
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    if left_to_right:
                        level.append(node.val)
                    else:
                        level.insert(0, node.val)

                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

            left_to_right = not left_to_right

        return res
