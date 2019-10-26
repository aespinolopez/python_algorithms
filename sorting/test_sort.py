import sorting.sort as sort


def test_insertion_sort():
    to_sort = [7, 85, 47, 21, 65, 2]
    expected_output = [2, 7, 21, 47, 65, 85]
    sort.insertion_sort(to_sort)

    print(to_sort)

    for i in range(len(expected_output)):
        assert to_sort[i] == expected_output[i]
