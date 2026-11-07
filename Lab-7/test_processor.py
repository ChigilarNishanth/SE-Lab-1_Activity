import pytest
from hypothesis import given, strategies as st
from processor import process_user_age, calculate_average, format_user_name

# Fuzz Test 1: process_user_age
@given(age=st.one_of(st.text(), st.integers(), st.floats(), st.none()))
def test_fuzz_process_user_age(age):
    try:
        result = process_user_age(age)
        assert isinstance(result, int)
        assert 0 <= result <= 120
    except (ValueError, TypeError):
        # Expected handled exceptions
        pass

# Fuzz Test 2: calculate_average
@given(numbers=st.one_of(st.lists(st.integers() | st.floats()), st.none(), st.text()))
def test_fuzz_calculate_average(numbers):
    try:
        result = calculate_average(numbers)
        assert isinstance(result, (int, float))
    except (ValueError, TypeError):
        # Expected handled exceptions
        pass

# Fuzz Test 3: format_user_name
@given(name=st.one_of(st.text(), st.integers(), st.none()))
def test_fuzz_format_user_name(name):
    try:
        result = format_user_name(name)
        assert isinstance(result, str)
        assert len(result) > 0
    except (ValueError, TypeError):
        # Expected handled exceptions
        pass
