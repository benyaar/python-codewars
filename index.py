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




if __name__ == "__main__":
    import pytest
    pytest.main([__file__])