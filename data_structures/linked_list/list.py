from abc import ABC, abstractmethod

# todo: implement circular list and circular doubly linked list with sentinel


class LinkedList(ABC):
    class Node:
        def __init__(self, value, next_node=None, prev_node=None):
            self.value = value
            self.next = next_node
            self.prev = prev_node

    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    @abstractmethod
    def insert(self, element):
        pass

    @abstractmethod
    def delete(self, element=None):
        pass

    @abstractmethod
    def clear(self):
        pass

    def search(self, element):
        current = self._head
        while current and current.value != element:
            current = current.next

        return current

    def is_empty(self):
        return self._size > 0

    def size(self):
        return self._size

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.value
            current = current.next


class SinglyLinkedList(LinkedList):
    def insert(self, element):
        new_item = self.Node(element)
        if not self._head and not self._tail:
            self._head = self._tail = new_item
        else:
            self._tail.next = new_item
            self._tail = new_item
        self._size += 1

    def delete(self, element=None):
        if not element and self._head:
            self._head = self._head.next
            self._size -= 1
            if not self._head.next:
                self._tail = self._head
        else:
            current = self._head
            prev = None
            while current and current.value != element:
                prev = current
                current = current.next

            if current:
                prev.next = current.next
                del current
                self._size -= 1
                if not prev.next:
                    self._tail = prev

    def clear(self):
        it = self._head
        while it:
            next_node = it.next
            del it.next
            del it.value
            it = next_node
        self._head = self._tail = None
        self._size = 0


class DoublyLinkedList(LinkedList):
    def insert(self, element):
        self._size += 1
        new_item = self.Node(element)
        if not self._head and not self._tail:
            self._head = self._tail = new_item
        else:
            new_item.prev = self._tail
            self._tail.next = new_item
            self._tail = new_item

    def delete(self, element=None):
        if not element and self._head:
            self._head = self._head.next
            self._head.prev = None
            self._size -= 1
            if not self._head.next:
                self._tail = self._head
        else:
            it = self._head
            while it and it.value != element:
                it = it.next

            if it:
                print("element:", element, "value:", it.value)
                print("next:", it.next.value, "prev:", it.prev.value)
                if it.prev:
                    it.prev.next = it.next
                else:
                    self._head = it.next
                if it.next:
                    it.next.prev = it.prev
                else:
                    self._tail = it.prev

    def clear(self):
        it = self._head
        while it:
            next_node = it.next
            it.next = None
            it.prev = None
            it.value = None
            it = next_node
        self._head = self._tail = None
        self._size = 0
