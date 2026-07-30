class Node:
    def __init__(self, val=None, left=None, right=None):
        self.left=left
        self.right=right
        self.val=val
class BST:
    def __init__(self):
        self.root = None
    #  insertion
    def insert(self, data):
        self.root = self.rec_insert(self.root, data)

    def rec_insert(self, root, data):
        if not root:
            return Node(data)
        elif root.val > data:
            root.left = self.rec_insert(root.left, data)
        elif root.val < data:
            root.right = self.rec_insert(root.right, data)
        else:
            return "Cannot insert same node value"
        return root

    # searching
    def search(self, key):
        if not self.root:
            return False
        return self.rec_search(self.root, key)

    def rec_search(self, root, key):
        if not root:
            return False
        elif root.val < key:
            return self.rec_search(root.right, key)
        elif root.val > key:
            return self.rec_search(root.left, key)
        else:
            return True


    #inorder traversal
    def inorder(self):
        res = []
        self.rec_inorder(self.root, res)
        return res

    def rec_inorder(self, root, res):
        if root:
            self.rec_inorder(root.left, res)
            res.append(root.val)
            self.rec_inorder(root.right, res)


    # deletion
    def delete(self, data):
        self.root = self.rec_delete(self.root, data)

    def rec_delete(self, root, data):
        if not root:
            return root

        if root.val > data:
            root.left = self.rec_delete(root.left, data)
        elif root.val < data:
            root.right = self.rec_delete(root.right, data)
        else:
            # no child
            if not root.left and not root.right:
                return None
            # single child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # two children
            pred = root.left
            while pred.right:
                pred = pred.right

            root.val = pred.val
            root.left = self.rec_delete(root.left, pred.val)
        return root


if __name__ == "__main__":
    tree = BST()
    vals = [40, 80, 10, 60, 70]
    for val in vals:
        tree.insert(val)
    print("Before:\n",tree.inorder())

    tree.delete(10)
    tree.delete(40)
    print("After:\n", tree.inorder())
