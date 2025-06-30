class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def insertAttheBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printLinkedlist(self):
        temp = self.head
        while temp:
            print(temp.data, end =' ')

            temp = temp.next
        print()

    def insertAttheEnd(self, new_data):
            new_node = Node(new_data)
            if self.head is None:
               self.head = new_node
               return None

            temp = self.head

            while temp.next:
                temp = temp.next
            temp.next = new_node


if __name__ == '__main__':
    llist = LinkedList()

    llist.insertAttheBeginning("Fox")
    llist.insertAttheBeginning("Brown")
    llist.insertAttheBeginning("Quick")
    llist.insertAttheBeginning("The")

    llist.printLinkedlist()

    llist.insertAttheEnd("jumps")
    llist.insertAttheEnd("over")
    llist.printLinkedlist()
