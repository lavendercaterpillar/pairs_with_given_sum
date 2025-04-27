import pytest
from main import pairs_with_given_sum

# Nominal cases

# @pytest.mark.skip("comment this skip out")
def test_two_pairs_unidentical_numbers():
    # example input: 
    numbers = [1, 2, 4, 5]
    target = 6
    # expected output:
    expected = 2   
    
    result = pairs_with_given_sum(numbers, target)

    assert result == expected


# @pytest.mark.skip("comment this skip out")
def test_three_pairs_unidentical_numbers():
    # example input: 
    numbers = [97, 51, 49, 35, 3, 65]
    target = 100
    # expected output:
    expected = 3   
    
    result = pairs_with_given_sum(numbers, target)

    assert result == expected


# @pytest.mark.skip("comment this skip out")
def test_invalid_list_item():
    # example input:
    numbers = [2,3,"4"]
    target = 100
    # expected output:
    expected = 'Invalid input in the list: 4. All numbers must be positive integers.'
    
    result = pairs_with_given_sum(numbers, target)

    assert expected == result

    # another way of using pytest.raise
    # with pytest.raises(ValueError, match="Invalid input"):
    #     pairs_with_given_sum(numbers, target)


# @pytest.mark.skip("comment this skip out")
def test_invalid_list():
    # example input:
    numbers = "[2,3],4"
    target = 5
    # expected output:
    expected = "Oops! Please enter numbers as a list."
    
    result = pairs_with_given_sum(numbers, target)

    assert expected == result


# @pytest.mark.skip("comment this skip out")
def test_invalid_target():
    # example input:
    numbers = [2,3,1]
    target = "5"
    # expected output:

    expected = "Oops! Please enter the target as a non-negative integer."
    
    result = pairs_with_given_sum(numbers, target)

    assert expected == result

# Edge Cases

# @pytest.mark.skip("comment this skip out")
def test_no_pair_sums_target():
    # example input:
    numbers = [1, 2, 3]
    target = 10
    # expected output:
    expected = 0
    
    result = pairs_with_given_sum(numbers, target)

    assert expected == result



# @pytest.mark.skip("comment this skip out")
def test_empty_list():
    # example input:
    numbers = []
    target = 5
    # expected output:
    expected = 0

    result = pairs_with_given_sum(numbers, target)

    assert expected == result


# @pytest.mark.skip("comment this skip out")
def test_one_item_list():
    # example input:
    numbers = [7]
    target = 7
    # expected output:
    expected = 0

    result = pairs_with_given_sum(numbers, target)

    assert expected == result


# @pytest.mark.skip("comment this skip out")
def test_duplicate_pairs():
    # example input:
    numbers = [1,5,1]
    target = 6
    # expected output:
    expected = 2

    result = pairs_with_given_sum(numbers, target)

    assert expected == result


# @pytest.mark.skip("comment this skip out")
def test_multimatch_pairs():
    # example input:
    numbers = [3,3,3,3]
    target = 6
    # expected output:
    expected = 6

    result = pairs_with_given_sum(numbers, target)

    assert expected == result


# @pytest.mark.skip("comment this skip out")
def test_duplicates_identical_pairs():
    # example input:
    numbers = [2,4,4,2]
    target = 6
    # expected output:
    expected = 4

    result = pairs_with_given_sum(numbers, target)

    assert expected == result



