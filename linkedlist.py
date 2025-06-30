class LinkedlistNode:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode



node1= LinkedlistNode(1)
node2= LinkedlistNode("2")
node3= LinkedlistNode("3")
node4= LinkedlistNode("4")
node5= LinkedlistNode("5")
node6= LinkedlistNode("6")
node7= LinkedlistNode("7")
node8= LinkedlistNode("8")
node9= LinkedlistNode("9")
node10= LinkedlistNode("10")



node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5
node5.nextNode = node6
node6.nextNode = node7
node7.nextNode = node8
node8.nextNode = node9
node9.nextNode = node10


current_node=node1
while True:
    print(current_node.value, ">>>", end=' ')

    if current_node.nextNode is None:
        print('None')
        break
    current_node= current_node.nextNode













