from typing import List


def insertion_sort(intlist: List[int]):
    for j in range(1, len(intlist)):
        key = intlist[j]
        i = j - 1
        while i >= 0 and intlist[i] > key:
            intlist[i + 1] = intlist[i]
            i = i - 1
        intlist[i + 1] = key
