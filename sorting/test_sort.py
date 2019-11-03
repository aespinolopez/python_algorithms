import sorting.sort as sort

to_sort = [7, 85, 47, 21, 65, 2]
expected_output = [2, 7, 21, 47, 65, 85]


def test_insertion_sort():
    sort.insertion_sort(to_sort)

    for i in range(len(expected_output)):
        assert to_sort[i] == expected_output[i]


def test_find_smallest():
    arr = [2, 8, 9, 1, 12]
    smallest_index = sort.find_smallest(arr)
    assert smallest_index == 3


def test_selection_sort():
    sorted_list = sort.selection_sort(to_sort)

    for i in range(len(expected_output)):
        assert sorted_list[i] == expected_output[i]


def test_quick_sort():
    sorted_list = sort.quick_sort(to_sort)
    for i in range(len(expected_output)):
        assert sorted_list[i] == expected_output[i]


def test_quick_sort_in_place():
    sorted_list = sort.quick_sort_in_place(to_sort, 0, len(to_sort))
    for i in range(len(expected_output)):
        assert sorted_list[i] == expected_output[i]
