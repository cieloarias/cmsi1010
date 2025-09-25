# ----------------------------------------------------------------------
# This is the file data_structures_cardio.py
#
# The intent is to give you practice with tuples, lists, sets, and
# dictionaries.
#
# Complete the functions below.
#
# Each function has a docstring that describes what it should do, but
# please see the unit tests at the bottom of the file for more
# specific examples of what each function should return. To run
# the tests, you can use the command
#
#     python3 -m unittest data_structures_cardio.py
#
# (or python depending on your system).
#
# Remove this comment, and all of the "replace the pass statement..."
# comments, prior to submission. You can, and should, add your own
# comments, but please remove all the comments that are here now.
# ----------------------------------------------------------------------


def third_element(t):
    """
    If t is a tuple with at least three elements, return the third
    element. If t is not a tuple or has fewer than three elements,
    raise an IndexError.
    """
    # replace the pass statement with your code
    pass


def reverse_pair(t):
    """
    if t is a tuple of two elements, return a new tuple with the
    elements in reverse order. If t is not a tuple, raise a TypeError.
    If t is a tuple with more or fewer than two elements, raise a
    ValueError.
    """
    # replace the pass statement with your code
    pass


def middle_element_of_list(a):
    """
    If a is a list with an odd number of elements, return the
    middle element. If a is a list with an even number of elements,
    return the leftmost middle element. If a is a list with no
    elements, raise an IndexError. If a is not a list, raise a
    TypeError.
    """
    # replace the pass statement with your code
    pass


def unique_elements(a):
    """
    Return a set of unique elements from the input list a.
    If a is not a list, raise a TypeError.
    """
    # replace the pass statement with your code
    pass


def contains_duplicates(a):
    """
    Return True if the input list a contains any duplicate elements,
    and False otherwise. If a is not a list, raise a TypeError.
    """
    # replace the pass statement with your code
    pass


def is_superset(a, b):
    """
    Return True if set a is a superset of set b, and False otherwise.
    If either a or b is not a set, raise a TypeError.
    """
    # replace the pass statement with your code
    pass


def is_subset(a, b):
    """
    Return True if set a is a subset of set b, and False otherwise.
    If either a or b is not a set, raise a TypeError.
    """
    # replace the pass statement with your code
    pass


def is_disjoint(a, b):
    """
    Return True if sets a and b are disjoint (i.e., have no elements in common),
    and False otherwise. If either a or b is not a set, raise a TypeError.
    """
    # replace the pass statement with your code
    pass


def most_frequent_value_or_values(d):
    """
    Return the value or values that appear most frequently in the
    dictionary d. If there are multiple values with the same maximum
    frequency, return them as a set. If d is empty, return the empty
    set (because there are no elements to count). If d is not a
    dictionary, raise a TypeError.
    """
    # replace the pass statement with your code
    pass


def key_is_in_both_dictionaries(d1, d2, key):
    """
    Return True if the key is present in both dictionaries d1 and d2,
    and False otherwise. If either d1 or d2 is not a dictionary,
    raise a TypeError.
    """
    # replace the pass statement with your code
    pass


def word_frequencies(s):
    """
    Return a dictionary with the frequency of each word in the string s.
    The keys of the dictionary are the words, and the values are the
    number of times each word appears in the string.

    A word is defined as a sequence of characters separated by spaces.
    You can implement this function using the split method.

    If s is not a string, raise a TypeError.
    """
    # replace the pass statement with your code
    pass


def _assert_raises(exception_type, func, *args):
    try:
        func(*args)
        assert False, "Expected exception not raised"
    except exception_type:
        assert True


def test_third_element():
    assert third_element((1, 2, 3, 4)) == 3
    _assert_raises(IndexError, third_element, (1, 2))
    _assert_raises(IndexError, third_element, (1,))
    _assert_raises(TypeError, third_element, "not a tuple")
    _assert_raises(TypeError, third_element, [1, 2, 3])


