class Node:
    def __init__(self, val=None, prev=None, nxt=None):
        self.val=val
        self.prev=prev
        self.nxt=nxt
class DLL:
    def __init__(self, head=None, tail=None):
        self.head=head
        self.tail=tail

    def insert_last(self, head, data):
        if not head:
            head = Node(data)
            self.tail = head
        else:
            self.tail.nxt = Node(data)
            self.tail.nxt.prev = self.tail
            self.tail = self.tail.nxt
        self.head=head
        return head

    def insert_front(self, head, data):
        if not head:
            head = Node(data)
            self.tail = head
        else:
            ptr = Node(data)
            ptr.nxt = head
            head.prev = ptr
            head = ptr
        self.head=head
        return head

    def traverse(self, head):
        ptr=head
        while ptr:
            print(ptr.val, end=" ")
            ptr=ptr.nxt


def main():
    head=None
    dll = DLL()
    vals=[10,50,40,80,60]
    for val in vals:
        head = dll.insert_front(head, val)

    dll.traverse(head)
    print("\n",dll.head.val)

main()

