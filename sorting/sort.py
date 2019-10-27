from typing import List


def insertion_sort(intlist: List[int]):
    for j in range(1, len(intlist)):
        key = intlist[j]
        i = j - 1
        while i >= 0 and intlist[i] > key:
            intlist[i + 1] = intlist[i]
            i = i - 1
        intlist[i + 1] = key


def find_smallest(subarray):
    smallest = subarray[0]
    smallest_index = 0
    for i in range(1, len(subarray)):
        if subarray[i] < smallest:
            smallest = subarray[i]
            smallest_index = i

    return smallest_index


def selection_sort(intlist: List[int]):
    new_arr = []
    for i in range(len(intlist)):
        smallest_index = find_smallest(intlist)
        new_arr.append(intlist.pop(smallest_index))

    return new_arr
