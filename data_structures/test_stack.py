from data_structures.stack import Stack
from data_structures.exceptions import StackOverflowError, StackUnderflowError
import pytest


def test_stack_push_pop():
    el = 1
    stack = Stack(5)
    stack.push(el)

    assert stack.size() == 1
    assert stack.pop() == el
    assert stack.size() == 0


def test_stack_push_overflows():
    stack = Stack(5)
    stack.push(1)
    stack.push(1)
    stack.push(1)
    stack.push(1)
    stack.push(1)
    with pytest.raises(StackOverflowError):
        assert stack.push(1)


def test_stack_pop_underflows():
    stack = Stack(5)
    with pytest.raises(StackUnderflowError):
        assert stack.pop()


def test_stack_is_empty():
    stack = Stack(5)

    assert stack.is_empty() is True
    stack.push(1)
    assert stack.is_empty() is False

