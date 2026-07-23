class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class BST:
    # initialization of root pointer
    def __init__(self):
        self.root=None
    # insert method
    def insert(self, data):
        self.root = self.rec_insert(self.root, data)

    def rec_insert(self, root, data):
        if root is None:
            return Node(data)
        elif root.val < data:
            root.right = self.rec_insert(root.right, data)
        else:
            root.left = self.rec_insert(root.left, data)
        return root

    # search method
    def search(self, root, data):
        self.root = self.rec_search(self.root, data)

    def rec_search(self, root, data):
        if root is None:
            return None
        if root.val == data:
            return root
        elif root.val < data:
            return self.rec_search(root.right, data)
        else:
            return self.rec_search(root.left, data)

#   traversal
#   inorder
    def inorder(self):
        result = []
        self.rec_inorder(self.root, result)
        return result

    def rec_inorder(self, root, result):
        if root:
            self.rec_inorder(root.left, result)
            result.append(root.val)
            self.rec_inorder(root.right, result)

#   preorder
    def preorder(self):
        result = []
        self.rec_preorder(self.root, result)
        return result

    def rec_preorder(self, root, result):
        if root:
            result.append(root.val)
            self.rec_preorder(root.left, result)
            self.rec_preorder(root.right, result)

#   postorder
    def postorder(self):
        result = []
        self.rec_postorder(self.root, result)
        return result

    def rec_postorder(self, root, result):
        if root:
            self.rec_postorder(root.left, result)
            self.rec_postorder(root.right, result)
            result.append(root.val)

def main():
    nodes=[50, 40, 60, 30, 45, 55, 75]
    tree = BST()
    for node in nodes:
        tree.insert(node)

    result = tree.inorder()
    print(result)

main()