class TreeNode:
    def __init__(self, value):
        self.left= None
        self.right= None
        self.value= value


    def insert(self, key_value):
        if key_value < self.value:
                if self.left is None:
                    self.left = TreeNode(key_value)
                else:
                    self.left.insert(key_value)
        else:
                if self.right is None:
                  self.right= TreeNode(key_value)
                else:
                   self.right.insert(key_value)

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.value)

        if self.right:
            self.right.in_order_traversal()


    def pre_order_traversal(self):
        print(self.value)
        if self.left:
            self.left.pre_order_traversal()

        if self.right:
            self.right.pre_order_traversal()


    def post_order_traversal(self):
        if self.left:
            self.left.pre_order_traversal()

        if self.right:
            self.right.pre_order_traversal()
        print(self.value)


    def find(self, key):
        if key < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find()

        elif key > self.value:
            if self.right is None:
                return False
            return self.right.find()
        else:
            return True

    def method(self):
        return True

if __name__=='__main__':
    trav= TreeNode(10)
    trav.insert(6)
    trav.insert(19)
    trav.insert(7)
    trav.insert(34)
    trav.insert(51)
    trav.insert(15)
    trav.insert(17)
    trav.insert(99)
    trav.insert(27)
    trav.insert(13)
    trav.insert(11)

    trav.in_order_traversal()
    print("\n")
    trav.post_order_traversal()
    print("\n")
    trav.pre_order_traversal()
    print("\n")




