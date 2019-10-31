import itertools


def group_equal(els):
    final_list = [list(groups) for elements, groups in itertools.groupby(els)]
    return final_list


if __name__ == '__main__':
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1, 1], [4, 4, 4], ["hello", "hello"], [4]]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []
