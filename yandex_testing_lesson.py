def reverse(s):
    if type(s) != str:
        raise TypeError('Expected str, got {}'.format(type(s)))

    return s[::-1]


def count_chars(s):
    if type(s) != str:
        raise TypeError('Expected str, got {}'.format(type(s)))

    dct = {}
    for char in s:
        if char in dct:
            dct[char] += 1
        else:
            dct[char] = 1

    return dct


def is_under_queen_attack(position, queen_position):
    dct = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    for line in [position, queen_position]:
        if type(line) != str:
            raise TypeError()
        elif line[0] not in ["a", "b", "c", "d", "e", "f", "g", "h"] or (line[1].isnumeric() and not (0 < int(line[1]) < 9)):
            raise ValueError()

    row, col = int(queen_position[1]), dct[queen_position[0]]
    row1, col1 = int(position[1]), dct[position[0]]
    if 0 < row1 <= 8 and 0 < col1 <= 8:
        if row == row1 and col == col1:
            return True

        if (row != row1 and col != col1) and ((row - row1) != (col - col1)):
            return False

        return True


class Rectangle:
    def __init__(self, w, h):
        if type(w) not in [int, float] or type(h) not in [int, float]:
            raise TypeError()
        elif w < 0 or h < 0:
            raise ValueError()

        self.w, self.h = w, h

    def get_area(self):
        return self.w * self.h

    def get_perimeter(self):
        return 2 * (self.w + self.h)
