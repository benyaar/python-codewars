import math
from collections import Counter

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
def likes(names):
    """
    Returns a string describing who likes something, based on the input list of names.
    """
    if not names:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"    

def test_likes():
    assert likes([]) == "no one likes this"
    assert likes(["Peter"]) == "Peter likes this"
    assert likes(["Jacob", "Alex"]) == "Jacob and Alex like this"
    assert likes(["Max", "John", "Mark"]) == "Max, John and Mark like this"
    assert likes(["Alex", "Jacob", "Mark", "Max"]) == "Alex, Jacob and 2 others like this"
    assert likes(["A", "B", "C", "D", "E"]) == "A, B and 3 others like this"
def can_form_palindrome(s):
    """
    Перевіряє, чи можна перестановкою символів у рядку утворити паліндром.
    Example: "civic" → True (вже паліндром)
             "ivicc" → True ("civic")
             "hello" → False
             "aabbcc" → True ("abccba")
    """
    from collections import Counter
    freq = Counter(s)
    odd_counts = sum(1 for count in freq.values() if count % 2 != 0)
    return odd_counts <= 1

def test_can_form_palindrome():
    assert can_form_palindrome("civic") is True
    assert can_form_palindrome("ivicc") is True
    assert can_form_palindrome("hello") is False
    assert can_form_palindrome("aabbcc") is True
    assert can_form_palindrome("aabbc") is True  # "abcba"
    assert can_form_palindrome("aabbcd") is False
    assert can_form_palindrome("") is True   
def find_odd(arr):
    """
    Returns the integer that appears an odd number of times in the list.
    """
    result = 0
    for num in arr:
        result ^= num  # XOR will cancel out even occurrences
    return result

def test_find_odd():
    assert find_odd([20, 1, 1, 2, 2, 3, 3]) == 20
    assert find_odd([10, 10, 10]) == 10
    assert find_odd([1, 1, 2]) == 2
    assert find_odd([7]) == 7
    assert find_odd([0, 0, 1, 1, 0]) == 0


