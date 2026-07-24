class Node:
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next
class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.ptr=None

    def insert_last(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def insert_front(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.ptr = Node(data)
            self.ptr.next = self.head
            self.head = self.ptr

    def traverse(self):
        self.ptr = self.head
        while self.ptr != None:
            print(self.ptr.val, end=" ")
            self.ptr = self.ptr.next

    def delete_last(self):
        self.ptr = self.head
        while self.ptr.next != self.tail:
            self.ptr = self.ptr.next
        self.tail = self.ptr
        self.tail.next = None

    def delete_front(self):
        self.ptr = self.head
        self.head = self.head.next
        self.ptr.next = None

def main():
    vals = [10,40,30,20]
    list = SLL()
    for val in vals:
        list.insert_front(val)
    print("Before:", end=" ")
    list.traverse()
    #list.delete_last()
    list.delete_front()
    print("\nAfter:", end=" ")
    list.traverse()
    # list.traverse()

main()
