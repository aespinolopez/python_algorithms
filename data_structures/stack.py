from data_structures.exceptions import StackOverflowError, StackUnderflowError


class Stack:
    def __init__(self, capacity):
        self._capacity = capacity
        self._stack = [None] * capacity
        self._top = 0

    def push(self, element):
        if self._top == self._capacity:
            raise StackOverflowError

        self._stack[self._top] = element
        self._top += 1

    def pop(self):
        if self.is_empty():
            raise StackUnderflowError
        self._top -= 1
        el = self._stack[self._top]
        self._stack[self._top] = None
        return el

    def size(self):
        return self._top

    def is_empty(self):
        return self.size() == 0