def count_characters(s):
    """
    Counts how many times each character appears in the string s.
    """
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def test_count_characters():
    assert count_characters("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert count_characters("mississippi") == {'m':1, 'i':4, 's':4, 'p':2}
    assert count_characters("") == {}
    assert count_characters("aabbcc") == {'a':2, 'b':2, 'c':2}


def remove_duplicates(lst):
    """
    Returns a list with duplicates removed, keeping the first occurrences only.
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 1, 3, 2, 4]) == [1, 2, 3, 4]
    assert remove_duplicates(['a', 'b', 'a', 'c', 'b']) == ['a', 'b', 'c']
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 1, 1, 1]) == [1]
    assert remove_duplicates([True, False, True, False]) == [True, False]

def longest_unique_substring(s):
    """
    Returns the length of the longest substring without repeating characters.
    Uses sliding window technique.
    """
    seen = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


def test_longest_unique_substring():
    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("bbbbb") == 1
    assert longest_unique_substring("pwwkew") == 3
    assert longest_unique_substring("") == 0
    assert longest_unique_substring("abcdefg") == 7
    assert longest_unique_substring("abba") == 2

def flatten(arr):
    """
    Recursively flattens a nested list into a flat list.
    """
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def test_flatten():
    assert flatten([1, [2, 3, [4, 5]], 6]) == [1, 2, 3, 4, 5, 6]
    assert flatten([[1, 2], [3, [4, [5]]]]) == [1, 2, 3, 4, 5]
    assert flatten([[[[]]]]) == []
    assert flatten([1, [], [2, [3]], 4]) == [1, 2, 3, 4]
    assert flatten([]) == []

def count_chars(s):
    """
    Counts the frequency of each character in the string.
    """
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq


def test_count_chars():
    assert count_chars("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert count_chars("aabcc") == {'a': 2, 'b': 1, 'c': 2}
    assert count_chars("") == {}
    assert count_chars("aaa") == {'a': 3}
    assert count_chars("abcabc") == {'a': 2, 'b': 2, 'c': 2}
    
def filter_squares(arr):
    """
    Returns a list of numbers that are perfect squares.
    """
    return [x for x in arr if math.isqrt(x) ** 2 == x]


def test_filter_squares():
    assert filter_squares([1, 2, 3, 4, 5, 9, 16, 18, 20]) == [1, 4, 9, 16]
    assert filter_squares([10, 15, 20]) == []
    assert filter_squares([0, 1, 25, 26]) == [0, 1, 25]
    assert filter_squares([]) == []
    assert filter_squares([100, 121, 144]) == [100, 121, 144]

def most_common_char(s):
    """
    Returns the most frequent character in the string.
    If multiple, returns the first by appearance.
    """
    if not s:
        return ""
    counts = Counter(s)
    max_count = max(counts.values())
    for ch in s:
        if counts[ch] == max_count:
            return ch

def test_most_common_char():
    assert most_common_char("hello world") == "l"
    assert most_common_char("aabbbcc") == "b"
    assert most_common_char("abc") == "a"
    assert most_common_char("aaab") == "a"
    assert most_common_char("") == ""


def char_frequency(s):
    """
    Returns a dictionary with the frequency of each character in the string.
    """
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

def test_char_frequency():
    assert char_frequency("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert char_frequency("abca") == {'a': 2, 'b': 1, 'c': 1}
    assert char_frequency("") == {}
    assert char_frequency("aAa") == {'a': 2, 'A': 1}

def group_elements(lst):
    seen = {}
    for item in lst:
        if item not in seen:
            seen[item] = []
        seen[item].append(item)
    return list(seen.values())

def test_group_elements():
    assert group_elements([1, 2, 1, 3, 2, 1]) == [[1, 1, 1], [2, 2], [3]]
    assert group_elements(['a', 'b', 'a', 'c', 'b']) == [['a', 'a'], ['b', 'b'], ['c']]
    assert group_elements([]) == []
    assert group_elements([1, 1, 1]) == [[1, 1, 1]]

def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels)

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("world") == 1
    assert count_vowels("Python") == 1
    assert count_vowels("AEIOU") == 5

def valid_parentheses(s):
    """
    Returns True if the string s has valid matching parentheses of types (), {}, [].
    Ignores non-bracket characters.
    """
    pairs = {')': '(', '}': '{', ']': '['}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack

@pytest.mark.parametrize("s, expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([{}])", True),
    ("([)]", False),
    ("", True),
    ("a+(b*c)-{d/2}", True),
    ("(((", False),
    ("))", False),
    ("{[()()]}", True),
    ("{[(])}", False),
    ("[", False),
    ("]", False),
])


def test_valid_parentheses(s, expected):
    assert valid_parentheses(s) == expected



def find_single_number(nums):
    """
    Rotates a number that appears more than once in the nums list.
    Every day, the number increases evenly by two.
    """
    result = 0
    for num in nums:
        result ^= num  
    return result


@pytest.mark.parametrize("nums, expected", [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([7, 3, 5, 3, 5, 7, 9], 9),
    ([10], 10),
    ([0, 1, 0], 1),
])
def test_find_single_number(nums, expected):
    assert find_single_number(nums) == expected

def second_largest(nums):
    """
    Returns the second largest unique number from the list.
    If there are fewer than two unique numbers, returns None.
    """
    unique_nums = list(set(nums))  # remove duplicates
    if len(unique_nums) < 2:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[1]

def test_second_largest():
    assert second_largest([10, 20, 4, 45, 99]) == 45
    assert second_largest([5, 5, 5]) is None
    assert second_largest([1, 2]) == 1

def flatten(arr):
    """
    Flattens a nested list into a single list.

    Args:
        arr (list): List that can contain nested lists.

    Returns:
        list: Flattened list with all elements from nested lists.
    """
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def test_flatten():
    assert flatten([1, [2, 3, [4, 5]], 6]) == [1, 2, 3, 4, 5, 6]
    assert flatten([]) == []
    assert flatten([1, [2], 3]) == [1, 2, 3]

def factorial(n):
    """
    Returns the factorial of a number n (n!).
    Factorial is the product of all positive integers <= n.
    Uses recursion.

    Args:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def factorial_iterative(n):
    """
    Returns the factorial of a number n (n!).
    Uses an iterative approach.

    Args:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial_iterative(0) == 1
    assert factorial_iterative(6) == 720


def roman_encoder(n: int) -> str:
    """
    Converts an integer to a Roman numeral.
    Supports numbers from 1 up to 3999.
    """
    dictionary = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
        1: 'I'
    }

    result = ""
    for key in sorted(dictionary.keys(), reverse=True):
        while n >= key:
            result += dictionary[key]
            n -= key
    return result


def test_roman_encoder():
    assert roman_encoder(1) == "I"
    assert roman_encoder(2) == "II"
    assert roman_encoder(3) == "III"
    assert roman_encoder(4) == "IV"
    assert roman_encoder(5) == "V"
    assert roman_encoder(9) == "IX"
    assert roman_encoder(10) == "X"
    assert roman_encoder(11) == "XI"
    assert roman_encoder(19) == "XIX"
    assert roman_encoder(22) == "XXII"
    assert roman_encoder(15) == "XV"
    assert roman_encoder(1000) == "M"
    assert roman_encoder(1001) == "MI"
    assert roman_encoder(1990) == "MCMXC"
    assert roman_encoder(2007) == "MMVII"
    assert roman_encoder(2008) == "MMVIII"


def rgb(r: int, g: int, b: int) -> str:
    """
    Converts RGB decimal values (0–255) into a 6-character hexadecimal string.
    Values outside the range are clamped to [0, 255].
    """
    def clamp(x: int) -> int:
        return max(0, min(255, x))

    return "".join(f"{clamp(x):02X}" for x in (r, g, b))


def test_rgb():
    assert rgb(0, 0, 0) == "000000"
    assert rgb(0, 0, -20) == "000000"
    assert rgb(300, 255, 255) == "FFFFFF"
    assert rgb(173, 255, 47) == "ADFF2F"


def tower_builder(n: int) -> list[str]:
    """
    Builds a tower represented as a list of strings.
    Each floor has centered '*' characters with spaces on both sides.
    
    Example:
    tower_builder(3) -> ["  *  ", " *** ", "*****"]
    """
    result = []
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        result.append(spaces + stars + spaces)
    return result


def test_tower_builder():
    assert tower_builder(1) == ["*"]
    assert tower_builder(2) == [" * ", "***"]
    assert tower_builder(3) == ["  *  ", " *** ", "*****"]


def factorial(n: int) -> int:
    """
    Returns the factorial of n.
    Factorial of 0 is defined as 1.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120



def unique_in_order(seq):
    """
    Unique In Order
    """
    result = []
    for i, ch in enumerate(seq):
        if i == 0 or ch != seq[i - 1]:
            result.append(ch)
    return result


def test_unique_in_order():
    assert unique_in_order("AAAABBBCCDAABBB") == ["A", "B", "C", "D", "A", "B"]
    assert unique_in_order("ABBCcAD") == ["A", "B", "C", "c", "A", "D"]
    assert unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3]


