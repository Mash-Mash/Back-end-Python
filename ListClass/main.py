from ListClass import ListClass

if __name__ == '__main__':
    a = ListClass([10])
    b = ListClass([1, 2, 3, 4])
    c = [1, 2, 3]
    print(a == b)
    print(list(a + c))
