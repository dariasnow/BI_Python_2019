
def group_equal(els):
    final_list = []
    for (i, x) in enumerate(els):
        if i < 1 or x != els[i - 1]:
            final_list.append([x])
        else:
            final_list[-1].append(x)
    return final_list


if __name__ == '__main__':
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1, 1], [4, 4, 4], ["hello", "hello"], [4]]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []
