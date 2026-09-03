class Stack:
    def __init__(self):
        self.items=[]
    def size(self):
        print(len(self.items))
    def isEmpty(self):
        print(len(self.items) == 0)

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.isEmpty():
            self.items.pop()
        else:
            raise IndexError("Stack already empty")

    def peek(self):
        print(self.items[-1])

    def display(self):
        for i in range(len(self.items)-1, -1, -1):
            print(self.items[i])


if __name__ == '__main__':
    s1 = Stack()

    stack_items = [45, 56, 87, 99, 21]

    for item in stack_items:
        s1.push(item)
    s1.display()