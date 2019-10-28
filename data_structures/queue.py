from data_structures.exceptions import QueueOverflowError, QueueUnderflowError


class Queue:
    def __init__(self, capacity):
        self._capacity = capacity
        self._queue = [None] * capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, element):
        # todo: the following condition head == tail + 1 is never true. check how to know if the queue is full
        if self._head == self._tail + 1 or (self._head == 0 and self._tail == self._capacity):
            raise QueueOverflowError
        self._queue[self._tail] = element
        self._tail += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflowError
        el = self._queue[self._head]
        self._head += 1
        return el

    def is_empty(self):
        return self._head == self._tail

    def size(self):
        return (self._capacity - self._head + self._tail) % self._capacity
