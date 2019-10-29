
def checkio(first, second):
    first, second = first.split(','), second.split(',')
    return ','.join(sorted(set(first) & set(second)))


if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
