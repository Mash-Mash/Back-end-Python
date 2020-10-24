from itertools import zip_longest


class ListClass(list):
    def __add__(self, other):
        if isinstance(other, list):
            return ListClass([x + y for x, y in zip_longest(self, other, fillvalue=0)])
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, list):
            return ListClass([x - y for x, y in zip_longest(self, other, fillvalue=0)])
        else:
            raise TypeError

    def __lt__(self, other):
        if isinstance(other, list):
            return sum(self) < sum(other)
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, list):
            return sum(self) == sum(other)
        else:
            raise TypeError

    def __ne__(self, other):
        if isinstance(other, list):
            return not self == other
        else:
            raise TypeError

    def __le__(self, other):
        if isinstance(other, list):
            return self < other or self == other
        else:
            raise TypeError

    def __gt__(self, other):
        if isinstance(other, list):
            return not self <= other
        else:
            raise TypeError

    def __ge__(self, other):
        if isinstance(other, list):
            return not self < other
        else:
            raise TypeError
