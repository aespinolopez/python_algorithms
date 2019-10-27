from abc import ABC, abstractmethod
from data_structures.linked_list.node import Node


class LinkedList(ABC):
    def __init__(self):
        self._head = None

    @abstractmethod
    def insert(self, element):
        pass

    @abstractmethod
    def search(self, element):
        pass

    @abstractmethod
    def delete(self, element):
        pass

    def is_empty(self):
        return self._head is None

    def size(self):
        count = 0
        for _ in self:
            count += 1

        return count

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.value
            current = current.next


class SinglyLinkedList(LinkedList):
    def insert(self, element):
        new_item = Node(element, next_node=self._head)
        self._head = new_item

    def search(self, element):
        current = self._head
        while current and current.value != element:
            current = current.next

        return current

    def delete(self, element):
        current = self._head
        prev = None
        while current and current.value != element:
            prev = current
            current = current.next

        if current:
            prev.next = current.next
            del current


if __name__ == '__main__':
    linked = SinglyLinkedList()
    linked.insert(5)
    linked.insert(12)
    linked.insert(54)
    linked.insert(10)
    print("first traversal".center(50, "-"))
    for i in linked:
        print(i)
    linked.delete(12)
    print("second traversal".center(50, "-"))
    for i in linked:
        print(i)

    print("size:", linked.size())
    print("search:", linked.search(54))
    print("search:", linked.search(-87))
