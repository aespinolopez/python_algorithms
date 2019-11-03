from typing import List
import random


def insertion_sort(intlist: List[int]):
    """
    Average time complexity: O(n²)
    """
    for j in range(1, len(intlist)):
        key = intlist[j]
        i = j - 1
        while i >= 0 and intlist[i] > key:
            intlist[i + 1] = intlist[i]
            i = i - 1
        intlist[i + 1] = key


def selection_sort(intlist: List[int]):
    """
    Average time complexity: O(n²)
    """
    new_arr = []
    for i in range(len(intlist)):
        smallest_index = find_smallest(intlist)
        new_arr.append(intlist.pop(smallest_index))

    return new_arr


def quick_sort(intlist: List[int]):
    """
    Average time complexity: O(n log n)
    Worst case time complexity: O(n²)
    """
    if len(intlist) < 2:
        return intlist

    # pivot = intlist[0] it's better if you choose a random pivot because you will be able to avoid it's worst case
    rand_index = random.randrange(0, len(intlist))
    swap(intlist, 0, rand_index)
    pivot = intlist[0]
    lesser = [item for item in intlist[1:] if item <= pivot]
    greater = [item for item in intlist[1:] if item > pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


# todo: fix index error
def quick_sort_in_place(intlist: List[int], p, r):
    if p < r:
        q = partition(intlist, p, r)
        quick_sort_in_place(intlist, p, q - 1)
        quick_sort_in_place(intlist, q + 1, r)


def find_smallest(subarray):
    smallest = subarray[0]
    smallest_index = 0
    for i in range(1, len(subarray)):
        if subarray[i] < smallest:
            smallest = subarray[i]
            smallest_index = i

    return smallest_index


def swap(intlist, index1, index2):
    temp = intlist[index2]
    intlist[index2] = intlist[index1]
    intlist[index1] = temp


def partition(arr, p, r):
    # randomize pivot to avoid worst case
    rand_index = random.randrange(p, len(arr))
    swap(arr, rand_index, r)
    # partition
    i = p - 1
    key = arr[r]
    for j in range(p, r - 1):
        if arr[j] < key:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, r)
    return i + 1

