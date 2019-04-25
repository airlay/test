class Stack:
    def __init__(self):
        self.stack = []

    def add(self, value):
        # fist in last out.  not allowing same value... precondition.  return true or false
        if value not in self.stack:
            self.stack.append(value)
            return True
        else:
            return False

    def remove(self):
        if self.stack is not None:
            self.stack.pop(len(self.stack)-1)
            return True
        else:
            return False

    def peek(self):
        print(self.stack[0])


class Queue:
    def __init__(self):
        self.queue = []

    def add(self, value):
        if value not in self.queue:
            self.queue.append(value)
            return True
        else:
            return False

    def remove(self):
        if self.queue is not None:
            self.queue.pop(0)
            return True
        else:
            return False

    def peek(self):
        if len(self.queue) > 0:
            print(self.queue[0])

    def __sizeof__(self):
        return len(self.queue)


a = Queue()
print(a.add('a'))
print(a.add('b'))
print(a.add('c'))
print(a.add('a'))

a.remove()

a.peek()

print('size of a : {}'.format(a.__sizeof__()))