def test_reverse_pair():
    assert reverse_pair((1, 2)) == (2, 1)
    _assert_raises(ValueError, reverse_pair, (1, 2, 3))
    _assert_raises(ValueError, reverse_pair, (1,))
    _assert_raises(TypeError, reverse_pair, [1, 2])
    _assert_raises(TypeError, reverse_pair, "not a tuple")


def test_middle_element_of_list():
    assert middle_element_of_list([1, 2, 3]) == 2
    assert middle_element_of_list([1, 2]) == 1
    assert middle_element_of_list([10, 20, 30, 40]) == 20
    assert middle_element_of_list([5] * 500) == 5
    _assert_raises(IndexError, middle_element_of_list, [])
    _assert_raises(TypeError, middle_element_of_list, (1, 2))
    _assert_raises(TypeError, middle_element_of_list, "not a list")


def test_unique_elements():
    assert unique_elements([1, 2, 2, 3]) == {1, 2, 3}
    assert unique_elements([1, 1, 1]) == {1}
    assert unique_elements([]) == set()
    assert unique_elements([1, 2, 3, 4, 5]) == {1, 2, 3, 4, 5}
    assert unique_elements(
        [False, 3, "dog", False, "dog"]) == {False, 3, "dog"}
    _assert_raises(TypeError, unique_elements, "not a list")
    _assert_raises(TypeError, unique_elements, {1, 2, 3})


def test_contains_duplicates():
    assert contains_duplicates([1, 2, 2]) is True
    assert contains_duplicates([1, 2, 3]) is False
    _assert_raises(TypeError, contains_duplicates, "not a list")
    _assert_raises(TypeError, contains_duplicates, {1, 2, 3})


def test_is_superset():
    assert is_superset({1, 2}, {1}) is True
    assert is_superset({1}, {1, 2}) is False
    _assert_raises(TypeError, is_superset, {1}, "not a set")


def test_is_subset():
    assert is_subset({1}, {1, 2}) is True
    assert is_subset({1, 2}, {1}) is False
    _assert_raises(TypeError, is_subset, "not a set", {1})


def test_is_disjoint():
    assert is_disjoint({1}, {2}) is True
    assert is_disjoint({1}, {1}) is False
    _assert_raises(TypeError, is_disjoint, {1}, "not a set")
    _assert_raises(TypeError, is_disjoint, "not a set", {1})


def test_most_frequent_value_or_values():
    assert most_frequent_value_or_values({'a': 1, 'b': 2, 'c': 1}) == {1}
    assert most_frequent_value_or_values({'a': 1, 'b': 2, 'c': 2}) == {2}
    assert most_frequent_value_or_values(
        {'a': 1, 'b': 1, 'c': 2, 'd': 2}) == {1, 2}
    assert most_frequent_value_or_values({}) == set()
    _assert_raises(TypeError, most_frequent_value_or_values, "not a dict")


def test_key_is_in_both_dictionaries():
    assert key_is_in_both_dictionaries(
        {'a': 1, 'b': 2}, {'b': 3, 'c': 4}, 'b') is True
    assert key_is_in_both_dictionaries(
        {'a': 1}, {'b': 2}, 'a') is False
    _assert_raises(
        TypeError,
        key_is_in_both_dictionaries, "not a dict", {'b': 2}, 'b')
    _assert_raises(
        TypeError,
        key_is_in_both_dictionaries, {'a': 1}, "not a dict", 'a')


def test_word_frequencies():
    assert word_frequencies("hello world hello") == {'hello': 2, 'world': 1}
    assert word_frequencies("a b a c b a") == {'a': 3, 'b': 2, 'c': 1}
    assert word_frequencies("test test test") == {'test': 3}
    assert word_frequencies("") == {}
    _assert_raises(TypeError, word_frequencies, 12345)
    _assert_raises(TypeError, word_frequencies, ["not", "a", "string"])
    _assert_raises(TypeError, word_frequencies, {"not": "a string"})


test_third_element()
test_reverse_pair()
test_middle_element_of_list()
test_unique_elements()
test_contains_duplicates()
test_is_superset()
test_is_subset()
test_is_disjoint()
test_most_frequent_value_or_values()
test_key_is_in_both_dictionaries()
test_word_frequencies()
print("All tests passed!")
