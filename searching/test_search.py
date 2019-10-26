from searching import search


def test_binary_search_found():
    sorted_input = [i for i in range(1, 101)]
    expected_index = 33
    needle = sorted_input[expected_index]
    index = search.binary_search(sorted_input, needle)

    assert index == expected_index
    assert needle == sorted_input[index]


def test_binary_search_not_found():
    needle = -54
    sorted_input = [i for i in range(1, 101)]
    index = search.binary_search(sorted_input, needle)

    assert index is None
