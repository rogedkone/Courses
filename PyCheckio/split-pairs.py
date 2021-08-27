def split_pairs(a):
    result = []
    st = ""
    count = 0
    if len(a) % 2 == 0:
        for i in range(0, len(a), 2):
            st = ""
            st += a[i] + a[i + 1]
            result.append(st)
        return result
    elif len(a) % 2 == 1:
        for i in range(len(a)):
            if count == 2:
                result.append(st)
                st = ""
                count = 0
            st += a[i]
            count += 1
        if count == 1:
            st += "_"
            result.append(st)
        return result
        


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
