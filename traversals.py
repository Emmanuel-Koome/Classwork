class TreeNode:
    def __init__(self, value):
        self.left= None
        self.right= None
        self.value= value


    def insert(self, value):
        if value < self.value:
            self.left = TreeNode(value)
        else:
             self.right= TreeNode(value)

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


if __name__=='__main__':
    trav= TreeNode('Á')




