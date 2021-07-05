from mlvizlib.utils.input_validation import check_consistent_length, check_array_type_support
import pytest


def test_check_consistent_length():
    # test that consistent lengths don't cause an error
    assert check_consistent_length([0, 1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1, 0]) is not ValueError


def test_inconsistent_lengths():
    # test that inconsistent lengths cause an error
    with pytest.raises(ValueError):
        check_consistent_length([0, 1, 2, 3], [0, 1, 2])


def test_check_array_type_support():
    # test that unsupported dtype raises TypeError
    with pytest.raises(TypeError):
        check_array_type_support("this should not work")
    # test that None raises ValueError
    with pytest.raises(ValueError):
        check_array_type_support(None)
