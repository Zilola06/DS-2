class QueueFromStacks:
    def __init__(self):
        self._in = []
        self._out = []

    def enqueue(self, x):
        self._in.append(x)

    def dequeue(self):
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())

        if not self._out:
            raise IndexError("dequeue from empty queue")

        return self._out.pop()


# Tests
q = QueueFromStacks()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

assert q.dequeue() == 1

q.enqueue(4)

assert q.dequeue() == 2
assert q.dequeue() == 3
assert q.dequeue() == 4

try:
    q.dequeue()
    assert False
except IndexError:
    pass
print("Challenge 4: passed successfully")
