def scramble(string, positions):
    """
    Example:
        scramble('abcd', [0, 3, 1, 2]) => 'acdb'
    """
    result = [''] * len(string)
    for i, pos in enumerate(positions):
        result[pos] = string[i]
    return ''.join(result)

def test_scramble_basic():
    assert scramble('abcd', [0,3,1,2]) == 'acdb'
    assert scramble('sc301s', [4,0,3,1,5,2]) == 'c0s3s1'
    assert scramble('bskl5', [2,1,4,3,0]) == '5sblk'

def count_by(x, n):
    """
    Returns a list of the first n multiples of x.
    Example: count_by(2, 5) → [2, 4, 6, 8, 10]
    """
    return [x * i for i in range(1, n + 1)]

def test_fixed_cases():
    assert count_by(1, 5) == [1, 2, 3, 4, 5]
    assert count_by(2, 5) == [2, 4, 6, 8, 10]
    assert count_by(3, 5) == [3, 6, 9, 12, 15]
    assert count_by(50, 5) == [50, 100, 150, 200, 250]
    assert count_by(100, 5) == [100, 200, 300, 400, 500]

def better_than_average(class_points, your_points):
    """
    Returns True if your_points is greater than average of class_points.
    """
    avg = sum(class_points) / len(class_points)
    return your_points > avg

import pytest

@pytest.mark.parametrize("arr, points, expected", [
    ([2, 3], 5, True),
    ([100, 40, 34, 57, 29, 72, 57, 88], 75, True),
    ([12, 23, 34, 45, 56, 67, 78, 89, 90], 69, True),
    ([41, 75, 72, 56, 80, 82, 81, 33], 50, False),
    ([29, 55, 74, 60, 11, 90, 67, 28], 21, False),
    ([100, 90, 80], 85, False),
    ([50, 50, 50], 50, False),
])
def test_better_than_average(arr, points, expected):
    assert better_than_average(arr, points) == expected


def reverse_words(s):
    """
    Reverses the order of words in a string.
    Example: "Hello world" → "world Hello"
    """
    return ' '.join(s.split()[::-1])

def test_reverse_words():
    assert reverse_words("Hello world") == "world Hello"
    assert reverse_words("Python is great") == "great is Python"
    assert reverse_words("a b c") == "c b a"
    assert reverse_words("one") == "one"
    assert reverse_words("") == ""

def is_isogram(string):
    """
    Перевіряє, чи є слово ізограмою (без повторюваних літер, ігноруючи регістр).
    Example: "Dermatoglyphics" → True
             "aba" → False
    """
    cleaned = string.lower()
    return len(set(cleaned)) == len(cleaned)

def test_is_isogram():
    assert is_isogram("Dermatoglyphics") is True
    assert is_isogram("isogram") is True
    assert is_isogram("aba") is False
    assert is_isogram("moOse") is False  # 'o' повторюється
    assert is_isogram("") is True
    
if __name__ == "__main__":
    pytest.main([__file__])