def generate_hashtag(s: str) -> str | bool:
    """
    Generates a hashtag from the input string.
    - Returns False if the string is empty or result exceeds 140 chars.
    - Capitalizes the first letter of each word and removes spaces.
    """
    if not s or not s.strip():
        return False

    result = "#" + "".join(word.capitalize() for word in s.strip().split())
    return result if len(result) <= 140 else False


def test_generate_hashtag():
    assert generate_hashtag("") is False
    assert generate_hashtag(" " * 200) is False
    assert generate_hashtag("Do We have A Hashtag") == "#DoWeHaveAHashtag"
    assert generate_hashtag("Codewars") == "#Codewars"
    assert generate_hashtag("Codewars Is Nice") == "#CodewarsIsNice"
    assert generate_hashtag("Codewars is nice") == "#CodewarsIsNice"
    assert generate_hashtag("code" + " " * 140 + "wars") == "#CodeWars"
    assert generate_hashtag(
        "L" + "o" * 138 + "ng Cat"
    ) is False  # too long
    assert generate_hashtag("a" * 139) == "#" + "A" + "a" * 138
    assert generate_hashtag("a" * 140) is False


def spin_words(sentence: str) -> str:
    """
    Reverses words with length >= 5 in the sentence.
    """
    return " ".join(
        word[::-1] if len(word) >= 5 else word
        for word in sentence.split()
    )


