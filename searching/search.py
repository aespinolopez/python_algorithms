def binary_search(sorted_input, needle):
    low = 0
    high = len(sorted_input) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = sorted_input[mid]
        if guess == needle:
            return mid
        if guess > needle:
            high = mid - 1
        else:
            low = mid + 1

    return None
