import random


class MyBinary:

    # initialized the object
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        # if value is <= root data insert left
        if value <= self.data:
            if self.left is None:
                self.left = MyBinary(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = MyBinary(value)
            else:
                self.right.insert(value)

    def hasvalue(self, lkval):
        # base case
        if self.data == lkval:
            return True
        elif lkval <= self.data:
            if self.left is None:
                return False
            else:
                return self.left.hasvalue(lkval)
        elif lkval > self.data:
            if self.right is None:
                return False
            else:
                return self.right.hasvalue(lkval)
        else:
            return False

    def travesnodes(self):
        if self.left is not None:
            self.left.travesnodes()
        print(self.data)
        if self.right is not None:
            self.right.travesnodes()

    def depth(self):
        # base case
        curdepth = 0
        leftdepth = 0
        rightdepth = 0

        if self.left is None and self.right is None:
            return 0
        elif self.left is not None:
            # curdepth += 1
            leftdepth = 1 + self.left.depth()
        elif self.right is not None:
            rightdepth = 1 + self.right.depth()

        return max(leftdepth, rightdepth)


if __name__ == '__main__':
    root = MyBinary(random.randint(1, 100))
    # root.insert(2)
    # root.insert(23)
    for i in reversed(range(1, 15)):
        root.insert(random.randint(1, 100))
        # root.insert(i)
    # print(root.data)
    # print(root.left.data)
    # print(root.right.data)
    #
    # h1 = root.hasvalue(15)
    # h2 = root.hasvalue(2)
    # h3 = root.hasvalue(23)
    #
    # hr = root.hasvalue(234)
    #
    # print('h1 : {}'.format(h1))
    # print('h2 : {}'.format(h2))
    # print('h3 : {}'.format(h3))
    # print('hr : {}'.format(hr))
    #
    # print('+++++++++++++++++++++')
    # root.travesnodes()

    mydepth = root.depth()

    print('root depth is {}'.format(mydepth))