def test_spin_words():
    assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
    assert spin_words("This is a test") == "This is a test"
    assert spin_words("This is another test") == "This is rehtona test"
    assert spin_words("Welcome") == "emocleW"
    assert spin_words("Codewars is awesome") == "srawedoC is emosewa"


def digital_root(n: int) -> int:
    """
    Returns the digital root of a number.
    """
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n


def test_digital_root():
    assert digital_root(16) == 7
    assert digital_root(942) == 6
    assert digital_root(132189) == 6
    assert digital_root(493193) == 2
    assert digital_root(9) == 9
    assert digital_root(0) == 0


def diamond(n: int) -> str | None:
    """
    Returns a diamond shape of '*' characters of size n.
    If n is even or <= 0 → returns None.
    """
    if n <= 0 or n % 2 == 0:
        return None

    result = []
    mid = n // 2

    for i in range(n):
        stars = n - abs(mid - i) * 2
        spaces = abs(mid - i)
        result.append(" " * spaces + "*" * stars)

    return "\n".join(result) + "\n"


def test_diamond_valid():
    assert diamond(1) == "*\n"
    assert diamond(3) == " *\n***\n *\n"
    assert diamond(5) == "  *\n ***\n*****\n ***\n  *\n"


def test_diamond_invalid():
    assert diamond(2) is None
    assert diamond(-3) is None
    assert diamond(0) is None


def accum(s: str) -> str:
    """
    Example:
        accum("abcd") => "A-Bb-Ccc-Dddd"
        accum("RqaEzty") => "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    """
    return "-".join(char.upper() + char.lower() * i for i, char in enumerate(s))


def test_accum_basic():
    assert accum("abcd") == "A-Bb-Ccc-Dddd"
    assert accum("RqaEzty") == "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    assert accum("cwAt") == "C-Ww-Aaa-Tttt"


def number_to_words(num):
    """
    Example:
        number_to_words(305) => ["three", "zero", "five"]
    """
    mapping = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
    }
    return [mapping[digit] for digit in str(num)]


def test_number_to_words_basic():
    assert number_to_words(305) == ["three", "zero", "five"]
    assert number_to_words(42) == ["four", "two"]
    assert number_to_words(0) == ["zero"]


def sum_of_multiples(n):
    """
    Example:
        sum_of_multiples(10) => 23
        # бо 3 + 5 + 6 + 9 = 23
    """
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)


def test_sum_of_multiples_basic():
    assert sum_of_multiples(10) == 23
    assert sum_of_multiples(20) == 78
    assert sum_of_multiples(0) == 0
    assert sum_of_multiples(1) == 0
    assert sum_of_multiples(16) == 60


def to_leet_speak(text):
    """
    Example:
        to_leet_speak("Leet") => "1337"
        to_leet_speak("Hello World") => "H3ll0 W0rld"
    """
    mapping = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        's': '5',
        't': '7'
    }
    result = ""
    for char in text:
        lower = char.lower()
        result += mapping.get(lower, char)
    return result


def test_to_leet_speak():
    assert to_leet_speak("Leet") == "1337"
    assert to_leet_speak("Hello World") == "H3ll0 W0rld"
    assert to_leet_speak("Python is strong") == "Py7h0n 15 57r0ng"
    assert to_leet_speak("Sos") == "505"
    assert to_leet_speak("") == ""


if __name__ == "__main__":
    pytest.main([__file__])
