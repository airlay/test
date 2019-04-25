class Node:
    def __init__(self, lkval):
        self.value = lkval
        self.nextNode = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def printvalue(self):
        currentnode = self.headval

        while currentnode is not None:
            print(currentnode.value)
            currentnode = currentnode.nextNode

    def insertatbeginning(self, newNode):
        # create a new node

        newNode.nextNode = self.headval
        self.headval = newNode

    def insertatend(self, newNode):
        # look for the end
        currentNode = self.headval
        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode

        if currentNode.nextNode is None:
            currentNode.nextNode = newNode

    def insertinbetween(self, middleNode, newNode):

        if middleNode is not None:
            if middleNode.nextNode is not None:
                newNode.nextNode = middleNode.nextNode
            middleNode.nextNode = newNode
        else:
            print('middle node is empty')

    def removenode(self, delvalue):
        # removing head node with next Node not empty
        if delvalue == self.headval.value:
            self.headval = self.headval.nextNode

        else:
            # find the correspond node

            curnode = self.headval


            while curnode is not None and curnode.value != delvalue:
                if curnode.value is not None:
                    prevnode = curnode
                    curnode = curnode.nextNode

                else:
                    print('can\'t find the value : (')

            # so this mean we find the id
            if curnode is not None and curnode.value == delvalue:
                prevnode.nextNode = curnode.nextNode
            else:
                print("can't find the node with this value : {}".format(delvalue))


mylinkedlist = SLinkedList()
mylinkedlist.headval = Node("Mom")
e2 = Node("Dad")
e3 = Node("Son")

mylinkedlist.headval.nextNode = e2
e2.nextNode = e3

mylinkedlist.printvalue()

e4 = Node("God")
# print("e4 value : {}".format(e4.value))
mylinkedlist.insertatbeginning(e4)

print("=====================")

mylinkedlist.printvalue()

e5 = Node("Edrick")

mylinkedlist.insertatend(e5)

print('=======================')
mylinkedlist.printvalue()

e5 = Node("bla!")

mylinkedlist.insertinbetween(mylinkedlist.headval.nextNode.nextNode, e5)

print('+++++++++++++++++++++')
mylinkedlist.printvalue()

mylinkedlist.removenode("bla!")
print('+++++++++++++++++++++')

mylinkedlist.removenode("son")
mylinkedlist.removenode("Son")
print('+++++++++++++++++++++')
mylinkedlist.removenode("God")

es = Node("Skyer")
print('***************')
mylinkedlist.insertinbetween(mylinkedlist.headval.nextNode, es)
mylinkedlist.printvalue()
