from logging import exception

class StackNode:
    def _init_(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def _init_(self):
        self.top = None
    def is_empty(self):
        return self.top is None
    def push(self,value):
        new_node = StackNode(value)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.is_empty():
            raise exception("cannot peek on empty stack!")
        pooped_value = self.top.value

        self.top = self.top.next

        return pooped_value

    def peek(self):
        if self.is_empty():
            raise exception("cannot peek on empty stack!")
        return self.top.value
    def display(self):
        current = self.top
        value = []
        while current:
            value.append(str(current.value))
            current = current.next
        print("Stack from top to bottom: " ," ->".join(value))
if __name__ == "__main__":
    stack_11 = LinkedListStack()
    stack_11.push(5)
    stack_11.push(10)
    stack_11.push(15)

    stack_11.display()

    print("peek top: ", stack_11.peek())

    print("pop: ", stack_11.pop())
    stack_11.display()